"""
Task Agent - Manages all task-related operations
This is one of your sub-agents
"""

from database import Task, SessionLocal
from datetime import datetime

class TaskAgent:
    """Agent responsible for task management"""
    
    def __init__(self):
        self.name = "Task Agent"
        self.db = SessionLocal()
    
    def create_task(self, title: str, description: str = "") -> dict:
        """Create a new task"""
        try:
            task = Task(
                title=title,
                description=description,
                created_at=datetime.utcnow()
            )
            self.db.add(task)
            self.db.commit()
            
            return {
                "status": "success",
                "message": f"✅ Task created: {title}",
                "task_id": task.id
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Failed to create task: {str(e)}"
            }
    
    def get_all_tasks(self) -> dict:
        """Get all tasks"""
        try:
            tasks = self.db.query(Task).all()
            task_list = [
                {
                    "id": task.id,
                    "title": task.title,
                    "description": task.description,
                    "completed": task.completed
                }
                for task in tasks
            ]
            
            return {
                "status": "success",
                "tasks": task_list,
                "count": len(task_list)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Failed to get tasks: {str(e)}"
            }
    
    def complete_task(self, task_id: int) -> dict:
        """Mark task as completed"""
        try:
            task = self.db.query(Task).filter(Task.id == task_id).first()
            if task:
                task.completed = True
                self.db.commit()
                return {
                    "status": "success",
                    "message": f"✅ Task {task_id} marked as completed"
                }
            else:
                return {
                    "status": "error",
                    "message": f"❌ Task {task_id} not found"
                }
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Failed to complete task: {str(e)}"
            }
    
    def delete_task(self, task_id: int) -> dict:
        """Delete a task"""
        try:
            task = self.db.query(Task).filter(Task.id == task_id).first()
            if task:
                self.db.delete(task)
                self.db.commit()
                return {
                    "status": "success",
                    "message": f"✅ Task {task_id} deleted"
                }
            else:
                return {
                    "status": "error",
                    "message": f"❌ Task {task_id} not found"
                }
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Failed to delete task: {str(e)}"
            }
