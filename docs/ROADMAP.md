# Roadmap: AI Agent-Driven Trend Detection

**Duration:** 3-day hackathon  
**Team Size:** 4-6 people  
**Goal:** Deploy a working multi-agent system that autonomously discovers trends

---

## 📅 Timeline Overview

| Day | Focus | Goal |
|-----|-------|------|
| **Day 1** | Setup & Agent Foundation | Agents running locally, ingestion working |
| **Day 2** | Integration & Analysis | Full pipeline: ingest → analyze → store |
| **Day 3** | UI & Polish | Dashboard live, demo-ready |

---

## 🎯 Day 1: Foundation & Setup

**Objective:** Get the agent framework running and collect first data

### WP1.1: Environment Setup
**Lead:** DevOps/Backend  
**Time:** 2 hours  
**Tasks:**
- [ ] Clone repo and set up local environment
- [ ] Install Python 3.10+, create virtual env
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Set up PostgreSQL + TimescaleDB locally (Docker Compose)
- [ ] Configure `.env` with API keys (OpenAI/Anthropic, Reddit, etc.)
- [ ] Run `scripts/init_db.py` to initialize schema
- [ ] Verify FastAPI server starts: `uvicorn src.trendlens_ai.api:app --reload`

**Deliverable:** Local stack fully running, team has API keys configured

---

### WP1.2: LangChain Agent Scaffolding
**Lead:** Backend/AI Engineer  
**Time:** 3 hours  
**Tasks:**
- [ ] Create base agent class with LangChain
- [ ] Set up Crew AI orchestrator
- [ ] Define agent roles and responsibilities
- [ ] Create tool registry for agent functions
- [ ] Set up agent logging and tracing
- [ ] Create `src/trendlens_ai/agents/` folder structure
- [ ] Write agent tests

**Deliverable:** Agent framework ready, example agent passes tests

**File structure:**
```
src/trendlens_ai/agents/
├── __init__.py
├── base_agent.py        # Base class for all agents
├── ingestion_agent.py   # Data collection
├── analysis_agent.py    # Pattern detection
├── insight_agent.py     # Summary generation
├── orchestrator.py      # Multi-agent coordinator
└── tools/
    ├── __init__.py
    ├── data_fetchers.py  # Reddit, HN, GitHub APIs
    ├── processors.py     # NLP, clustering
    └── storage.py        # DB operations
```

---

### WP1.3: Ingestion Agent v1
**Lead:** Backend/Data Engineer  
**Time:** 4 hours  
**Tasks:**
- [ ] Implement Reddit data collector (PRAW)
- [ ] Implement Hacker News collector (API)
- [ ] Implement GitHub trends collector (API)
- [ ] Create data normalization functions
- [ ] Create `fetch_*()` tools for agent
- [ ] Write unit tests
- [ ] Test collecting 100+ records from each source

**Deliverable:** Agent can autonomously collect data, store to database

**Example agent prompt:**
```
You are the Ingestion Agent. Your job is to:
1. Fetch trending data from Reddit, Hacker News, GitHub
2. Normalize timestamps and metadata
3. Store records in the database
4. Report what you collected

Available tools: fetch_reddit(), fetch_hackernews(), fetch_github(), store_record()
```

---

### WP1.4: Database Schema & Storage Layer
**Lead:** Backend/Data Engineer  
**Time:** 2 hours  
**Tasks:**
- [ ] Design schema for trends, signals, agent runs
- [ ] Create SQLAlchemy ORM models
- [ ] Add indices for time-series queries
- [ ] Create helper functions for CRUD operations
- [ ] Write migration scripts
- [ ] Add agent memory tables (for state, conversation history)
- [ ] Test schema with sample data

**Deliverable:** Database ready to accept data and agent state

**Tables needed:**
- `signals` — raw data points (timestamp, source, content, metadata)
- `trends` — identified trends (name, created_at, score)
- `agent_runs` — execution history (agent_id, status, output)
- `agent_memory` — agent state and chat history

---

## End of Day 1 Checkpoint

✅ Team can run agents locally  
✅ Ingestion agent collects data  
✅ Data persists in database  
✅ CI/CD pipeline works  

**Daily standup:** Review data quality, adjust collectors if needed

---

## 🎯 Day 2: Agent Intelligence & Pipeline

**Objective:** Implement analysis and make decisions; create full data flow

### WP2.1: Analysis Agent
**Lead:** AI/ML Engineer  
**Time:** 4 hours  
**Tasks:**
- [ ] Implement clustering with scikit-learn (K-means, DBSCAN)
- [ ] Add NLP preprocessing (spaCy, tokenization)
- [ ] Implement sentiment analysis
- [ ] Detect trend anomalies (statistical methods)
- [ ] Create `cluster_signals()`, `compute_sentiment()`, `find_anomalies()` tools
- [ ] Write unit tests
- [ ] Test analysis on Day 1 collected data

**Deliverable:** Agent can identify patterns and emerging trends

**Example agent prompt:**
```
You are the Analysis Agent. Your job is to:
1. Fetch recent signals from the database
2. Cluster similar signals using NLP
3. Compute sentiment and engagement metrics
4. Detect anomalies (unusual spikes)
5. Create trend records for significant clusters
6. Store analysis results

Available tools: cluster_signals(), compute_sentiment(), find_anomalies(), create_trend()
```

---

### WP2.2: API Endpoints
**Lead:** Backend Engineer  
**Time:** 3 hours  
**Tasks:**
- [ ] Create `/api/trends` endpoint (list all trends)
- [ ] Create `/api/trends/{id}` endpoint (trend details)
- [ ] Create `/api/analyze` endpoint (trigger analysis)
- [ ] Create `/api/agents/status` endpoint (agent health)
- [ ] Create `/api/signals` endpoint (raw signals query)
- [ ] Add pagination and filtering
- [ ] Write API documentation
- [ ] Test with Postman/curl

**Deliverable:** API ready for frontend consumption

---

### WP2.3: Task Scheduler
**Lead:** Backend Engineer  
**Time:** 2 hours  
**Tasks:**
- [ ] Set up APScheduler
- [ ] Create jobs for ingestion (every 1-2 hours)
- [ ] Create jobs for analysis (every 4 hours)
- [ ] Create scheduler monitoring dashboard
- [ ] Write logs for each job
- [ ] Test scheduler with dummy jobs
- [ ] Set up graceful shutdown

**Deliverable:** Background agents run autonomously on schedule

---

### WP2.4: Insight Agent v1
**Lead:** AI/ML Engineer  
**Time:** 3 hours  
**Tasks:**
- [ ] Implement LLM-based summary generation
- [ ] Create trend report templates
- [ ] Implement prediction logic (trend trajectory)
- [ ] Create `generate_report()` and `forecast_trend()` tools
- [ ] Write prompts for Claude/GPT-4
- [ ] Test with real trend data
- [ ] Optimize token usage

**Deliverable:** Agent generates human-readable insights

---

### WP2.5: Agent Orchestration
**Lead:** Backend/AI Engineer  
**Time:** 2 hours  
**Tasks:**
- [ ] Connect all three agents into workflow
- [ ] Create orchestrator that coordinates tasks
- [ ] Handle agent failures and retries
- [ ] Log agent reasoning and decisions
- [ ] Create monitoring/debugging tools
- [ ] Test end-to-end pipeline

**Deliverable:** Multi-agent system works together seamlessly

---

## End of Day 2 Checkpoint

✅ Agents collect, analyze, and generate insights  
✅ API endpoints working  
✅ Background scheduler active  
✅ Full data pipeline: collect → analyze → report  

**Daily standup:** Check trend quality, data accuracy, agent reasoning logs

---

## 🎯 Day 3: UI, Polish & Demo

**Objective:** Beautiful interface + demo-ready system

### WP3.1: Streamlit Dashboard
**Lead:** Frontend Engineer  
**Time:** 4 hours  
**Tasks:**
- [ ] Create main dashboard layout
- [ ] Implement trends browser (sortable, filterable)
- [ ] Show trend details with evidence
- [ ] Add real-time signal ingestion view
- [ ] Create agent status monitor
- [ ] Add manual trigger buttons for agents
- [ ] Implement search functionality
- [ ] Add charts for trend evolution

**Deliverable:** Functional dashboard for trend exploration

**Key pages:**
- Trends overview (list, sort by score/date)
- Trend detail (sources, sentiment, evidence)
- Live feed (incoming signals)
- Agent monitor (status, last run, logs)

---

### WP3.2: Data Quality & Fine-tuning
**Lead:** Data/ML Engineer  
**Time:** 3 hours  
**Tasks:**
- [ ] Review collected trends for quality
- [ ] Remove duplicates/spam
- [ ] Adjust clustering parameters
- [ ] Improve sentiment analysis accuracy
- [ ] Fine-tune anomaly detection
- [ ] Validate API responses
- [ ] Check database performance

**Deliverable:** Polished data, accurate trends

---

### WP3.3: Documentation & Demo Script
**Lead:** Tech Lead  
**Time:** 2 hours  
**Tasks:**
- [ ] Write API documentation
- [ ] Create agent documentation
- [ ] Add dashboard user guide
- [ ] Write demo script (story to tell)
- [ ] Create architecture diagram slides
- [ ] Prepare talking points
- [ ] Record demo video (backup)

**Deliverable:** Ready for presentation

---

### WP3.4: Deployment & Testing
**Lead:** DevOps/Backend  
**Time:** 2 hours  
**Tasks:**
- [ ] Create production Docker images
- [ ] Test deployment to staging environment
- [ ] Set up GitHub Actions CI/CD
- [ ] Create `.env.example` with all required keys
- [ ] Write deployment README
- [ ] Prepare backup demo (local version)
- [ ] Test all APIs on deployed version

**Deliverable:** One-click deployment ready

---

### WP3.5: Polish & Bug Fixes
**Lead:** Team (parallel)  
**Time:** 2 hours  
**Tasks:**
- [ ] Fix any bugs found during testing
- [ ] Improve error handling
- [ ] Add loading states/spinners in UI
- [ ] Optimize performance (slow endpoints)
- [ ] Add error messages and help text
- [ ] Final code review
- [ ] Clean up logs and comments

**Deliverable:** Production-quality code

---

## End of Day 3 Checkpoint

✅ Dashboard live and responsive  
✅ Full system deployed and tested  
✅ Demo script ready  
✅ All documentation complete  

**Final: Presentation & Demo** 🎉

---

## 📊 Work Package Summary

| WP | Title | Owner | Day | Hours | Status |
|----|-------|-------|-----|-------|--------|
| 1.1 | Environment Setup | DevOps | D1 | 2 | 🔄 In Progress |
| 1.2 | Agent Scaffolding | Backend | D1 | 3 | ⏳ Not Started |
| 1.3 | Ingestion Agent v1 | Backend/Data | D1 | 4 | ⏳ Not Started |
| 1.4 | Database Schema | Backend/Data | D1 | 2 | ⏳ Not Started |
| 2.1 | Analysis Agent | AI/ML | D2 | 4 | ⏳ Not Started |
| 2.2 | API Endpoints | Backend | D2 | 3 | ⏳ Not Started |
| 2.3 | Task Scheduler | Backend | D2 | 2 | ⏳ Not Started |
| 2.4 | Insight Agent v1 | AI/ML | D2 | 3 | ⏳ Not Started |
| 2.5 | Orchestration | Backend/AI | D2 | 2 | ⏳ Not Started |
| 3.1 | Streamlit Dashboard | Frontend | D3 | 4 | ⏳ Not Started |
| 3.2 | Data Quality | Data/ML | D3 | 3 | ⏳ Not Started |
| 3.3 | Documentation | Tech Lead | D3 | 2 | ⏳ Not Started |
| 3.4 | Deployment | DevOps | D3 | 2 | ⏳ Not Started |
| 3.5 | Polish & Bugs | Team | D3 | 2 | ⏳ Not Started |

**Total:** ~40 hours of work across team

---

## 🚨 Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| API rate limits | Blocked data collection | Use caching, backoff strategy |
| Agent hallucinations | Bad trends | Validate LLM outputs, human review |
| Database slowness | Poor UX | Add indices, pagination, caching |
| Team coordination | Merge conflicts | Clear branch strategy, daily standups |
| Time pressure | Incomplete features | Prioritize MVP, drop nice-to-haves |

---

## 📈 Success Metrics

- ✅ 3+ data sources ingesting live data
- ✅ Agents autonomously running without manual intervention
- ✅ Dashboard displaying 10+ real trends
- ✅ API responding in <500ms
- ✅ Zero critical bugs at demo time
- ✅ Team presents working end-to-end system

---

## 🔄 Post-Hackathon (if continuing)

- Multi-agent collaboration improvements
- Advanced ML models for trend prediction
- Authentication & multi-user support
- Scaling to cloud infrastructure
- Mobile app
- Notification system
- Integration with external dashboards
