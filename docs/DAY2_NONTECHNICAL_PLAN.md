# Day 2 Sprint Plan (Non-Technical Guide)

**Date:** Tomorrow (Day 2 of hackathon)  
**Time Available:** ~8 hours (9 AM - 5 PM with breaks)  
**Team Size:** 4-5 people  
**Goal:** Have a working demo that shows real trends collected from the internet

---

## 🎯 What Are We Building Today?

Imagine a **tool that automatically finds what people are talking about on Reddit, GitHub, and news sites**, groups the similar conversations together, and shows you the **top trending topics with why they matter**.

**End Result:** A simple web interface where you type a product name, hit a button, and it shows you the top 10 trending topics related to that product.

---

## 📋 Team Roles & Responsibilities

### Role 1: **Backend Developer** (Technical)
- Writes the code that connects to Reddit, GitHub, etc.
- Sets up the database
- Creates the API (the "brain" of the system)
- **Lead Person:** Pick your strongest programmer

### Role 2: **Data Analyst / AI Specialist** (Semi-Technical)
- Works on clustering (grouping similar topics)
- Analyzes sentiment (is it positive or negative?)
- Explains WHY topics are trending
- **Lead Person:** Someone comfortable with data/Excel

### Role 3: **Frontend Developer** (Technical)
- Builds the visual dashboard (what users see)
- Connects the dashboard to the backend
- Makes it look good and work smoothly
- **Lead Person:** Someone who can code web interfaces (React/Streamlit)

### Role 4: **Product Manager / QA** (Non-Technical)
- Tests everything works correctly
- Writes the demo script
- Prepares the presentation
- **Lead Person:** Organized, detail-oriented person

### Role 5: **DevOps / Setup Lead** (Technical)
- Gets everyone's computers set up
- Installs all the software needed
- Makes sure everyone can start at the same time
- **Lead Person:** Person comfortable with terminals/installation

---

## ⚡ Hour-by-Hour Breakdown

### **Hour 1 (9:00-10:00 AM): Setup & Kickoff**

**What:** Get everyone's computer ready to code  
**Who:** DevOps Lead + Backend Dev  
**What Gets Done:** Everyone can run the basic code and see it working locally

#### Step-by-Step for Everyone:

1. **Backend Dev + DevOps Lead:**
   - [ ] Download all the software packages we need
   - [ ] Create a database on your computer (like a storage box for data)
   - [ ] Start the "backend server" (the brain of our app)
   - [ ] Verify it's running by checking the computer says "Server is running"

2. **Frontend Dev + DevOps Lead:**
   - [ ] Download the UI starter code
   - [ ] Get Streamlit installed (the tool for making the visual interface)
   - [ ] Start the dashboard and see a blank screen appear in browser

3. **Product Manager:**
   - [ ] Create the demo script document
   - [ ] Set up a checklist for what needs to work by end of day
   - [ ] Test that you can open the web browser and see the dashboard

4. **Data Analyst:**
   - [ ] Get Python and data science tools installed
   - [ ] Review what "clustering" means (grouping similar topics)

**Checkpoint:** Everyone can see:
- ✅ Backend server running
- ✅ Dashboard page loading in browser  
- ✅ No errors in the code

**Time buffer if problems:** 15 minutes

---

### **Hour 2-3 (10:00 AM-12:00 PM): Collect Real Data**

**What:** Make the system go out to Reddit and GitHub and grab real trending topics  
**Who:** Backend Dev + Data Analyst  
**What Gets Done:** Database has 100+ real discussions from people online

#### Step-by-Step:

1. **Backend Dev:**
   - [ ] Write code to log into Reddit (with permission keys we provide)
   - [ ] Search Reddit for trending topics in tech category
   - [ ] Grab the top 50 posts about technology
   - [ ] Do the same for GitHub repositories
   - [ ] Do the same for Hacker News
   - [ ] Save all this data to the database in a clean, organized way

2. **Data Analyst:**
   - [ ] Watch the data come in
   - [ ] Check: "Does this look right? Are these real trending topics?"
   - [ ] Make notes about what topics appear most
   - [ ] Flag any weird/spam posts to be removed later

3. **Product Manager:**
   - [ ] Sample 5-10 of the raw posts and read them
   - [ ] Understand what data looks like before processing
   - [ ] Update checklist: "✅ Data collected"

**Example of What We're Collecting:**
```
Post Title: "AI agents are transforming software development"
Source: Reddit
Upvotes: 2,543
Comments: 487
Link: reddit.com/r/programming/...

Post Title: "GPT-4 Can Now Code Better Than Senior Developers"
Source: Hacker News
Points: 1,234
Comments: 523
Link: news.ycombinator.com/...
```

**Checkpoint:**
- ✅ 100+ posts in database from 3 sources
- ✅ Data looks clean and relevant
- ✅ No errors during collection

**Time buffer:** 10 minutes

---

### **Hour 4-5 (12:00-2:00 PM): Group Similar Topics (Clustering)**

**What:** Take all the posts and automatically group similar ones together (e.g., all AI-related posts in one group, all crypto posts in another)  
**Who:** Data Analyst + Backend Dev  
**What Gets Done:** 10-15 clear topic groups are created

#### Step-by-Step Explanation for Non-Tech:

Imagine you have 100 articles. We want to read them and group similar ones:
- All articles about "AI" go in pile 1
- All articles about "Web3" go in pile 2
- All articles about "Remote Work" go in pile 3
- Etc.

**How We Do This:**
1. **Analyze words in each post:** Look for keywords (AI, agents, LLM, ChatGPT, etc.)
2. **Score engagement:** Count upvotes and comments (more popular = higher score)
3. **Group similar posts:** Posts with similar words and high engagement are grouped together

#### Step-by-Step for Team:

1. **Data Analyst:**
   - [ ] Review the 100 posts manually - what themes do you see?
   - [ ] List the top 10-15 topics you notice
   - [ ] Example: "AI Agents", "LLMs in Production", "GitHub Copilot", "Voice Interfaces", "Local AI"

2. **Backend Dev:**
   - [ ] Write code that does this automatically using AI
   - [ ] System reads each post and assigns it to a topic group
   - [ ] Calculates a "score" for each group based on engagement
   - [ ] Saves the groups to database with names

3. **Data Analyst (Check):**
   - [ ] Look at the computer's groupings
   - [ ] Does it make sense? Is it grouping correctly?
   - [ ] If not, adjust the settings and try again
   - [ ] Goal: Get to 10-15 clean, distinct trend clusters

4. **Frontend Dev (Prepare):**
   - [ ] Create API endpoint that returns the grouped trends
   - [ ] Test that the endpoint works: `GET /api/trends` returns JSON with trends

**Example Output:**
```
Trend 1: "AI Agents"
  - Posts grouped: 23
  - Total engagement score: 8,542
  - Keywords: agent, AI, autonomous, LLM

Trend 2: "Local AI / On-Device ML"
  - Posts grouped: 18
  - Total engagement score: 5,231
  - Keywords: local, on-device, privacy, open source

Trend 3: "Voice Interfaces & Audio AI"
  - Posts grouped: 12
  - Total engagement score: 3,890
  - Keywords: voice, audio, speech, voice-to-text
```

**Checkpoint:**
- ✅ 10-15 trend clusters created
- ✅ Each cluster has 5+ posts grouped correctly
- ✅ API endpoint returns the trends as JSON

**Time buffer:** 15 minutes

---

### **Hour 5-6 (2:00-3:30 PM): Add Explanations (Why Are These Trending?)**

**What:** For each trend group, write explanations for WHY it's trending  
**Who:** Data Analyst + Backend Dev  
**What Gets Done:** Each trend has a clear explanation + suggested opportunities

#### Step-by-Step:

1. **Data Analyst:**
   - [ ] For each of the 10-15 trends, read 5-10 posts
   - [ ] Answer these questions:
     - Why are people talking about this?
     - Is sentiment positive or negative?
     - Is this growing or declining?
     - What opportunity does this represent?
   - [ ] Write a 1-2 sentence explanation for each trend

2. **Backend Dev:**
   - [ ] Create system that uses AI to auto-generate these explanations
   - [ ] Add to each trend in database:
     - "Why it's trending" (generated by AI)
     - "Sentiment" (positive/negative/neutral)
     - "Momentum" (growing/stable/declining)
     - "Suggested opportunity" (what product could address this)

3. **Example Explanation:**
   ```
   TREND: "AI Agents"
   
   Why it's trending:
   "People are excited about AI systems that can work autonomously. 
   Multiple new frameworks (Crew AI, AutoGen) launched recently, 
   and companies are experimenting with using them in production."
   
   Sentiment: Very positive (88% of posts are optimistic)
   Momentum: Growing (mentions increased 40% in last 2 weeks)
   Opportunity: "Tool to help companies manage AI agent workflows"
   ```

4. **Product Manager:**
   - [ ] Read through all explanations
   - [ ] Are they clear? Do they make sense?
   - [ ] Flag any that need rewording

**Checkpoint:**
- ✅ All 10-15 trends have explanations
- ✅ Explanations mention WHY people care
- ✅ Each trend has sentiment and momentum data

---

### **Hour 6-7 (3:30-4:30 PM): Build the Dashboard**

**What:** Create the visual interface where someone types a product name and sees the trends  
**Who:** Frontend Dev + Backend Dev (support)  
**What Gets Done:** Working web page that displays all trends nicely

#### Step-by-Step:

1. **Frontend Dev:**
   - [ ] Create a page with:
     - Input box: "Enter product name or topic"
     - "Analyze" button
     - List of top trends displayed with:
       - Trend name (big text)
       - Engagement score (★★★★★)
       - "Why it's trending" (explanation)
       - "Opportunities" (suggested actions)
       - Links to source posts (Reddit, GitHub, etc.)

2. **Example Dashboard Layout:**
   ```
   ╔═══════════════════════════════════════╗
   ║     TrendLens AI                      ║
   ║  Find Emerging Trends                 ║
   ╠═══════════════════════════════════════╣
   ║                                       ║
   ║ Enter topic: [AI Agents    ]          ║
   ║                             [Analyze] ║
   ║                                       ║
   ╠═══════════════════════════════════════╣
   ║                                       ║
   ║ 🔥 Trend 1: AI Agents                 ║
   ║ Score: ★★★★★ (8,542 engagement)       ║
   ║ Why: "Autonomous AI systems gaining.. ║
   ║ Opportunity: Workflow management tool ║
   ║ Evidence: [23 posts] [View sources]   ║
   ║                                       ║
   ║ 🔥 Trend 2: Local AI                  ║
   ║ Score: ★★★★☆ (5,231 engagement)       ║
   ║ Why: "Privacy-focused on-device ML... ║
   ║ Opportunity: Privacy-first framework  ║
   ║ Evidence: [18 posts] [View sources]   ║
   ║                                       ║
   ╚═══════════════════════════════════════╝
   ```

3. **Backend Dev (Support):**
   - [ ] Make sure the API keeps working
   - [ ] Fix any connection issues between dashboard and backend
   - [ ] Test that data loads fast (under 2 seconds)

4. **Product Manager:**
   - [ ] Test the dashboard on multiple computers
   - [ ] Does it look professional?
   - [ ] Can you understand what each trend means?
   - [ ] Make a list of any visual improvements needed

**Checkpoint:**
- ✅ Dashboard loads without errors
- ✅ All trends display with explanations
- ✅ Looks clean and professional
- ✅ Fast loading (under 2 seconds)

---

### **Hour 7-8 (4:30-5:30 PM): Polish & Demo Prep**

**What:** Fix any bugs, make sure everything works perfectly, prepare the presentation  
**Who:** Entire team  
**What Gets Done:** Demo-ready system + presentation ready

#### Step-by-Step:

1. **Backend Dev:**
   - [ ] Run full system end-to-end
   - [ ] Does data collection work?
   - [ ] Does clustering work?
   - [ ] Does API respond correctly?
   - [ ] Fix any errors

2. **Frontend Dev:**
   - [ ] Test on multiple browsers
   - [ ] Check that all buttons work
   - [ ] Make sure no broken links
   - [ ] Test with slow internet (simulate real conditions)

3. **Data Analyst:**
   - [ ] Review final trend quality
   - [ ] Are these legitimate trends or noise?
   - [ ] Should we remove any?
   - [ ] Make final notes

4. **Product Manager:**
   - [ ] Write demo script (what you'll say)
   - [ ] Practice the demo
   - [ ] Time it (should be 2-3 minutes)
   - [ ] Create backup plan if something breaks
   - [ ] Take screenshots for slides

5. **Team (Together):**
   - [ ] Do a final run-through of demo
   - [ ] Someone plays the "judge" and asks questions
   - [ ] Everyone knows what to say
   - [ ] List any improvements for "future versions"

**Demo Script Example:**
```
"Hello! This is TrendLens AI. 

We're solving a problem product managers face: 
How do you know what's trending without spending 
hours researching?

Watch this: I'll search for 'AI' topics...

[Click Analyze]

Within 2 seconds, our system has:
1. Searched Reddit, GitHub, and Hacker News
2. Found 100+ relevant discussions
3. Grouped them into 15 distinct trends
4. Analyzed why each is trending

Here are the top trending topics related to AI:

1. AI Agents - People are excited about autonomous AI 
   systems. Multiple frameworks just launched.

2. Local AI - Developers care about privacy-first, 
   on-device AI that doesn't require cloud.

3. Voice Interfaces - Audio AI is becoming accessible 
   to more developers.

Each trend shows how many people are talking about it 
and links to the actual discussions so you can dig deeper.

This helps product managers stay ahead of the curve 
without manual research."
```

**Checkpoint:**
- ✅ System works end-to-end
- ✅ Demo script written and rehearsed
- ✅ All team members know their talking points
- ✅ Backup plan if system fails

---

## 📊 Work Breakdown Table

| Hour | Activity | Owner | Goal | Status |
|------|----------|-------|------|--------|
| 1 | Setup | DevOps + Backend | Everyone ready to code | ⏳ |
| 2-3 | Data Collection | Backend + Data Analyst | 100+ posts in database | ⏳ |
| 4-5 | Clustering | Data Analyst + Backend | 10-15 trend groups | ⏳ |
| 5-6 | Explanations | Data Analyst + Backend | Why each trend matters | ⏳ |
| 6-7 | Dashboard | Frontend + Backend | Beautiful working UI | ⏳ |
| 7-8 | Polish & Demo | Entire Team | Demo-ready system | ⏳ |

---

## 🚨 What Can Go Wrong (And How to Fix It)

### Problem 1: "Data collection is taking too long"
**Solution:** Use sample/cached data from test sources instead of live Reddit

### Problem 2: "Clustering is grouping things wrong"
**Solution:** Use simpler method (just keyword matching) instead of fancy AI

### Problem 3: "Dashboard is not connecting to backend"
**Solution:** Backend developer helps frontend developer debug the connection

### Problem 4: "Everything is broken at hour 6"
**Solution:** Show just the raw data list instead of fancy visualization - still counts as working demo

### Problem 5: "We didn't finish everything"
**Solution:** Demo what IS working, narrate what WOULD happen next

---

## ✅ Success Checklist

By end of Day 2, you should have:

- [ ] A working website/dashboard
- [ ] It collects real data from Reddit, GitHub, or Hacker News
- [ ] It groups similar topics together  
- [ ] It shows top 10 trends with explanations
- [ ] It loads in under 5 seconds
- [ ] No major errors or crashes during demo
- [ ] Team can explain what each trend means
- [ ] Demo script is written and practiced
- [ ] Everyone knows their role during presentation

---

## 🎬 During Demo (What to Show Judges)

1. **Show the problem:** "Product managers spend hours researching trends..."
2. **Show the input:** "We just type a topic..."
3. **Show the process:** "System searches Reddit, GitHub, Hacker News..."
4. **Show the output:** "Here are the top 15 trending topics with why they matter"
5. **Show the opportunity:** "This saves product managers 5+ hours of research per week"
6. **Show the tech:** Briefly explain: AI + clustering + data sources + dashboard
7. **Ask for feedback:** "What would you add? What's most valuable?"

---

## 🎉 If You Finish Early

**Nice-to-haves to add:**
- [ ] Add a "sources" view showing original posts
- [ ] Add sorting/filtering by engagement, sentiment, or date
- [ ] Add charts showing trend growth over time
- [ ] Add competitor analysis ("What are others in the space talking about?")
- [ ] Add a "save" feature to bookmark trends

---

## 📞 Questions to Ask Throughout Day

**Hour 1:** Is everyone able to see the code running on their computer?

**Hour 3:** Do the 100 posts make sense? Are they relevant?

**Hour 5:** Does the grouping look right? Would a product manager understand?

**Hour 6:** Is the dashboard clear? Would someone know how to use it without help?

**Hour 7:** Can you demo this without any crashes? Does it tell a good story?

---

## 🏁 Final Note

You don't need to build Google or Facebook-level infrastructure. You just need to show that the idea works and is valuable. A simple, working MVP impresses judges more than a broken, fancy system.

**Focus on:** Making judges say "Oh, I get it" and "That's actually useful"

**Don't focus on:** Making it pretty, adding every feature, or being perfect

**Good luck! 🚀**
