# 🚀 OrchestrAI Labs - Multi-Agent AI System

**Hackathon Project**: Gen AI Academy APAC Edition  
**Team**: Preethy's Team  


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



### Scenario 1: Single Agent Action
**User**: "Create task: Prepare presentation"  
**System**: Orchestrator → Task Agent → Database → ✅ Task created

### Scenario 2: Another Single Agent
**User**: "Schedule meeting on April 8"  
**System**: Orchestrator → Calendar Agent → Database → ✅ Meeting scheduled

### Scenario 3: Multi-Agent Workflow
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


