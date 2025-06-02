# 🚀 Smart Task Manager with AI Agents

![Task Management](https://img.shields.io/badge/Task%20Management-AI%20Powered-brightgreen)
![Built with CrewAI](https://img.shields.io/badge/Built%20with-CrewAI-blue)
![LLM](https://img.shields.io/badge/LLM-Groq%20API-orange)
![UI](https://img.shields.io/badge/UI-Streamlit-red)

A powerful task scheduling system that uses AI agents to organize your day based on priorities and deadlines. This project leverages a team of specialized AI agents to analyze, schedule, and optimize your tasks intelligently.



## ✨ Features

- **🔍 Intelligent Deadline Analysis**: Automatically identifies and prioritizes tasks based on deadlines
- **⏰ Smart Time Allocation**: Creates optimized time blocks for your tasks
- **📊 Priority-Based Scheduling**: Ensures important tasks get the best time slots
- **☕ Strategic Breaks**: Integrates appropriate breaks to maintain productivity
- **📱 Simple Interface**: Easy-to-use Streamlit UI
- **📥 Exportable Results**: Download your schedule as a text file

## 🛠️ How It Works

The system consists of three specialized AI agents working together:

1. **Task Analyzer Agent**
   - Parses your tasks and extracts deadline information
   - Sorts tasks by urgency and importance
   - Classifies tasks by type and estimates required time

2. **Schedule Builder Agent**
   - Creates a time-optimized daily schedule
   - Allocates prime productive hours to critical tasks
   - Balances workload throughout the day

3. **Productivity Enhancer Agent**
   - Adds strategic breaks between tasks
   - Implements productivity techniques like Pomodoro
   - Formats the schedule as an easy-to-use to-do list

## 📋 Input Format

Tasks should be formatted as follows:
```
- Task name (deadline: when, duration)
```

Examples:
```
- Complete project report (deadline: today 5pm, 2 hours)
- Team meeting (deadline: tomorrow 2pm, 1 hour)
- Review emails (deadline: today evening, 30 minutes)
- Call client (deadline: Friday morning, 45 minutes)
- Research new tools (deadline: next week, 3 hours)
```

## 📊 Output Example

```
📅 TODAY'S TO-DO LIST

🔴 HIGH PRIORITY
1. 9:00 AM - 11:00 AM: Complete project report (2 hours)
2. 11:00 AM - 12:00 PM: Review emails (1 hour)

🟡 MEDIUM PRIORITY
1. 1:00 PM - 2:00 PM: Team meeting (1 hour)
2. 3:00 PM - 3:45 PM: Call client (45 minutes)

🟢 LOW PRIORITY
1. 4:00 PM - 5:00 PM: Research new tools (1 hour)

☕ BREAKS & PERSONAL
1. 12:00 PM - 1:00 PM: Lunch break
2. 2:00 PM - 2:15 PM: Coffee break
3. 5:00 PM onwards: Personal time

💡 TIP: Start with high priority tasks when your energy is highest!
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A Groq API key (get one at [console.groq.com](https://console.groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/smart-task-manager.git
   cd smart-task-manager
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Create a `.env` file in the project directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
smart-task-manager/
├── app.py                 # Streamlit UI
├── agents.py              # AI agent definitions
├── tasks.py               # Task definitions for the agents
├── crew.py                # Agent orchestration
├── requirements.txt       # Dependencies
├── .env                   # API keys (create this file)
└── README.md              # This file
```

## 🔧 Technology Stack

- **Agent Framework**: [CrewAI](https://github.com/joaomdmoura/crewAI)
- **LLM Provider**: [Groq API](https://console.groq.com)
- **UI Framework**: [Streamlit](https://streamlit.io)
- **Language Models**: Llama3 (via Groq)

## ⚠️ Limitations

- Free tier Groq API has rate limits that may cause occasional errors
- Complex task descriptions might not parse correctly
- The system works best with clearly defined deadlines and durations

## 🔮 Future Enhancements

- Integration with calendar systems (Google Calendar, Outlook)
- Recurring task support
- Mobile app version
- Progress tracking and analytics
- Multiple day planning

## 📚 References

- [CrewAI Documentation](https://crewai.io)
- [Groq API Documentation](https://console.groq.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io)

## 🔗 Connect & Contribute

Feel free to fork this repository, submit PRs, or suggest improvements!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Built with ❤️ using AI agents to make your day more productive!
