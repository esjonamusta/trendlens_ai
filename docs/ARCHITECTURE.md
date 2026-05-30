# Architecture Overview

**TrendLens AI** helps product managers identify and prioritize emerging trends by AI-powered clustering of product discussions and market signals.

**User Problem:** Product managers need to quickly identify and prioritize emerging trends without manually monitoring multiple sources.

**Solution:** AI agents that collect discussions, cluster by topic, analyze why they're trending, and surface opportunities.

## Core Architecture

```
Product Description (Input)
      ↓
Data Collectors (Reddit, HN, GitHub, Twitter, Product Hunt)
      ↓
Normalize & Store Signals
      ↓
Clustering Agent (Group by topic + engagement)
      ↓
Insight Agent (Why is it trending? Opportunities?)
      ↓
Ranked Trends Dashboard
```

### Main Components

**1. Input Layer**
- User provides: product description, category, optional user stories
- Defines scope for data collection

**2. Data Ingestion**
- Multi-source collectors: Reddit, Hacker News, GitHub, Twitter, Product Hunt
- Ingestion Agent fetches relevant discussions autonomously
- Normalizes timestamps, metrics, and metadata
- Stores raw signals in database

**3. AI Clustering & Analysis**
- **Clustering Agent:** Groups related discussions into trend clusters
  - Uses NLP embeddings (semantic similarity)
  - Scores by engagement, momentum, relevance
  - Identifies distinct trends from noise
- **Insight Agent:** Explains WHY clusters are trending
  - Analyzes engagement velocity
  - Identifies emerging opportunities
  - Generates actionable summaries

**4. Storage**
- PostgreSQL + TimescaleDB
- Tables: signals, trends, trend_clusters, analysis_results, agent_runs

**5. API Endpoints**
- `/api/analyze` — Trigger full pipeline
- `/api/trends` — List identified trends with scores
- `/api/trends/{id}` — Trend details + why + opportunities
- `/api/signals` — Raw signals/discussions

**6. Dashboard (Streamlit)**
- Input: product description
- Output: ranked trends with:
  - **Trend name** (what people are talking about)
  - **Score & momentum** (engagement metrics)
  - **Why it's trending** (key factors, sentiment)
  - **Opportunities** (actionable insights)
  - **Evidence** (links to source discussions)

## MVP Scope

**Must have:**
- Data collection from 3+ sources (Reddit, HN, GitHub)
- Basic clustering (semantic grouping + engagement scoring)
- Trend ranking by score
- Simple dashboard showing top trends
- Evidence links to source discussions
- Explanation of why each trend is trending

**Nice-to-have:**
- Voice interface
- Local LLM option
- Real-time updates
- Multi-agent orchestration
- Advanced NLP models

## Design Principles

- **User-centric:** Focus on product manager needs first
- **Fast insights:** Results in seconds, not hours
- **Transparent:** Show WHY trends matter (evidence-based)
- **Actionable:** Surface opportunities, not just data
- **Observable:** All agent reasoning is logged and traceable
