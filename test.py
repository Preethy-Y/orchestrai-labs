"""
Quick Test Script
Run this to make sure everything works!
"""

print("🧪 Testing OrchestrAI Labs System...\n")

# Test 1: Database
print("Test 1: Database Setup")
try:
    from database import init_db
    init_db()
    print("✅ Database initialized successfully!\n")
except Exception as e:
    print(f"❌ Database error: {e}\n")

# Test 2: Task Agent
print("Test 2: Task Agent")
try:
    from task_agent import TaskAgent
    task_agent = TaskAgent()
    result = task_agent.create_task("Test Task", "This is a test")
    print(f"✅ Task Agent working: {result['message']}\n")
except Exception as e:
    print(f"❌ Task Agent error: {e}\n")

# Test 3: Calendar Agent
print("Test 3: Calendar Agent")
try:
    from calendar_agent import CalendarAgent
    calendar_agent = CalendarAgent()
    result = calendar_agent.schedule_meeting("Test Meeting", "tomorrow")
    print(f"✅ Calendar Agent working: {result['message']}\n")
except Exception as e:
    print(f"❌ Calendar Agent error: {e}\n")

# Test 4: Orchestrator
print("Test 4: Orchestrator Agent")
try:
    from orchestrator import OrchestratorAgent
    orchestrator = OrchestratorAgent()
    result = orchestrator.process_request("Create task to finish hackathon")
    print(f"✅ Orchestrator working: {result['message']}\n")
except Exception as e:
    print(f"❌ Orchestrator error: {e}\n")

# Test 5: Multi-step workflow
print("Test 5: Multi-Step Workflow")
try:
    from orchestrator import OrchestratorAgent
    orchestrator = OrchestratorAgent()
    result = orchestrator.process_request("Schedule meeting and create task")
    print(f"✅ Multi-step workflow working!\n")
    if "steps" in result:
        print("   Steps completed:")
        for i, step in enumerate(result["steps"], 1):
            print(f"   {i}. {step['message']}")
    print()
except Exception as e:
    print(f"❌ Multi-step error: {e}\n")

print("=" * 50)
print("🎉 All tests completed!")
print("=" * 50)
print("\n📌 Next Steps:")
print("1. Run the UI: python ui.py")
print("2. Or run the API: python main.py")
print("3. Start testing your demo!")
