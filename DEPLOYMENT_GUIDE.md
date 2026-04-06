# ☁️ Google Cloud Run Deployment Guide

## Prerequisites Checklist

- [ ] Google Cloud account (free tier available)
- [ ] Project running locally
- [ ] GitHub repository created
- [ ] Credit card (for verification - won't be charged on free tier)

---

## Part 1: Google Cloud Setup (15 minutes)

### Step 1: Create Google Cloud Account

1. **Go to:** https://cloud.google.com/
2. **Click:** "Get started for free"
3. **Sign in** with your Google account
4. **Fill in** billing information (you get $300 free credits!)
5. **Complete** verification

**Note:** You won't be charged during free trial!

---

### Step 2: Create a New Project

1. **Go to:** https://console.cloud.google.com/
2. **Click** the project dropdown (top left, next to "Google Cloud")
3. **Click:** "New Project"
4. **Enter:**
   - Project name: `orchestrai-labs`
   - Project ID: `orchestrai-labs-[random-numbers]` (will be auto-generated)
5. **Click:** "Create"
6. **Wait** for project creation (30 seconds)
7. **Select** your new project from the dropdown

---

### Step 3: Enable Required APIs

1. **Go to:** https://console.cloud.google.com/apis/library
2. **Search and enable** these APIs (click "Enable" for each):
   - Cloud Run API
   - Cloud Build API
   - Artifact Registry API

**Each API:**
- Search for it
- Click on it
- Click "Enable"
- Wait for confirmation

---

### Step 4: Install Google Cloud CLI (Command Line Tool)

**For Windows:**

1. **Download:** https://cloud.google.com/sdk/docs/install
2. **Click:** "Windows" tab
3. **Download** the installer
4. **Run** the installer
5. **Follow** installation wizard (use default settings)
6. **Finish** installation

**Verify Installation:**

Open Command Prompt (cmd) and type:
```bash
gcloud --version
```

You should see version info!

---

### Step 5: Authenticate and Configure

In Command Prompt:

```bash
# Login to Google Cloud
gcloud auth login
```

**This will:**
- Open browser
- Ask you to sign in
- Ask for permissions
- Confirm success

```bash
# Set your project
gcloud config set project orchestrai-labs-[YOUR-PROJECT-ID]
```

**Replace `[YOUR-PROJECT-ID]` with your actual project ID from Step 2!**

```bash
# Configure default region (choose closest to you)
gcloud config set run/region asia-south1
```

**Asia-South1 = Mumbai, India** (closest to you!)

Other options:
- `asia-southeast1` = Singapore
- `asia-east1` = Taiwan

---

## Part 2: Prepare Your Code (10 minutes)

### Step 1: Update main.py for Cloud Run

Your `main.py` needs a small change to work with Cloud Run.

**Current last line:**
```python
uvicorn.run(app, host="0.0.0.0", port=8000)
```

**Change to:**
```python
import os
port = int(os.environ.get("PORT", 8080))
uvicorn.run(app, host="0.0.0.0", port=port)
```

**Why?** Cloud Run assigns a random port via environment variable.

---

### Step 2: Verify Files

Make sure you have these files in your project folder:

```
OrchestrAI_Complete/
├── database.py           ✅
├── task_agent.py         ✅
├── calendar_agent.py     ✅
├── orchestrator.py       ✅
├── main.py              ✅ (updated for Cloud Run)
├── requirements.txt      ✅
├── Dockerfile           ✅ (I created this for you)
└── .dockerignore        ✅ (I created this for you)
```

All ✅ means you're ready!

---

## Part 3: Deploy to Cloud Run (15 minutes)

### Method 1: Direct Deployment (Easiest)

Open Command Prompt in your project folder:

```bash
# Navigate to your project
cd Desktop\OrchestrAI_Complete

# Deploy to Cloud Run (this does EVERYTHING automatically!)
gcloud run deploy orchestrai \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --platform managed
```

**What happens:**
1. ✅ Code is uploaded
2. ✅ Container is built automatically
3. ✅ App is deployed
4. ✅ Public URL is generated

**This takes 3-5 minutes!**

Watch the progress. You'll see:
```
Building using Dockerfile...
✓ Creating Container
✓ Uploading package
✓ Building image
✓ Deploying
Done.
Service [orchestrai] revision [orchestrai-00001-abc] has been deployed
Service URL: https://orchestrai-[random]-as.a.run.app
```

**COPY THAT URL!** That's your submission link! 🎉

---

### Method 2: Manual Docker Build (Alternative)

If Method 1 doesn't work:

```bash
# 1. Build the container
gcloud builds submit --tag gcr.io/orchestrai-labs/orchestrai

# 2. Deploy the container
gcloud run deploy orchestrai \
  --image gcr.io/orchestrai-labs/orchestrai \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated
```

---

## Part 4: Test Your Deployment (5 minutes)

### Test 1: Check the URL

Visit your deployed URL:
```
https://orchestrai-[random]-as.a.run.app
```

You should see:
```json
{
  "status": "running",
  "service": "OrchestrAI Labs",
  "version": "1.0.0",
  "agents": ["Orchestrator", "Task Agent", "Calendar Agent"]
}
```

**✅ IT WORKS!**

---

### Test 2: Test API Endpoints

**Test creating a task:**
```bash
curl -X POST "https://orchestrai-[YOUR-URL].a.run.app/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test from Cloud", "description": "It works!"}'
```

**Test the chat endpoint:**
```bash
curl -X POST "https://orchestrai-[YOUR-URL].a.run.app/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Create task to celebrate deployment"}'
```

**View API docs:**

Go to: `https://orchestrai-[YOUR-URL].a.run.app/docs`

You'll see the full API documentation!

---

### Test 3: Check Logs

In Google Cloud Console:

1. Go to: https://console.cloud.google.com/run
2. Click on "orchestrai" service
3. Click "LOGS" tab
4. See all requests and responses

---

## Part 5: Get Your Submission URL (1 minute)

Your deployment URL format:
```
https://orchestrai-[random-string]-as.a.run.app
```

**Example:**
```
https://orchestrai-abc123xyz-as.a.run.app
```

**This is what you submit in the "Cloud Run Deployment Link" field!**

---

## Troubleshooting

### Problem 1: "Permission denied"

**Solution:**
```bash
gcloud auth login
gcloud config set project orchestrai-labs-[YOUR-ID]
```

### Problem 2: "APIs not enabled"

**Solution:**
Go to each API and click "Enable":
- Cloud Run API
- Cloud Build API
- Artifact Registry API

### Problem 3: "Build failed"

**Solution:**
Check your Dockerfile. Make sure it's exactly as I provided.

### Problem 4: "Service returns 500 error"

**Solution:**
```bash
# Check logs
gcloud run services logs read orchestrai --region asia-south1

# Common issue: database initialization
# Make sure main.py calls init_db()
```

### Problem 5: "Cannot connect to database"

**Solution:**
SQLite doesn't persist on Cloud Run restarts (this is OK for demo!).
Every restart creates a fresh database.

For production, you'd use Cloud SQL, but for hackathon demo, this is fine!

---

## Cost Estimate

**Good News:** Cloud Run Free Tier includes:

- ✅ 2 million requests per month
- ✅ 360,000 GB-seconds of memory
- ✅ 180,000 vCPU-seconds

**Your hackathon usage:** Basically FREE! 🎉

Even after free trial, your demo will cost less than $0.50/month!

---

## Alternative: Quick Deploy Button

If command line is intimidating, use this:

1. **Push to GitHub** first
2. **Go to:** https://console.cloud.google.com/run
3. **Click:** "Create Service"
4. **Choose:** "Continuously deploy from a repository"
5. **Connect** your GitHub
6. **Select** your repository
7. **Click** "Deploy"

Cloud Run will auto-deploy whenever you push to GitHub!

---

## Deployment Checklist

- [ ] Google Cloud account created
- [ ] Project created (`orchestrai-labs`)
- [ ] APIs enabled (Cloud Run, Cloud Build, Artifact Registry)
- [ ] gcloud CLI installed
- [ ] Authenticated (`gcloud auth login`)
- [ ] Project configured
- [ ] main.py updated for Cloud Run
- [ ] All files present (including Dockerfile)
- [ ] Deployed using `gcloud run deploy`
- [ ] Received deployment URL
- [ ] Tested URL in browser
- [ ] Tested API endpoints
- [ ] URL saved for submission

---

## Getting Help

**gcloud documentation:**
https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service

**Cloud Run console:**
https://console.cloud.google.com/run

**If stuck:**
1. Check error message carefully
2. Google the exact error
3. Check Cloud Run logs
4. Ask me for help!

---

## After Deployment

**Update your README** with the deployment URL:
```markdown
## 🌐 Live Demo

**Deployed on Google Cloud Run:**
https://orchestrai-[your-url].a.run.app

**API Documentation:**
https://orchestrai-[your-url].a.run.app/docs
```

---

## Time Breakdown

- Google Cloud setup: 15 minutes
- Code preparation: 10 minutes
- Actual deployment: 5 minutes
- Testing: 5 minutes

**Total: ~35 minutes** from start to deployed URL! 🚀

---

**Ready to deploy? Start with Part 1: Google Cloud Setup!**
