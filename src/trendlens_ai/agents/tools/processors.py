"""Simple processing utilities for embeddings, clustering, and scoring.
These are minimal implementations intended for the hackathon MVP.
"""
from typing import List, Dict, Tuple
import math


def embed_text(text: str) -> List[float]:
    # Deterministic pseudo-embedding: character-level features
    vec = [float(ord(c) % 32) for c in text[:64]]
    return vec


def cluster_by_similarity(items: List[Dict], threshold: float = 0.5) -> List[Tuple[str, List[Dict]]]:
    # Very simple keyword-based clustering for MVP
    clusters = {}
    for item in items:
        title = item.get("title", "")
        # pick the first word as a crude "topic"
        key = title.split()[0].lower() if title else "misc"
        clusters.setdefault(key, []).append(item)
    return [(k, v) for k, v in clusters.items()]


def score_by_engagement(signals: List[Dict]) -> int:
    # Sum up available engagement fields
    score = 0
    for s in signals:
        score += int(s.get("score", 0))
        score += int(s.get("points", 0))
        score += int(s.get("comments", 0))
    return score
