"""Lightweight data fetcher stubs for MVP.
These functions are intentionally simple and return deterministic sample data
so the non-technical team can demo without external API keys during the hackathon.
Replace with real API calls (PRAW, requests) when available.
"""
from typing import List, Dict
import time


def fetch_reddit(query: str, limit: int = 20) -> List[Dict]:
    # Stubbed sample data
    time.sleep(0.1)
    return [
        {"title": f"Sample Reddit post about {query} #{i}", "source": "reddit", "score": 100 - i, "url": "https://reddit.example/post/" + str(i)}
        for i in range(limit)
    ]


def fetch_hackernews(query: str, limit: int = 20) -> List[Dict]:
    time.sleep(0.05)
    return [
        {"title": f"HN story on {query} #{i}", "source": "hackernews", "points": 200 - i, "url": "https://news.ycombinator.example/item/" + str(i)}
        for i in range(limit)
    ]


def fetch_github(query: str, limit: int = 20) -> List[Dict]:
    time.sleep(0.05)
    return [
        {"title": f"GitHub issue about {query} #{i}", "source": "github", "comments": i % 5, "url": "https://github.example/issue/" + str(i)}
        for i in range(limit)
    ]
