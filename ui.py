"""
Gradio UI for OrchestrAI Labs
Simple and impressive interface
"""

import gradio as gr
from orchestrator import OrchestratorAgent
from database import init_db

# Initialize database
init_db()

# Initialize orchestrator
orchestrator = OrchestratorAgent()

def chat_interface(message, history):
    result = orchestrator.process_request(message)
    if result.get("status") == "success":
        response = result.get("message", "Done!")
        if "steps" in result:
            response += "\n\n🔄 Multi-Step Workflow:"
            for i, step in enumerate(result["steps"], 1):
                response += f"\n  Step {i}: {step.get('message', 'Completed')}"
    else:
        response = result.get("message", "Something went wrong")
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response})
    return "", history

def create_task_ui(title, description):
    result = orchestrator.create_task(title, description)
    return result.get("message", "Task created!")

def show_tasks_ui():
    result = orchestrator.get_tasks()
    if result.get("status") == "success":
        tasks = result.get("tasks", [])
        if not tasks:
            return "No tasks yet!"
        task_text = f"📋 Total Tasks: {len(tasks)}\n\n"
        for task in tasks:
            status = "✅" if task.get("completed") else "⏳"
            task_text += f"{status} {task['title']}\n"
            if task.get("description"):
                task_text += f"   {task['description']}\n"
        return task_text
    return "Error fetching tasks"

def schedule_meeting_ui(title, date, time):
    result = orchestrator.schedule_meeting(title, date, time)
    return result.get("message", "Meeting scheduled!")

def show_meetings_ui():
    result = orchestrator.get_meetings()
    if result.get("status") == "success":
        meetings = result.get("meetings", [])
        if not meetings:
            return "No meetings scheduled!"
        meeting_text = f"📅 Total Meetings: {len(meetings)}\n\n"
        for meeting in meetings:
            meeting_text += f"🗓️ {meeting['title']}\n"
            meeting_text += f"   Date: {meeting['date']}"
            if meeting.get('time'):
                meeting_text += f" at {meeting['time']}"
            meeting_text += "\n"
        return meeting_text
    return "Error fetching meetings"

# Create Gradio interface
with gr.Blocks(title="OrchestrAI Labs") as demo:
    gr.Markdown(
        """
        # 🤖 OrchestrAI Labs
        ### Multi-Agent AI System for Task & Schedule Management
        **Powered by**: Orchestrator Agent → Task Agent & Calendar Agent
        """
    )

    with gr.Tabs():
        with gr.Tab("💬 Chat with AI"):
            gr.Markdown("**Try**: 'Create task to finish hackathon' or 'Schedule meeting tomorrow and create reminder'")
            chatbot = gr.Chatbot(height=400)
            msg = gr.Textbox(placeholder="Type your message here...", label="Your Message")
            clear = gr.Button("Clear")
            msg.submit(chat_interface, [msg, chatbot], [msg, chatbot])
            clear.click(lambda: ([], []), None, [msg, chatbot], queue=False)

        with gr.Tab("📋 Tasks"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Create New Task")
                    task_title = gr.Textbox(label="Task Title", placeholder="e.g., Finish hackathon project")
                    task_desc = gr.Textbox(label="Description (optional)", placeholder="Additional details...")
                    create_task_btn = gr.Button("Create Task", variant="primary")
                    task_output = gr.Textbox(label="Result", interactive=False)
                with gr.Column():
                    gr.Markdown("### Your Tasks")
                    show_tasks_btn = gr.Button("Show All Tasks")
                    tasks_display = gr.Textbox(label="Tasks", interactive=False, lines=10)
            create_task_btn.click(create_task_ui, [task_title, task_desc], task_output)
            show_tasks_btn.click(show_tasks_ui, None, tasks_display)

        with gr.Tab("📅 Meetings"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Schedule Meeting")
                    meeting_title = gr.Textbox(label="Meeting Title", placeholder="e.g., Team Standup")
                    meeting_date = gr.Textbox(label="Date", placeholder="e.g., tomorrow, April 5")
                    meeting_time = gr.Textbox(label="Time (optional)", placeholder="e.g., 3:00 PM")
                    schedule_btn = gr.Button("Schedule Meeting", variant="primary")
                    meeting_output = gr.Textbox(label="Result", interactive=False)
                with gr.Column():
                    gr.Markdown("### Your Calendar")
                    show_meetings_btn = gr.Button("Show All Meetings")
                    meetings_display = gr.Textbox(label="Meetings", interactive=False, lines=10)
            schedule_btn.click(schedule_meeting_ui, [meeting_title, meeting_date, meeting_time], meeting_output)
            show_meetings_btn.click(show_meetings_ui, None, meetings_display)

        with gr.Tab("🏗️ System Architecture"):
            gr.Markdown(
                """
                ## Multi-Agent System Architecture

                ```
                User Input
                    ↓
                🧠 Orchestrator Agent (Primary Agent)
                    ↓
                ├── 📋 Task Agent (Sub-Agent 1)
                │   ├── Create Task
                │   ├── Show Tasks
                │   └── Complete Task
                │
                └── 📅 Calendar Agent (Sub-Agent 2)
                    ├── Schedule Meeting
                    ├── Show Meetings
                    └── Cancel Meeting
                    ↓
                💾 SQLite Database
                    ↓
                Response to User
                ```

                ### Key Features:
                - ✅ Multi-Agent Coordination
                - ✅ Tool Integration (Database, Task Tools, Calendar Tools)
                - ✅ Multi-Step Workflows
                - ✅ RESTful API Deployment
                - ✅ Natural Language Processing

                ### Technologies:
                - **Backend**: Python + FastAPI
                - **Agents**: Custom Multi-Agent System
                - **Database**: SQLite
                - **UI**: Gradio
                """
            )

if __name__ == "__main__":
    print("🚀 Launching OrchestrAI Labs UI...")
    print("🌐 Open your browser to use the app!")
    demo.launch(server_name="0.0.0.0", server_port=7860)
