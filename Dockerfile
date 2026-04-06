# Use official Python runtime as base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY database.py .
COPY task_agent.py .
COPY calendar_agent.py .
COPY orchestrator.py .
COPY main.py .

# Expose port
EXPOSE 8080

# Set environment variable for port
ENV PORT=8080

# Initialize database on startup and run the application
CMD python -c "from database import init_db; init_db()" && \
    uvicorn main:app --host 0.0.0.0 --port $PORT
