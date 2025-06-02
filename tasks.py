from crewai import Task
from agents import task_analyzer, schedule_builder, productivity_enhancer

def create_task_analysis_task(tasks_content):
    return Task(
        description=f"""
        Analyze these tasks and sort by deadline urgency:
        {tasks_content}
        
        Requirements:
        1. Extract deadlines and sort by urgency (most urgent first)
        2. Assign priority (High/Medium/Low) 
        3. Estimate time needed
        4. Keep output simple and clear
        """,
        agent=task_analyzer,
        expected_output="Simple task list sorted by deadline with priority and time estimates"
    )

def create_schedule_building_task():
    return Task(
        description="""
        Create a simple daily schedule based on the analyzed tasks:
        
        Requirements:
        1. Schedule urgent tasks in morning hours
        2. Create clear time slots
        3. Keep format simple and readable
        4. Use format: 9:00 AM - 11:00 AM: Task Name (2 hours) - High Priority
        """,
        agent=schedule_builder,
        expected_output="Clean schedule with time slots, task names, duration, and priority"
    )

def create_productivity_enhancement_task():
    return Task(
        description="""
        Create a To-Do List format schedule with checkboxes.
        
        **CRITICAL:** Ensure EACH CHECKBOX ITEM IS ON ITS OWN SEPARATE LINE.
        
        Requirements:
        1. Format as a checkable to-do list using '☐' for checkboxes.
        2. Group by priority levels: HIGH, MEDIUM, LOW.
        3. Include time slots and duration for each task.
        4. Add breaks as separate items under 'BREAKS & PERSONAL'.
        5. Keep it clean and organized like a daily planner.
        """,
        agent=productivity_enhancer,
        expected_output="""To-Do List format like this (each item on new line):

📅 **TODAY'S TO-DO LIST**

## 🔴 HIGH PRIORITY
☐ 9:00 AM - 11:00 AM: Complete project report (2 hours)
☐ 11:00 AM - 12:00 PM: Team meeting (1 hour)

## 🟡 MEDIUM PRIORITY  
☐ 1:00 PM - 2:30 PM: Review documents (1.5 hours)
☐ 3:00 PM - 4:00 PM: Email responses (1 hour)

## 🟢 LOW PRIORITY
☐ 4:30 PM - 5:30 PM: Planning next week (1 hour)

## ☕ BREAKS & PERSONAL
☐ 12:00 PM - 1:00 PM: Lunch break
☐ 2:30 PM - 2:45 PM: Coffee break
☐ 5:30 PM onwards: Personal time

💡 **TIP:** Start with high priority tasks when you're most focused!"""
    )