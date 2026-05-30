# Stack Decision

**Status:** ✅ DECIDED  
**Date:** May 30, 2026  
**Product:** TrendLens AI - AI-Powered Trend Discovery for Product Managers  
**Focus:** Collect → Cluster → Analyze → Visualize

## Problem Statement

Product managers spend hours monitoring multiple sources (Reddit, GitHub, HN, Twitter, Product Hunt) to spot emerging trends. They need an **AI tool that autonomously discovers trends, clusters related discussions, and surfaces actionable opportunities**.

## Target User

Product managers, founders, strategists who need to identify and prioritize emerging market opportunities without manual research.

## MVP Scope

**User Input:** Product description or category focus  

**Processing Pipeline:**
1. **Collect:** Fetch relevant discussions from Reddit, GitHub, HN, Twitter, Product Hunt
2. **Cluster:** Group related discussions using AI (semantic similarity + engagement scoring)
3. **Analyze:** Use LLM to explain WHY trends are emerging + identify opportunities
4. **Visualize:** Display ranked trends with evidence and actionable insights

**MVP Output:**
- Ranked list of top 10-20 emerging trends
- For each trend:
  - **Trend name** (what people are discussing)
  - **Momentum score** (engagement, growth velocity)
  - **Why it's trending** (key factors, sentiment analysis)
  - **Suggested opportunities** (actionable next steps)
  - **Evidence** (links to source discussions, quote samples)

## Chosen Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Language** | Python 3.10+ | Rich ecosystem for AI/ML, LangChain support, team familiarity |
| **Agent Framework** | LangChain + Crew AI | Multi-agent orchestration, function calling, tool integration |
| **LLM** | Claude 3.5 (Anthropic) or GPT-4 | Advanced reasoning for trend analysis |
| **Backend API** | FastAPI | Async support, automatic docs, agent endpoint exposure |
| **Database** | PostgreSQL + TimescaleDB | Time-series trends, agent memory/state |
| **Task Scheduler** | APScheduler or Celery | Periodic ingestion, background agent runs |
| **UI** | Streamlit | Rapid prototyping, agent interaction, real-time monitoring |
| **Deployment** | Docker + GitHub Actions | Reproducible environments, CI/CD pipeline |

## Architecture Overview

```
┌──────────────────────────────────────────────────────────┐
│                    User Interface (Streamlit)            │
└──────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────┐
│            FastAPI Backend (Agent Endpoints)             │
│  • /api/trends                                           │
│  • /api/analyze                                          │
│  • /api/insights                                         │
└──────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────┐
│                   LangChain Agents                       │
│  ┌─────────────────┐  ┌─────────────────┐               │
│  │ Ingestion Agent │  │ Analysis Agent  │               │
│  │ (Scrape data)   │  │ (Find patterns) │               │
│  └─────────────────┘  └─────────────────┘               │
│  ┌─────────────────┐  ┌─────────────────┐               │
│  │ Insight Agent   │  │ Orchestrator    │               │
│  │ (Generate)      │  │ (Multi-agent)   │               │
│  └─────────────────┘  └─────────────────┘               │
└──────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────┐
│              Tools & External Services                   │
│  • Reddit API         • Sentiment Analysis               │
│  • Hacker News API    • Clustering (scikit-learn)        │
│  • GitHub API         • Web Search                       │
│  • Twitter/X API      • Database Storage                 │
└──────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────┐
│       PostgreSQL + TimescaleDB (Storage & Memory)        │
│  • Trend records          • Agent conversation history   │
│  • Time-series signals    • Analysis results             │
└──────────────────────────────────────────────────────────┘
```

## Key Agents

### 1. **Ingestion Agent**
- **Input:** Product description from user
- **Task:** Autonomously collect relevant discussions from Reddit, HN, GitHub, Twitter, Product Hunt
- **Run:** On-demand (MVP) or scheduled (future)
- **Output:** Normalized signals stored in database
- **Tools:** 
  - `fetch_reddit(query)` → posts + comments
  - `fetch_hackernews(query)` → stories + discussions
  - `fetch_github(query)` → issues + PRs + discussions
  - `fetch_twitter(query)` → tweets + threads
  - `fetch_producthunt()` → product launches
  - `normalize_signal(raw_data)` → clean, standardized format

### 2. **Clustering Agent**
- **Input:** Normalized signals from database
- **Task:** Group related discussions into semantic clusters (trends)
- **Method:** 
  - NLP embeddings (spaCy or OpenAI embeddings)
  - Semantic similarity clustering
  - Score by engagement (upvotes, replies, momentum)
- **Output:** Trend clusters with:
  - Cluster ID & name (auto-generated or LLM-named)
  - Size (number of signals)
  - Aggregated score/engagement
  - Timeline (first seen to latest)
- **Tools:**
  - `embed_text(text)` → embedding vector
  - `cluster_by_similarity(embeddings, threshold)` → cluster assignments
  - `score_by_engagement(signals)` → engagement scores
  - `extract_trend_name(signals)` → LLM-generated trend name

### 3. **Insight Agent**
- **Input:** Trend clusters + original signals
- **Task:** Analyze WHY clusters are trending + identify opportunities
- **Method:** 
  - LLM reasoning on signals, sentiment, velocity
  - Extract key themes and narratives
  - Identify emerging opportunities
  - Suggest product actions
- **Output:** For each trend:
  - Why is it trending? (sentiment, engagement velocity, mentions)
  - Opportunities (market gaps, feature suggestions)
  - Competitive landscape
  - Suggested actions
- **Tools:**
  - `analyze_sentiment(signals)` → sentiment distribution
  - `calculate_velocity(signals)` → growth trend
  - `extract_themes(signals)` → key topics/narratives
  - `generate_opportunity_report(trend)` → LLM-generated opportunities
  - `rank_by_opportunity_score(trends)` → prioritized list

### 4. **Orchestrator Agent** (MVP: simple, can be enhanced)
- **MVP:** Simple sequential execution (collect → cluster → analyze)
- **Future:** Parallel execution, error handling, re-runs
- **Task:** Coordinate multi-agent workflow, manage state, return final results

## Dependencies

```toml
# AI & Agents
langchain = "^0.1"
crew-ai = "^0.1"
anthropic = "^0.7"  # Claude API
openai = "^1.0"      # GPT-4 (alternative)

# Backend
fastapi = "^0.104"
uvicorn = "^0.24"
pydantic = "^2.0"

# Database
psycopg2-binary = "^2.9"
sqlalchemy = "^2.0"
timescaledb = "^1.1"

# Data Processing
numpy = "^1.24"
pandas = "^2.0"
scikit-learn = "^1.3"
spacy = "^3.7"

# Task Scheduling
apscheduler = "^3.10"

# UI
streamlit = "^1.28"

# Utilities
python-dotenv = "^1.0"
requests = "^2.31"
praw = "^7.7"  # Reddit API
```

## Setup Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add API keys: OPENAI_API_KEY, ANTHROPIC_API_KEY, REDDIT_CLIENT_ID, etc.

# Initialize database
python scripts/init_db.py

# Run backend
uvicorn src.trendlens_ai.api:app --reload

# Run UI (in separate terminal)
streamlit run src/trendlens_ai/ui/app.py

# Run background agent workers (in separate terminal)
python src/trendlens_ai/workers/scheduler.py
```

## Why This Stack?

✅ **Agent-native:** LangChain + Crew AI designed for multi-agent systems  
✅ **Hackathon speed:** Streamlit + FastAPI reduce boilerplate  
✅ **Scalable:** PostgreSQL + TimescaleDB for long-term trend data  
✅ **Team-ready:** Python dominates AI/ML hiring, low onboarding friction  
✅ **Flexible:** LLM choice (Claude/GPT-4) can change without refactor  
✅ **Observable:** Agent reasoning is traceable and debuggable  

## Alternatives Considered

| Option | Pros | Cons | Status |
|--------|------|------|--------|
| LangChain + Crew | Multi-agent, composable | Steeper learning curve | ✅ **CHOSEN** |
| AutoGen | Collaborative agents | Heavy, research-oriented | ⏳ Future |
| Node.js + LangChain | Full JS stack | Smaller ML ecosystem | ❌ Rejected |
| Serverless (AWS Lambda) | Scaling, cost | Cold starts, agent state management | ⏳ Future |

## Deployment Plan

1. **Development:** Local Docker containers
2. **Staging:** GitHub Actions CI, test agents on PR
3. **Production:** Docker on cloud (Render, Railway, or self-hosted)
4. **Monitoring:** Agent execution logs, trend accuracy metrics

## Next Steps

- [ ] Set up PostgreSQL + TimescaleDB locally
- [ ] Create agent scaffolding with LangChain
- [ ] Implement Ingestion Agent first
- [ ] Build API endpoints
- [ ] Create Streamlit dashboard
- [ ] Set up CI/CD pipeline
