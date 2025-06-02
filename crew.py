from crewai import Crew, Process
from agents import task_analyzer, schedule_builder, productivity_enhancer
from tasks import create_task_analysis_task, create_schedule_building_task, create_productivity_enhancement_task

def create_scheduling_crew(tasks_content):
    # Create tasks
    task_analysis = create_task_analysis_task(tasks_content)
    schedule_building = create_schedule_building_task()
    productivity_enhancement = create_productivity_enhancement_task()
    
    # Create crew
    crew = Crew(
        agents=[task_analyzer, schedule_builder, productivity_enhancer],
        tasks=[task_analysis, schedule_building, productivity_enhancement],
        process=Process.sequential,
        verbose=False
    )
    
    return crew

def run_scheduling_process(tasks_content):
    """Run the scheduling process with error handling"""
    try:
        crew = create_scheduling_crew(tasks_content)
        result = crew.kickoff()
        return result
    except Exception as e:
        error_msg = str(e)
        if "rate_limit" in error_msg.lower():
            return "⏳ Rate limit reached. Please wait a few seconds and try again."
        else:
            return f"❌ Error creating schedule: {error_msg}"