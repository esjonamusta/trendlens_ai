# Emergency Day 2 Sprint Plan

**Status:** 8 hours remaining | Team: 4-5 people | Goal: Working demo with real data + agents + dashboard

---

## 🎯 MVP Focus (Drop Everything Else)

✅ **Must have:**
- Real data flowing (Reddit + Hacker News)
- Agents collecting & analyzing
- Trends showing up in database
- Simple dashboard displaying trends

❌ **Nice-to-have (SKIP):**
- GitHub collector
- Advanced clustering
- Sentiment analysis
- Multi-agent orchestration
- Beautiful UI animations
- Deployment

---

## ⚡ Sprint Breakdown (8 hours)

### Hour 1-2: Quick Setup (Parallel)
**Team split into 2 groups:**

**Group A (Backend Lead + 1):**
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Spin up PostgreSQL in Docker: `docker run -d -e POSTGRES_PASSWORD=password postgres`
- [ ] Create `.env` file with API keys (Reddit, OpenAI)
- [ ] Run `python scripts/init_db.py` to create schema
- [ ] Start FastAPI: `uvicorn src.trendlens_ai.api:app --reload`

**Group B (Frontend Lead + 1):**
- [ ] Create basic folder structure in `src/trendlens_ai/agents/`
- [ ] Create stub `requirements.txt` with: `langchain`, `openai`, `psycopg2`, `praw`, `fastapi`, `streamlit`
- [ ] Create first Streamlit app skeleton: `streamlit run app.py`

---

### Hour 2-4: Minimal Agents (Parallel)
**Group A (Backend Lead + Data Engineer):**
1. Create **one simple Ingestion Agent** (NOT multi-agent yet)
   ```python
   # src/trendlens_ai/agents/simple_ingestion.py
   import praw  # Reddit
   import requests  # HN
   
   def collect_reddit_trends():
       reddit = praw.Reddit(...)
       for post in reddit.subreddit("technology").hot(limit=20):
           return {
               "title": post.title,
               "source": "reddit",
               "score": post.score,
               "url": post.url,
               "timestamp": now()
           }
   
   def collect_hackernews_trends():
       # Similar for HN
       pass
   ```

2. **Simple analysis function** (no ML needed yet):
   ```python
   def analyze_trends(signals):
       # Just group by keyword + sort by score
       trends = {}
       for signal in signals:
           keyword = extract_keyword(signal["title"])
           if keyword not in trends:
               trends[keyword] = []
           trends[keyword].append(signal)
       return sorted(trends.items(), 
                    key=lambda x: sum(s["score"] for s in x[1]), 
                    reverse=True)
   ```

3. **Create API endpoints:**
   ```python
   # src/trendlens_ai/api.py
   @app.post("/api/collect")
   def collect():
       signals = collect_reddit_trends() + collect_hackernews_trends()
       save_to_db(signals)
       return {"collected": len(signals)}
   
   @app.post("/api/analyze")
   def analyze():
       signals = get_from_db()
       trends = analyze_trends(signals)
       save_trends(trends)
       return {"trends": trends}
   
   @app.get("/api/trends")
   def get_trends():
       return get_from_db_trends()
   ```

**Group B (Frontend Lead):**
1. Create basic Streamlit dashboard:
   ```python
   # streamlit_app.py
   import streamlit as st
   import requests
   
   st.title("TrendLens AI - Live Trends")
   
   if st.button("🔄 Collect Data"):
       r = requests.post("http://localhost:8000/api/collect")
       st.success(f"Collected {r.json()['collected']} signals")
   
   if st.button("📊 Analyze Trends"):
       requests.post("http://localhost:8000/api/analyze")
       st.success("Analysis complete")
   
   # Fetch and display trends
   trends = requests.get("http://localhost:8000/api/trends").json()
   
   for trend in trends[:10]:
       st.subheader(trend["name"])
       st.metric("Score", trend["score"])
       st.write(f"Sources: {trend['source_count']}")
       st.divider()
   ```

---

### Hour 4-6: Data Flow (Parallel)
**Group A:** 
- [ ] Test API endpoints with curl/Postman
- [ ] Run collection: `curl -X POST http://localhost:8000/api/collect`
- [ ] Verify data in database
- [ ] Run analysis: `curl -X POST http://localhost:8000/api/analyze`
- [ ] Verify trends created

**Group B:**
- [ ] Connect dashboard to API
- [ ] Add refresh buttons
- [ ] Display real data from database
- [ ] Test on sample data

---

### Hour 6-8: Polish & Demo (Team)
- [ ] Test entire flow end-to-end
- [ ] Fix bugs/errors
- [ ] Add error handling
- [ ] Create demo script:
  1. Click "Collect Data" → loads real Reddit/HN trends
  2. Click "Analyze" → groups into trends
  3. Dashboard shows top 10 trends
- [ ] Take screenshots
- [ ] Write 2-3 slide summary

---

## 📋 Simplified Tech

```
Reddit/HN APIs
      ↓
[Simple Python Functions]
      ↓
FastAPI Endpoints
      ↓
PostgreSQL
      ↓
Streamlit Dashboard
```

**No LangChain agents yet.** Just working code.

---

## 🎬 Demo Script (30 seconds)

1. **Show dashboard:** "Here are 20+ trending topics collected from Reddit and Hacker News in real-time"
2. **Click collect button:** "Fetching latest trends..."
3. **Click analyze button:** "Grouping by topic and scoring by engagement..."
4. **Show results:** "See how we surface emerging trends and their sources"

---

## 🚨 If Running Out of Time

**At Hour 5:** If things are breaking:
- [ ] Drop HN collector, just use Reddit
- [ ] Drop database, use JSON file
- [ ] Just show API responses in terminal (no dashboard)
- [ ] Still shows working system

**At Hour 7:** If still broken:
- [ ] Hardcode 10 sample trends in code
- [ ] Show them on dashboard
- [ ] Narrate what *would* happen with real collectors

---

## File Structure Needed

```
src/trendlens_ai/
├── api.py               # FastAPI endpoints (main file)
├── collectors.py        # Reddit + HN functions
├── analyzer.py          # Simple grouping logic
└── db.py                # Database helpers

streamlit_app.py         # Dashboard

scripts/
└── init_db.py           # Create schema
```

---

## Success Criteria (Bare Minimum)

✅ API returns real Reddit + HN data  
✅ Can group into 5+ trends  
✅ Dashboard displays trends  
✅ Can run demo without crashes  

That's it. Ship it. 🚀

---

## Quick Start Commands

```bash
# Terminal 1: Database
docker run -d --name postgres -e POSTGRES_PASSWORD=password -p 5432:5432 postgres

# Terminal 2: Backend API
python scripts/init_db.py
uvicorn src.trendlens_ai.api:app --reload

# Terminal 3: Frontend Dashboard
streamlit run streamlit_app.py

# Terminal 4: Manual testing
curl -X POST http://localhost:8000/api/collect
```

---

## Next Hackathon Improvements

Once you have a working demo:
- Add LangChain agents (complexity)
- Multi-source collectors
- Real ML clustering
- Cloud deployment
