# Agentic HR Assistant – AI Workflow Automation System

## Overview
The **Agentic HR Assistant** is an AI-driven system designed to automate key stages of the hiring lifecycle, including job description generation, candidate screening, interview scheduling, and onboarding planning.

Unlike traditional chatbots, this system follows an **agent-inspired architecture**, where multiple specialized components collaborate to complete complex workflows. The design mirrors real-world enterprise service management systems used in IT and HR operations.

The app provides a user-friendly interface via **Streamlit** and integrates several AI-powered tools to assist HR professionals in making the hiring process smoother and more efficient.

---

## 🎯 Key Capabilities

- 🧠 **Job Description Generation**  
  Automatically generates structured job descriptions based on role requirements.

- 📄 **Semantic Resume Screening**  
  Uses embedding-based similarity to evaluate and rank candidates beyond keyword matching.

- 🔁 **Agent-Based Workflow Orchestration**  
  Modular components simulate agent behavior (planning → evaluation → action).

- 📅 **Interview Scheduling (Mock MCP Integration)**  
  Simulates external tool integration (calendar scheduling) via a mock service layer.

- 📘 **Onboarding Plan Generation**  
  Creates structured onboarding workflows (30-60-90 day plans).

- 💬 **Interactive UI (Streamlit)**  
  Lightweight frontend for demonstrating end-to-end workflow.

---

## Workflow

1. User provides hiring requirement  
2. System generates job description  
3. Candidate resumes are indexed and evaluated  
4. Candidates are ranked using semantic similarity  
5. Interview scheduling is triggered  
6. Onboarding plan is generated  

---

## Project Structure

```
hr_agents/
│── app.py                  # Streamlit entry point
│── graphy                  # LangGraph StateGraph orchestration
│── requirements.txt        # Dependencies
│── .env                    # Environment variables template
│
├── mcp_tools/              # MCP connections
│   ├── __init__.py        
│   ├── calender_tool.py    # Calender MCP
│
├── agents/                 # Core agent modules
│   ├── job_planner.py      # Job description generation
│   ├── resume_filter.py    # Resume indexing + ranking
│   ├── scheduler.py        # Interview scheduling
│   └── onboarding.py       # Onboarding plan generation
│
├── data/                   # Data 
│   ├── applicatiions.json  # All the applications for multiple roles
│   ├── candidates.json     # Unique candidates
│   
├── utils/                  # Supporting utilities
│   ├── calendar.py         # Interview slot generation
│   ├── db.py               # Candidate data handling
│   └── memory.py           # Session memory management
│   └── guardrails.py       # Safety checks before and after agents
│
└── memory/
    └── state.json          # Persistent session state
```
---

## Demo Video 

https://drive.google.com/file/d/1vppzSK5PttuaLklPSP8eh3Y55CrEAcuL/view?usp=sharing

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sahithi-Sane/agentic-hr-ai-app.git
cd agentic-hr-ai-app
```

---

### 2. Create virtual environment

```bash
python -m venv agentic_hr
```

---

### 3. Activate environment

```bash
agentic_hr\Scripts\activate   # Windows
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT="Agentic HR"
```

Optional:
```env
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

---

### 6. Run the application

```bash
streamlit run app.py
```
This will open the app in your web browser. You can now interact with the different modules of the HR Agentic AI App.

---

## 🔌 Integrations

- **Mock MCP (Default)**
  - Used for stable demo and simulation of scheduling workflows

- **Extensible Integrations**
  - Google Calendar
  - ServiceNow / ITSM tools
  - HR systems (ATS platforms)

--- 

## Features

### 1. **Planner Agent**
  - Interprets hiring requirements
  - Generates structured job descriptions

### 2. **Screening Agent**
  - Converts resumes into embeddings
  - Performs semantic similarity ranking

### 3. **Scheduler Agent**
  - Generates interview slots
  - Simulates calendar integration via MCP layer

### 4. **Onboarding Agent**
  - Produces onboarding plans based on role context

### 5. **Memory Management**
   - **Context-Aware Interactions**: The app retains session data using **memory** (saved in `state.json`) for more personalized and context-aware interactions.

### 6. **MCP (Tool Interface Layer)**
  - Simulates external integrations (e.g., calendar APIs)
  - Designed to be replaceable with real services

## Tech Stack

This project is built using the following technologies:

- **Python 3.11+**
- **Streamlit**: A framework for building interactive web applications.
- **LangChain**: A framework for building AI-powered agents.
- **Hugging Face**: Provides pre-trained models and embeddings for natural language processing.
- **Custom Utils**: Includes helpers for database management, memory handling, and generating interview slots.

## Next Steps (Future Enhancements)

### 1. **User Authentication**:
   - Add login and user roles for HR professionals, allowing them to store their data securely.

### 2. **Integrations**:
   - Integrate with external systems such as **Slack**, **Google Calendar**, and **ATS systems** to automate more HR processes.

### 3. **Deployment**:
   - **Docker**: Containerize the app for easy deployment.
   - **Cloud Deployment**: Deploy the app to cloud platforms like **AWS**, **GCP**, or **Azure** for scalable usage.

---

## 📊 Future Enhancements

- Evaluation metrics (Precision@K, ranking quality)
- Confidence scoring for candidate selection
- Real API integrations (calendar, HR tools)
- Persistent database (PostgreSQL / NoSQL)
- Monitoring and observability (LangSmith dashboards)
- Role-based access and authentication

---

## Troubleshooting

- **App Not Starting**: Make sure all dependencies are installed and `.env` variables are correctly set.
- **API Key Issues**: If you encounter issues with API calls, ensure that the keys in the `.env` file are correct and that the respective APIs are active.

## Note

This is a **prototype system** focused on demonstrating architecture and workflow design.  
It is designed to be easily extended into a production-grade system.

---

## 👤 Author

**Sahithi Sane**  
