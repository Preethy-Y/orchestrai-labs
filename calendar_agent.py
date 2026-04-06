"""
Calendar Agent - Manages all calendar and meeting operations
This is your second sub-agent
"""

from database import Meeting, SessionLocal
from datetime import datetime

class CalendarAgent:
    """Agent responsible for calendar management"""
    
    def __init__(self):
        self.name = "Calendar Agent"
        self.db = SessionLocal()
    
    def schedule_meeting(self, title: str, date: str, time: str = "", description: str = "") -> dict:
        """Schedule a new meeting"""
        try:
            meeting = Meeting(
                title=title,
                date=date,
                time=time,
                description=description,
                created_at=datetime.utcnow()
            )
            self.db.add(meeting)
            self.db.commit()
            
            return {
                "status": "success",
                "message": f"✅ Meeting scheduled: {title} on {date}",
                "meeting_id": meeting.id
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Failed to schedule meeting: {str(e)}"
            }
    
    def get_all_meetings(self) -> dict:
        """Get all meetings"""
        try:
            meetings = self.db.query(Meeting).all()
            meeting_list = [
                {
                    "id": meeting.id,
                    "title": meeting.title,
                    "date": meeting.date,
                    "time": meeting.time,
                    "description": meeting.description
                }
                for meeting in meetings
            ]
            
            return {
                "status": "success",
                "meetings": meeting_list,
                "count": len(meeting_list)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Failed to get meetings: {str(e)}"
            }
    
    def cancel_meeting(self, meeting_id: int) -> dict:
        """Cancel a meeting"""
        try:
            meeting = self.db.query(Meeting).filter(Meeting.id == meeting_id).first()
            if meeting:
                self.db.delete(meeting)
                self.db.commit()
                return {
                    "status": "success",
                    "message": f"✅ Meeting {meeting_id} cancelled"
                }
            else:
                return {
                    "status": "error",
                    "message": f"❌ Meeting {meeting_id} not found"
                }
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Failed to cancel meeting: {str(e)}"
            }
