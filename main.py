"""
FastAPI Backend for OrchestrAI Labs
This is your API deployment requirement
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from orchestrator import OrchestratorAgent
from database import init_db
from typing import Optional

# Initialize FastAPI app
app = FastAPI(
    title="OrchestrAI Labs API",
    description="Multi-Agent AI System for Task and Schedule Management",
    version="1.0.0"
)

# Initialize database
init_db()

# Initialize orchestrator
orchestrator = OrchestratorAgent()

# Request models
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""

class MeetingCreate(BaseModel):
    title: str
    date: str
    time: Optional[str] = ""
    description: Optional[str] = ""

class ChatRequest(BaseModel):
    message: str

# API Endpoints
@app.get("/")
def root():
    """Health check endpoint"""
    return {
        "status": "running",
        "service": "OrchestrAI Labs",
        "version": "1.0.0",
        "agents": ["Orchestrator", "Task Agent", "Calendar Agent"]
    }

@app.post("/chat")
def chat(request: ChatRequest):
    """
    Natural language interface
    This shows multi-agent coordination
    """
    try:
        result = orchestrator.process_request(request.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tasks")
def create_task(task: TaskCreate):
    """Create a new task"""
    try:
        result = orchestrator.create_task(task.title, task.description)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks")
def get_tasks():
    """Get all tasks"""
    try:
        result = orchestrator.get_tasks()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/meetings")
def create_meeting(meeting: MeetingCreate):
    """Schedule a new meeting"""
    try:
        result = orchestrator.schedule_meeting(
            meeting.title,
            meeting.date,
            meeting.time,
            meeting.description
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/meetings")
def get_meetings():
    """Get all meetings"""
    try:
        result = orchestrator.get_meetings()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the server
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting OrchestrAI Labs API...")
    print("📍 API will be available at: http://localhost:8000")
    print("📚 API docs at: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
