from fastapi import FastAPI, HTTPException, Query, Header
from typing import Any, List, Optional
import logging
from datetime import datetime, timezone

from .agents.analysis_agent import AnalysisAgent
from .db.session import SessionLocal
from .db import crud
from .agents.tools import storage
from . import scheduler as _scheduler
import os


SCHEDULER_API_KEY = os.getenv("SCHEDULER_API_KEY")


def _require_scheduler_key(x_api_key: Optional[str]):
    if not SCHEDULER_API_KEY:
        # scheduler control disabled if no key configured
        raise HTTPException(status_code=403, detail="Scheduler control disabled")
    if x_api_key != SCHEDULER_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

logger = logging.getLogger("trendlens.api")

app = FastAPI(title="TrendLens AI API")


@app.post("/api/analyze")
def trigger_analysis() -> Any:
    agent = AnalysisAgent()
    try:
        trends = agent.run()
        return {"created": len(trends), "trends": trends}
    except Exception as exc:
        logger.exception("Analysis failed")
        raise HTTPException(status_code=500, detail=str(exc))


@app.get("/api/trends")
def list_trends(limit: int = Query(100, ge=1, le=1000), offset: int = 0, q: Optional[str] = None) -> List[Any]:
    """List trends with pagination and optional name search (`q`)."""
    try:
        db = SessionLocal()
        items = crud.list_trends(db, limit=limit, offset=offset)
        results = []
        for t in items:
            if q and q.lower() not in (t.name or "").lower():
                continue
            results.append({"id": t.id, "name": t.name, "score": t.score, "created_at": t.created_at.isoformat()})
        return results
    except Exception:
        trends = storage.list_trends()
        if q:
            trends = [t for t in trends if q.lower() in (t.get("name") or "").lower()]
        return trends[offset : offset + limit]
    finally:
        try:
            db.close()
        except Exception:
            pass


@app.get("/api/signals")
def list_signals(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = 0,
    source: Optional[str] = None,
    since: Optional[str] = None,
) -> List[Any]:
    """List signals with pagination and optional source and since (ISO date)."""
    since_dt = None
    if since:
        try:
            since_dt = datetime.fromisoformat(since).replace(tzinfo=timezone.utc)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid since date; use ISO format YYYY-MM-DD")
    try:
        db = SessionLocal()
        items = crud.list_signals(db, limit=limit, offset=offset)
        results = []
        for s in items:
            if source and source.lower() != (s.source or "").lower():
                continue
            if since_dt and s.created_at and s.created_at.replace(tzinfo=timezone.utc) < since_dt:
                continue
            results.append({"id": s.id, "title": s.title, "source": s.source, "created_at": s.created_at.isoformat()})
        return results
    except Exception:
        sigs = storage.list_signals()
        if source:
            sigs = [s for s in sigs if s.get("source") and s.get("source").lower() == source.lower()]
        if since_dt:
            def _created_date(s):
                ts = s.get("metadata", {}).get("created_utc")
                try:
                    return datetime.utcfromtimestamp(int(ts))
                except Exception:
                    return None

            sigs = [s for s in sigs if (_created_date(s) and _created_date(s) >= since_dt.replace(tzinfo=None))]
        return sigs[offset : offset + limit]
    finally:
        try:
            db.close()
        except Exception:
            pass


@app.post("/api/scheduler/start")
def scheduler_start(x_api_key: Optional[str] = Header(None)):
    """Start background scheduler (requires X-API-KEY)."""
    _require_scheduler_key(x_api_key)
    try:
        svc = _scheduler.start_scheduler()
        return {"status": "started"}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/api/scheduler/stop")
def scheduler_stop(x_api_key: Optional[str] = Header(None)):
    """Stop background scheduler (requires X-API-KEY)."""
    _require_scheduler_key(x_api_key)
    try:
        _scheduler.stop_scheduler()
        return {"status": "stopped"}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.get("/api/scheduler/status")
def scheduler_status(x_api_key: Optional[str] = Header(None)):
    """Get scheduler status (requires X-API-KEY)."""
    _require_scheduler_key(x_api_key)
    try:
        return _scheduler.scheduler_status()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
