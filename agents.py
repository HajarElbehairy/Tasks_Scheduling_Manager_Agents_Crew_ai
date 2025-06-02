from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# Setup LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="groq/llama3-8b-8192",
    temperature=0,
    max_tokens=800
)

# Task Analyzer Agent
task_analyzer = Agent(
    role='Task Analyzer',
    goal='Sort tasks by deadline urgency and estimate time - keep output simple',
    backstory="""You are a practical task organizer who creates clear, simple task lists. 
    You prioritize by deadlines and give realistic time estimates.""",
    verbose=False,
    allow_delegation=False,
    llm=llm
)

# Schedule Builder Agent
schedule_builder = Agent(
    role='Schedule Builder',
    goal='Create simple daily schedules with clear time slots',
    backstory="""You are a time management expert who creates clean, easy-to-follow schedules. 
    You put urgent tasks first and use simple time formats.""",
    verbose=False,
    allow_delegation=False,
    llm=llm
)

# Productivity Enhancer Agent
productivity_enhancer = Agent(
    role='Productivity Enhancer',
    goal='Add essential breaks and practical tips - keep it simple',
    backstory="""You are a productivity coach who believes in simplicity. 
    You add necessary breaks and give one useful tip.""",
    verbose=False,
    allow_delegation=False,
    llm=llm
)