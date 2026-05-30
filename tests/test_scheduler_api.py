import os
from fastapi.testclient import TestClient
from trendlens_ai.api import app


def test_scheduler_start_stop(monkeypatch):
    # ensure the API key used by the API module is set
    monkeypatch.setattr("trendlens_ai.api.SCHEDULER_API_KEY", "secret-key", raising=False)

    # monkeypatch start/stop to avoid running BackgroundScheduler
    started = {}

    def fake_start():
        started["ok"] = True
        return "ok"

    def fake_stop():
        started["stop"] = True

    monkeypatch.setattr("trendlens_ai.api._scheduler.start_scheduler", fake_start)
    monkeypatch.setattr("trendlens_ai.api._scheduler.stop_scheduler", fake_stop)

    client = TestClient(app)
    headers = {"X-API-KEY": "secret-key"}
    r = client.post("/api/scheduler/start", headers=headers)
    assert r.status_code == 200 and r.json().get("status") == "started"

    r2 = client.post("/api/scheduler/stop", headers=headers)
    assert r2.status_code == 200 and r2.json().get("status") == "stopped"


def test_scheduler_status(monkeypatch):
    monkeypatch.setattr("trendlens_ai.api.SCHEDULER_API_KEY", "secret-key", raising=False)

    def fake_status():
        return {"running": True, "available": True}

    monkeypatch.setattr("trendlens_ai.api._scheduler.scheduler_status", fake_status)

    client = TestClient(app)
    headers = {"X-API-KEY": "secret-key"}
    r = client.get("/api/scheduler/status", headers=headers)
    assert r.status_code == 200
    assert r.json() == {"running": True, "available": True}
