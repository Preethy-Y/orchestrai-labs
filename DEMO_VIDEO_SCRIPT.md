# 🎬 Demo Video Script (3 Minutes)

## Setup Before Recording
- [ ] Open UI at http://localhost:7860
- [ ] Clear any test data
- [ ] Prepare screen recording software (OBS Studio or Windows Game Bar)
- [ ] Close unnecessary browser tabs
- [ ] Practice once before final recording

---

## Script Timeline

### **[0:00 - 0:30] Introduction (30 seconds)**

**[Show title slide or introduce yourself on camera]**

**Say:**
> "Hello! I'm [Your Name] from [Team Name], and we're presenting OrchestrAI Labs - a multi-agent AI system built for the Gen AI Academy APAC Edition hackathon.
>
> We're solving the problem of fragmented task and schedule management by using coordinated AI agents that work together to complete complex workflows."

**[Switch to architecture diagram or show the system overview]**

---

### **[0:30 - 1:15] Architecture Explanation (45 seconds)**

**[Show the architecture tab in your UI or a diagram]**

**Say:**
> "Our system uses a multi-agent architecture with three key components:
>
> First, the Orchestrator Agent - our primary agent that analyzes user requests and decides which specialized agents to use.
>
> Second, the Task Agent - a sub-agent that handles all task management operations.
>
> Third, the Calendar Agent - another sub-agent that manages meeting scheduling.
>
> All agents interact with a SQLite database and use MCP tools for task and calendar management. This demonstrates true multi-agent coordination where agents communicate to complete complex, multi-step workflows."

**[Point to different parts of the architecture as you explain]**

---

### **[1:15 - 2:30] Live Demo (75 seconds)**

**[Switch to the UI - Chat tab]**

**Say:**
> "Let me show you how it works in action."

**Demo 1: Simple Task (15 seconds)**

**Type in chat:** "Create task to finish hackathon project"

**Say while typing:**
> "I'll start with a simple request - creating a task."

**[Wait for response]**

**Say:**
> "The Orchestrator routes this to the Task Agent, which stores it in the database. Task created successfully!"

**Demo 2: Simple Meeting (15 seconds)**

**Type in chat:** "Schedule meeting tomorrow at 3pm"

**Say:**
> "Now let's schedule a meeting."

**[Wait for response]**

**Say:**
> "Calendar Agent handles this and schedules the meeting. Done!"

**Demo 3: Multi-Agent Workflow (30 seconds)**

**Type in chat:** "Schedule team meeting tomorrow and create task to prepare presentation"

**Say:**
> "Here's where it gets impressive - a multi-step workflow requiring coordination between multiple agents."

**[Wait for response showing both steps]**

**Say:**
> "Notice how the Orchestrator analyzed the request, called BOTH the Calendar Agent to schedule the meeting AND the Task Agent to create the reminder - all automatically. This is true multi-agent coordination in action!"

**[Optional: Click on Tasks tab or Meetings tab to show the results]**

**Say (15 seconds):**
> "We can verify everything was stored correctly..."

**[Show the tasks and meetings lists]**

---

### **[2:30 - 2:50] Technical Stack (20 seconds)**

**[Show code editor briefly or list on screen]**

**Say:**
> "From a technical perspective, we built this using Python with FastAPI for the backend, SQLite for data persistence, and Gradio for the user interface. 
>
> It's deployed on Google Cloud Run as a containerized API, making it scalable and production-ready."

---

### **[2:50 - 3:00] Conclusion (10 seconds)**

**[Return to camera or show final slide]**

**Say:**
> "OrchestrAI Labs demonstrates true multi-agent AI coordination, meets all hackathon requirements, and solves a real-world problem. Thank you for watching!"

**[Smile and wave if on camera]**

---

## Recording Tips

### Before Recording:
1. **Test your microphone** - clear audio is crucial
2. **Close notifications** - turn on "Do Not Disturb" mode
3. **Clear browser cache** - ensure smooth performance
4. **Have water nearby** - in case you need to restart
5. **Lighting** - if showing your face, ensure good lighting

### During Recording:
1. **Speak clearly and confidently** - imagine explaining to a friend
2. **Don't rush** - better to use 2:50 than cram into 3:00
3. **Pause between sections** - easier to edit if needed
4. **Show enthusiasm** - judges appreciate passion
5. **If you mess up** - just keep going or restart (it's only 3 minutes!)

### Recording Tools:
- **Windows**: Xbox Game Bar (Win + G) - built-in, free
- **Professional**: OBS Studio (free) - more features
- **Mac**: QuickTime Player or Screen Recording
- **Online**: Loom (free tier) - very easy to use

### After Recording:
1. **Watch it once** - check audio and video quality
2. **Upload to YouTube** - set as "Unlisted" (not private!)
3. **Test the link** - make sure it's accessible
4. **Alternative**: Upload to Google Drive with public sharing enabled

---

## YouTube Upload Settings

**Title:** OrchestrAI Labs - Multi-Agent AI System | Gen AI Academy APAC

**Description:**
```
OrchestrAI Labs - Multi-Agent Productivity Assistant
Gen AI Academy APAC Edition Hackathon Submission

A multi-agent AI system featuring:
- Orchestrator Agent (Primary)
- Task Agent & Calendar Agent (Sub-agents)
- SQLite Database Integration
- MCP Tools Integration
- Multi-step Workflow Coordination

Built with: Python, FastAPI, Gradio
Deployed on: Google Cloud Run

Team: [Your Team Name]
Track: Multi-Agent Productivity Assistant

GitHub: [Your GitHub Link]
```

**Visibility:** 🔓 Unlisted (Important!)

**Tags:** AI, Multi-Agent System, Hackathon, Gen AI Academy, Google Cloud

---

## Alternative: Google Drive Upload

If you prefer Google Drive:

1. **Upload video file**
2. **Right-click** → Share
3. **Change to**: Anyone with the link can view
4. **Copy link**
5. **Test in incognito window** to verify it's accessible

---

## Video Quality Checklist

- [ ] Audio is clear (no background noise)
- [ ] Video is at least 720p (HD)
- [ ] Text/UI is readable
- [ ] Demo flows smoothly
- [ ] All features shown work correctly
- [ ] Under 3 minutes
- [ ] Link is publicly accessible
- [ ] Tested link in incognito/private browser

---

## Emergency Backup Plan

If you're uncomfortable on camera:
- **Just do a screen recording with voiceover**
- No need to show your face
- Focus on the demo and architecture
- Judges care more about the project than presentation style

**Remember:** A simple, clear demo is better than a fancy, confusing one!
