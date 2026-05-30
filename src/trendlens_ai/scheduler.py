import logging
from typing import Optional

from .agents.ingestion_agent import IngestionAgent
from .agents.analysis_agent import AnalysisAgent

logger = logging.getLogger("trendlens.scheduler")

# Try to import APScheduler; if unavailable, provide a lightweight no-op fallback
try:
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.triggers.interval import IntervalTrigger
    APSCHEDULER_AVAILABLE = True
except Exception:
    BackgroundScheduler = None  # type: ignore
    IntervalTrigger = None  # type: ignore
    APSCHEDULER_AVAILABLE = False


class SchedulerService:
    def __init__(self):
        self.running = False
        if APSCHEDULER_AVAILABLE:
            self.scheduler = BackgroundScheduler()
        else:
            self.scheduler = None

    def start(self):
        logger.info("Starting SchedulerService")
        if APSCHEDULER_AVAILABLE and self.scheduler is not None:
            # ingestion every hour
            self.scheduler.add_job(self._run_ingest, IntervalTrigger(hours=1), id="ingest_job", replace_existing=True)
            # analysis every 4 hours
            self.scheduler.add_job(self._run_analysis, IntervalTrigger(hours=4), id="analysis_job", replace_existing=True)
            self.scheduler.start()
        else:
            # fallback: mark running but do not schedule jobs
            logger.warning("APScheduler not available; scheduler will be no-op")
        self.running = True

    def shutdown(self, wait: bool = True):
        logger.info("Shutting down SchedulerService")
        if APSCHEDULER_AVAILABLE and self.scheduler is not None:
            self.scheduler.shutdown(wait=wait)
        self.running = False

    def _run_ingest(self):
        try:
            logger.info("Scheduler: running ingestion job")
            agent = IngestionAgent("scheduled-ingest")
            agent.run(query="scheduled", limit=50)
        except Exception:
            logger.exception("Ingestion job failed")

    def _run_analysis(self):
        try:
            logger.info("Scheduler: running analysis job")
            agent = AnalysisAgent()
            agent.run()
        except Exception:
            logger.exception("Analysis job failed")


_service: Optional[SchedulerService] = None


def start_scheduler() -> SchedulerService:
    global _service
    if _service is None:
        _service = SchedulerService()
        _service.start()
    return _service


def stop_scheduler():
    global _service
    if _service is not None:
        _service.shutdown()
        _service = None


def scheduler_status():
    if _service is None:
        return {"running": False, "available": APSCHEDULER_AVAILABLE}
    return {"running": _service.running, "available": APSCHEDULER_AVAILABLE}
