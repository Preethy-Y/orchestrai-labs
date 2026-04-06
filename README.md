# 🚀 OrchestrAI Labs - Multi-Agent AI System

**Hackathon Project**: Gen AI Academy APAC Edition  
**Team**: Preethy's Team  
**Deadline**: April 8, 11:59 PM IST

## 🎯 What This Project Does

A **Multi-Agent AI System** that helps users manage tasks and schedules using:
- 🧠 **Primary Agent**: Orchestrator (main brain)
- 🤖 **Sub-Agent 1**: Task Agent (manages tasks)
- 🤖 **Sub-Agent 2**: Calendar Agent (manages meetings)
- 💾 **Database**: SQLite (stores everything)
- 🛠️ **Tools**: Task tools + Calendar tools

## ✅ Hackathon Requirements Met

- [x] Primary Agent (Orchestrator)
- [x] Multiple Sub-Agents (Task + Calendar)
- [x] Database Integration (SQLite)
- [x] MCP Tools (Task tools + Calendar tools)
- [x] Multi-Step Workflows
- [x] API Deployment (FastAPI)
- [x] Working Demo (Gradio UI)

## 🏗️ System Architecture

```
User Input
    ↓
Orchestrator Agent (Primary)
    ↓
├── Task Agent (Sub-Agent 1)
└── Calendar Agent (Sub-Agent 2)
    ↓
SQLite Database
    ↓
Response
```

## 📁 Project Structure

```
OrchestrAI/
├── requirements.txt      # Python packages
├── database.py          # Database setup
├── task_agent.py        # Task Agent
├── calendar_agent.py    # Calendar Agent
├── orchestrator.py      # Orchestrator Agent
├── main.py             # FastAPI backend
├── ui.py               # Gradio UI
└── README.md           # This file
```

## 🚀 Quick Start Guide (For Beginners)

### Step 1: Install Dependencies

Open Command Prompt in your OrchestrAI folder and run:

```bash
pip install -r requirements.txt
```

Wait for installation (2-3 minutes)

### Step 2: Test the System

**Option A: Run UI (Recommended for Demo)**

```bash
python ui.py
```

- Opens browser automatically
- Use the chat or tabs to test features
- Perfect for judges demo!

**Option B: Run API**

```bash
python main.py
```

- API runs at: http://localhost:8000
- API docs at: http://localhost:8000/docs
- Use Postman or curl to test

### Step 3: Test Multi-Agent Workflows

Try these in the chat:

1. **Simple Task**: "Create task to finish hackathon"
2. **Simple Meeting**: "Schedule meeting tomorrow"
3. **Multi-Step** (Impressive!): "Schedule meeting tomorrow and create reminder"

## 🎬 Demo Scenarios for Judges

### Scenario 1: Single Agent Action
**User**: "Create task: Prepare presentation"  
**System**: Orchestrator → Task Agent → Database → ✅ Task created

### Scenario 2: Another Single Agent
**User**: "Schedule meeting on April 8"  
**System**: Orchestrator → Calendar Agent → Database → ✅ Meeting scheduled

### Scenario 3: Multi-Agent Workflow (🔥 Impressive!)
**User**: "Schedule meeting tomorrow and create reminder"  
**System**:
1. Orchestrator receives request
2. Calls Calendar Agent → schedules meeting
3. Calls Task Agent → creates reminder task
4. Returns combined result

**This demonstrates true multi-agent coordination!**

## 🛠️ Tech Stack

- **Language**: Python 3.12+
- **Backend**: FastAPI
- **Database**: SQLite
- **UI**: Gradio
- **Agents**: Custom Multi-Agent System

## 📊 Features Implemented

### Core Features
- ✅ Create tasks
- ✅ View tasks
- ✅ Schedule meetings
- ✅ View meetings
- ✅ Multi-step workflows
- ✅ Natural language chat

### Advanced Features (Bonus Points!)
- ✅ RESTful API
- ✅ Interactive UI
- ✅ Database persistence
- ✅ Multi-agent coordination
- ✅ Architecture documentation

## 🎯 How to Present to Judges

### 1. Show the Problem (30 seconds)
"Managing tasks and schedules is hard. We built a multi-agent AI system to help."

### 2. Show the Architecture (1 minute)
"We have 3 agents working together:
- Orchestrator (decides what to do)
- Task Agent (manages tasks)
- Calendar Agent (manages meetings)"

### 3. Live Demo (2 minutes)
1. Open UI
2. Show simple task creation
3. Show simple meeting scheduling
4. **Show multi-step workflow** (most important!)

### 4. Show the Code (1 minute)
"Here's how agents communicate..." (show orchestrator.py briefly)

### 5. Mention Tech Stack (30 seconds)
"Python, FastAPI, SQLite, Gradio - all industry-standard tools"

## 🏆 Why This Wins Swags

✅ **Working Demo** - Not just slides  
✅ **Multi-Agent** - Clear coordination between agents  
✅ **Clean Code** - Easy to understand  
✅ **Good UI** - Professional Gradio interface  
✅ **Meets All Requirements** - Check all boxes  

## 📝 Submission Checklist

Before submitting:

- [ ] Test all features work
- [ ] Record demo video (3-5 minutes)
- [ ] Take screenshots of UI
- [ ] Prepare architecture diagram
- [ ] Write submission description
- [ ] Upload to GitHub (optional but recommended)
- [ ] Submit before deadline!

## 🚨 Troubleshooting

**Problem**: `pip install` fails  
**Solution**: Run as administrator or use `pip install --user -r requirements.txt`

**Problem**: Port already in use  
**Solution**: Change port in ui.py: `demo.launch(server_port=7861)`

**Problem**: Database error  
**Solution**: Delete `orchestrai.db` file and restart

## 📞 Need Help?

If something doesn't work:
1. Check if Python is installed: `python --version`
2. Check if packages installed: `pip list`
3. Read error messages carefully
4. Ask for help!

## 🎉 Good Luck!

You have everything you need to win swags! 🏆

Remember:
- Start testing TODAY
- Practice your demo
- Stay calm during presentation
- You've got this! 🚀
