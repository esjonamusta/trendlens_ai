# Architecture Overview

This project uses **AI agents** to autonomously discover and analyze emerging trends across multiple data sources.

## Core Architecture

```
Data Sources → Agents → Analysis → Storage → API → Dashboard
```

### Main Components

**Ingestion:** Collectors for Reddit, Hacker News, Twitter, GitHub, etc.
- Managed by autonomous Ingestion Agent
- Runs on schedule via APScheduler

**Processing:** AI agents for clustering, NLP, and trend detection
- Ingestion Agent: scrapes and normalizes data
- Analysis Agent: detects patterns and clusters
- Insight Agent: generates summaries and predictions

**Storage:** PostgreSQL + TimescaleDB for trend metadata and time-series signals
- Stores raw signals
- Maintains agent memory and conversation history
- Tracks trend evolution

**API:** FastAPI to expose agent capabilities
- Query trends
- Trigger analysis
- Get insights
- Manage agents

**UI:** Streamlit dashboard for browsing trends, filtering, and viewing evidence
- Real-time agent status
- Trend exploration interface
- Insight generation

**Implementation:** See [docs/STACK_DECISION.md](STACK_DECISION.md) for the complete tech stack and setup.

## Design Principles

- **Modular agents:** Each agent is independently testable and replaceable
- **Tool-based:** Agents use tools (API calls) rather than direct database access
- **Observable:** All agent reasoning is logged and traceable
- **Hackathon-ready:** Rapid prototyping with LangChain and Streamlit
