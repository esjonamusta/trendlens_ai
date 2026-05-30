"""Minimal storage helpers used by agents during the hackathon.
Currently implemented as in-memory collections for simplicity; can be
replaced with real database calls (SQLAlchemy) later.
"""
from typing import Dict, List

_signals: List[Dict] = []
_trends: List[Dict] = []


def save_signal(signal: Dict) -> None:
    _signals.append(signal)


def list_signals() -> List[Dict]:
    return list(_signals)


def save_trend(trend: Dict) -> None:
    _trends.append(trend)


def list_trends() -> List[Dict]:
    return list(_trends)


def clear_storage():
    _signals.clear()
    _trends.clear()
