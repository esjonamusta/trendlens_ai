# Stack Decision

**Status:** ✅ DECIDED  
**Date:** May 30, 2026  
**Focus:** AI Agent-Driven Trend Detection

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
- Autonomously collect data from Reddit, Hacker News, GitHub, etc.
- Runs on schedule (APScheduler)
- Stores raw signals in database
- Tool functions: `fetch_reddit()`, `fetch_hackernews()`, `fetch_github()`

### 2. **Analysis Agent**
- Processes raw signals for patterns
- Uses NLP to cluster similar topics
- Detects emerging trends via statistical analysis
- Tool functions: `cluster_signals()`, `compute_sentiment()`, `find_anomalies()`

### 3. **Insight Agent**
- Synthesizes analysis into human-readable insights
- Generates summaries and predictions
- Answers user queries about trends
- Tool functions: `query_trends()`, `generate_report()`, `forecast()`

### 4. **Orchestrator Agent** (optional)
- Coordinates multi-agent workflows
- Delegates tasks based on priority
- Manages resource allocation

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
