"""
Database setup for OrchestrAI Labs
Stores tasks and meetings
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Task(Base):
    """Task model"""
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)

class Meeting(Base):
    """Meeting model"""
    __tablename__ = 'meetings'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date = Column(String, nullable=False)
    time = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Database setup
engine = create_engine('sqlite:///orchestrai.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Initialize database"""
    Base.metadata.create_all(engine)
    print("✅ Database initialized!")

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
