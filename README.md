# HR Agents – Agentic AI App for Hiring

## Overview
**Agentic HR AI App** is designed to assist **HR professionals** in planning and managing the **hiring process** for startups or enterprises. This app uses **LangChain**, **Hugging Face**, and custom-built agents to automate and streamline key HR functions like **job description generation**, **resume filtering**, **interview scheduling**, and **onboarding plans**.

The app provides a user-friendly interface via **Streamlit** and integrates several AI-powered tools to assist HR professionals in making the hiring process smoother and more efficient.

## Project Structure

Here’s the breakdown of the directory structure:

hr_agents/
│── app.py # Streamlit entry point for running the app
│── requirements.txt # List of Python dependencies
│── .env.example.txt # Example environment variables file
│
├── agents/ # Core AI agents responsible for business logic
│ ├── job_planner.py # Generates job descriptions
│ ├── resume_filter.py # Builds resume index and shortlists candidates
│ ├── scheduler.py # Creates interview schedules
│ └── onboarding.py # Generates onboarding plans
│
├── utils/ # Helper utilities for the app
│ ├── calendar.py # Helper to generate interview time slots
│ ├── db.py # Manages candidate data in the database
│ └── memory.py # Handles session and memory management
│
└── memory/
└── state.json # Stores session data and memory for context


## Installation

### 1. Clone the repository

To get started, clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/hr_agents.git
cd hr_agents

### 2. Set up a virtual environment

Creating a virtual environment helps manage dependencies for the project without conflicting with your system libraries.

For Linux/Mac:
python3 -m venv venv
source venv/bin/activate
