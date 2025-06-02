import streamlit as st
import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from crew import run_scheduling_process

load_dotenv()

def main():
    st.set_page_config(
        page_title="Smart Task Manager",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 Smart Task Manager with AI Agents")
    st.subheader("Intelligent task scheduling system with deadline priority using CrewAI")
    
    # Check for API Key
    if not os.getenv("GROQ_API_KEY"):
        st.error("⚠️ Please add GROQ_API_KEY to your .env file")
        st.stop()
    
    # Sidebar - SWAPPED ORDER HERE
    st.sidebar.header("✍️ Manual Input")
    manual_tasks = st.sidebar.text_area(
        "Write your tasks here:",
        height=200
    )
    
    # File upload MOVED BELOW manual tasks
    st.sidebar.header("📁 Task Input")
    uploaded_file = st.sidebar.file_uploader("Choose a task file", type=['txt'])
    
    # Sample tasks button
    if st.sidebar.button("📋 Use Sample Tasks"):
        manual_tasks = """- Complete quarterly presentation (deadline: today 4pm, 2 hours)
- Client meeting preparation (deadline: tomorrow 9am, 1 hour)
- Review and respond to emails (deadline: today end of day, 30 minutes)
- Gym workout session (deadline: today evening, 45 minutes)
- Read development book chapter (deadline: this week, 1 hour)"""
    
    # Get task content
    tasks_content = ""
    if uploaded_file:
        tasks_content = uploaded_file.read().decode('utf-8')
        st.sidebar.success("✅ File uploaded!")
    elif manual_tasks:
        tasks_content = manual_tasks
    
    # Display input tasks
    if tasks_content:
        st.header("📋 Input Tasks")
        st.text_area("", tasks_content, height=150, disabled=True)
        
        # Run system button
        if st.button("📋 Generate Numbered To-Do List", type="primary", use_container_width=True):
            with st.spinner("🤖 Creating your to-do list..."):
                # Run scheduling process
                result = run_scheduling_process(tasks_content)
                
                # Check for errors
                if "Rate limit reached" in str(result) or "Error" in str(result):
                    st.error(result)
                    st.info("💡 Please wait a few seconds and try again")
                else:
                    # Success
                    st.success("✅ Your to-do list is ready!")
                    
                    # Display the to-do list
                    st.header("📋 Your Daily To-Do List")
                    
                    # Display the result as is
                    st.markdown(result)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download To-Do List",
                        data=str(result),
                        file_name=f"todo_list_{datetime.now().strftime('%Y%m%d')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                    
                    # Print view button
                    if st.button("🖨️ Print View", use_container_width=True):
                        st.code(result)
                    
                    # Progress tracking
                    with st.expander("📊 Daily Progress"):
                        st.markdown("""
                        **Track Your Progress:**
                        - Mark off completed tasks
                        - Focus on high priority items first
                        - Follow your scheduled time slots
                        """)
    
    else:
        st.info("📝 Enter your tasks to generate a to-do list")
        
        # Quick example
        st.markdown("**Example:**")
        st.code("""- Finish project report (deadline: today 5pm, 2 hours)
- Team meeting (deadline: tomorrow 2pm, 1 hour)
- Check emails (deadline: today evening, 30 minutes)""")
    
    # Instructions
    with st.expander("📖 How to Format Your Tasks"):
        st.markdown("""
        **Simple Format:** `- Task name (deadline: when, duration)`
        
        **Examples:**
        ```
        - Write presentation (deadline: today 4pm, 2 hours)
        - Call client (deadline: tomorrow morning, 30 minutes)
        - Submit report (deadline: Friday, 1 hour)
        ```
        """)
    
    # System information
    with st.expander("ℹ️ About the System"):
        st.markdown("""
        **🤖 Three AI Agents Working for You:**
        
        **🔍 Task Analyzer:** Sorts your tasks by deadline urgency and priority
        
        **📊 Schedule Builder:** Creates optimal time slots for maximum productivity
        
        **⚡ Productivity Enhancer:** Formats everything as a numbered to-do list with breaks
        
        **🛠️ Technologies:** CrewAI • Groq API • Streamlit • Smart Scheduling
        """)

if __name__ == "__main__":
    main()