# 💻 GitHub Repository Setup Guide

## Part 1: Create GitHub Account (5 minutes)

### If You Don't Have a GitHub Account

1. **Go to:** https://github.com
2. **Click:** "Sign up"
3. **Enter:**
   - Email address
   - Password
   - Username (choose something professional like: `yourname-dev`)
4. **Verify** your email
5. **Complete** the welcome survey (optional)

### If You Already Have GitHub

1. **Go to:** https://github.com
2. **Sign in**
3. Ready to go! ✅

---

## Part 2: Create Repository (5 minutes)

### Step 1: Create New Repository

1. **Go to:** https://github.com/new
   (Or click the "+" icon → "New repository")

2. **Fill in details:**
   - **Repository name:** `orchestrai-labs`
   - **Description:** "Multi-Agent AI System for Task & Schedule Management - Gen AI Academy APAC Hackathon"
   - **Visibility:** ✅ **Public** (required for hackathon!)
   - **Initialize repository:**
     - ☐ Do NOT check "Add a README file"
     - ☐ Do NOT add .gitignore
     - ☐ Do NOT choose a license

3. **Click:** "Create repository"

---

### Step 2: Save Repository URLs

After creation, you'll see your repository page with these URLs:

**HTTPS URL** (you'll need this):
```
https://github.com/[your-username]/orchestrai-labs.git
```

**Repository Page** (for submission):
```
https://github.com/[your-username]/orchestrai-labs
```

**SAVE BOTH OF THESE!**

---

## Part 3: Install Git on Windows (10 minutes)

### Step 1: Download Git

1. **Go to:** https://git-scm.com/download/win
2. **Download** starts automatically
3. **Run** the installer (Git-2.44.0-64-bit.exe or similar)

### Step 2: Install Git

During installation:

- **Select Components:** Use defaults ✅
- **Default editor:** Select "Use Visual Studio Code" or "Nano" (easier than Vim)
- **Adjusting PATH:** Select "Git from the command line and also from 3rd-party software" ✅
- **HTTPS backend:** Use "Use the OpenSSL library" ✅
- **Line ending conversions:** Use "Checkout Windows-style, commit Unix-style line endings" ✅
- **Terminal emulator:** Use "Use MinTTY" ✅
- **Everything else:** Keep defaults

**Click "Install"**

### Step 3: Verify Installation

Open **new** Command Prompt (important - new window!):

```bash
git --version
```

You should see:
```
git version 2.44.0.windows.1
```

✅ Git is installed!

---

## Part 4: Upload Your Code (10 minutes)

### Step 1: Configure Git (First Time Only)

Open Command Prompt:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Use the same email as your GitHub account!**

---

### Step 2: Navigate to Your Project

```bash
cd Desktop\OrchestrAI_Complete
```

---

### Step 3: Initialize Git Repository

```bash
# Initialize git in your folder
git init
```

You'll see:
```
Initialized empty Git repository in C:/Users/YourName/Desktop/OrchestrAI_Complete/.git/
```

---

### Step 4: Add All Files

```bash
# Add all files to staging
git add .
```

Check what's added:
```bash
git status
```

You should see a list of green files ready to commit!

---

### Step 5: Create First Commit

```bash
git commit -m "Initial commit: OrchestrAI Labs multi-agent system"
```

You'll see:
```
[master (root-commit) abc1234] Initial commit: OrchestrAI Labs multi-agent system
 9 files changed, 500 insertions(+)
```

---

### Step 6: Connect to GitHub

```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/[YOUR-USERNAME]/orchestrai-labs.git
```

**Replace `[YOUR-USERNAME]` with your actual GitHub username!**

Example:
```bash
git remote add origin https://github.com/preethy123/orchestrai-labs.git
```

---

### Step 7: Push to GitHub

```bash
# Push your code to GitHub
git branch -M main
git push -u origin main
```

**You'll be asked for credentials:**

**IMPORTANT:** You cannot use your password anymore! You need a **Personal Access Token**.

---

### Step 8: Create Personal Access Token (PAT)

**If git asks for credentials:**

1. **Go to:** https://github.com/settings/tokens
2. **Click:** "Generate new token" → "Generate new token (classic)"
3. **Note:** "Hackathon submission token"
4. **Expiration:** Choose "30 days"
5. **Select scopes:**
   - ✅ `repo` (full control of private repositories)
6. **Click:** "Generate token"
7. **COPY THE TOKEN IMMEDIATELY** (you won't see it again!)

**Use this as your password when git asks!**

**Username:** your-github-username  
**Password:** ghp_xxxxxxxxxxxxxxxxxxxx (your token)

---

### Step 9: Verify Upload

**Go to your repository page:**
```
https://github.com/[your-username]/orchestrai-labs
```

You should see all your files! 🎉

Files should include:
- calendar_agent.py
- database.py
- main.py
- orchestrator.py
- task_agent.py
- test.py
- ui.py
- requirements.txt
- Dockerfile
- .gitignore
- README.md

---

## Part 5: Update README (5 minutes)

### Step 1: Edit README on GitHub

1. **Go to** your repository page
2. **Click** on "README.md"
3. **Click** the pencil icon (Edit)
4. **Replace** `[Your Team Name]`, `[Your Names]`, etc. with actual info
5. **Add** your Cloud Run URL when you have it
6. **Click** "Commit changes"

---

### Step 2: Add Topics (Tags)

On your repository page:

1. **Click** the gear icon next to "About"
2. **Add topics:**
   - `ai`
   - `multi-agent`
   - `hackathon`
   - `google-cloud`
   - `fastapi`
   - `python`
3. **Click** "Save changes"

This makes your repo more discoverable!

---

## Part 6: Make Repository Look Professional (10 minutes)

### Add a License

1. **Click** "Add file" → "Create new file"
2. **Name:** `LICENSE`
3. **Click** "Choose a license template"
4. **Select:** "MIT License"
5. **Click** "Review and submit"
6. **Commit** the file

### Add Repository Description

1. **Click** gear icon next to "About"
2. **Description:** "Multi-Agent AI System for Task & Schedule Management"
3. **Website:** (Your Cloud Run URL when ready)
4. **Topics:** (Already added)
5. **Save**

---

## Part 7: Test Your Repository Link (2 minutes)

### Verification Checklist

1. **Open incognito/private browser window**
2. **Go to:** `https://github.com/[your-username]/orchestrai-labs`
3. **Check:**
   - [ ] Repository loads without login
   - [ ] All files are visible
   - [ ] README displays correctly
   - [ ] Code is readable
   - [ ] No private/sensitive data visible

**If all ✅, your link is ready for submission!**

---

## Part 8: Future Updates (After Initial Upload)

If you make changes to your code:

```bash
# Navigate to project folder
cd Desktop\OrchestrAI_Complete

# Add changes
git add .

# Commit with message
git commit -m "Updated feature X"

# Push to GitHub
git push
```

Your GitHub repository will auto-update! ✅

---

## Troubleshooting

### Problem 1: "Permission denied"

**Solution:** Check your Personal Access Token
```bash
# Reset credentials
git config --global credential.helper wincred
# Try pushing again - will ask for credentials
```

### Problem 2: "Repository not found"

**Solution:** Check the remote URL
```bash
# See current remote
git remote -v

# If wrong, remove and re-add
git remote remove origin
git remote add origin https://github.com/[CORRECT-USERNAME]/orchestrai-labs.git
```

### Problem 3: "Fatal: not a git repository"

**Solution:** You're not in the right folder
```bash
cd Desktop\OrchestrAI_Complete
git init
```

### Problem 4: Forgot to add a file

**Solution:**
```bash
# Add the missing file
git add filename.py

# Commit
git commit -m "Added missing file"

# Push
git push
```

### Problem 5: "Authentication failed"

**Solution:** Generate a new Personal Access Token and use it as password

---

## GitHub Desktop (Alternative Easy Method)

If command line is too hard:

### Download GitHub Desktop

1. **Go to:** https://desktop.github.com/
2. **Download** GitHub Desktop
3. **Install** it
4. **Sign in** with your GitHub account

### Upload Your Project

1. **Click** "File" → "Add local repository"
2. **Choose** your project folder
3. **Click** "Create repository"
4. **Click** "Publish repository"
5. **Make sure** "Keep this code private" is **UNCHECKED**
6. **Click** "Publish repository"

Done! Much easier! ✅

---

## GitHub Repository Checklist

- [ ] GitHub account created
- [ ] Repository created (public)
- [ ] Git installed on Windows
- [ ] Git configured (name and email)
- [ ] Code uploaded to GitHub
- [ ] README updated with team info
- [ ] License added (MIT)
- [ ] Repository description added
- [ ] Topics/tags added
- [ ] Tested link in incognito mode
- [ ] All files visible
- [ ] Repository link saved for submission

---

## Your Submission Link Format

```
https://github.com/[your-username]/orchestrai-labs
```

**Example:**
```
https://github.com/preethy123/orchestrai-labs
```

**This is what goes in "GitHub Repository Link" field!**

---

## Making Your README Awesome

After uploading, edit README.md to add:

- Screenshots of your UI
- Architecture diagram
- Demo GIF (optional but impressive!)
- Badges (the colorful status icons at top)

**Example badges:**
```markdown
![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
```

---

## Time Estimate

- Create account: 5 minutes
- Create repository: 5 minutes
- Install Git: 10 minutes
- Upload code: 10 minutes
- Polish repository: 10 minutes

**Total: ~40 minutes**

---

**Ready? Start with Part 1: Create GitHub Account!**
