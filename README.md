# HR Agents – Agentic AI App for Hiring

## Overview
**Agentic HR AI App** is designed to assist **HR professionals** in planning and managing the **hiring process** for startups or enterprises. This app uses **LangChain**, **Hugging Face**, and custom-built agents to automate and streamline key HR functions like **job description generation**, **resume filtering**, **interview scheduling**, and **onboarding plans**.

The app provides a user-friendly interface via **Streamlit** and integrates several AI-powered tools to assist HR professionals in making the hiring process smoother and more efficient.

## Project Structure

Here’s the breakdown of the directory structure:

```
hr_agents/
│── app.py                  # Streamlit entry point for running the app
│── requirements.txt        # List of Python dependencies
│── .env.example.txt        # Example environment variables file
│
├── agents/                 # Core AI agents responsible for business logic
│   ├── job_planner.py      # Generates job descriptions
│   ├── resume_filter.py    # Builds resume index and shortlists candidates
│   ├── scheduler.py        # Creates interview schedules
│   └── onboarding.py       # Generates onboarding plans
│
├── utils/                  # Helper utilities for the app
│   ├── calendar.py         # Helper to generate interview time slots
│   ├── db.py               # Manages candidate data in the database
│   └── memory.py           # Handles session and memory management
│
└── memory/
    └── state.json          # Stores session data and memory for context
```
## Demo Video 

https://drive.google.com/file/d/1vppzSK5PttuaLklPSP8eh3Y55CrEAcuL/view?usp=sharing

## Installation

### 1. Clone the repository

To get started, clone the repository to your local machine.

```bash
git clone https://github.com/Sahithi-Sane/agentic-hr-ai-app.git
cd agents
```

### 2. Set up a virtual environment

Creating a virtual environment helps manage dependencies for the project without conflicting with your system libraries.

#### For Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Once the virtual environment is activated, install the necessary Python libraries using `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Some services require **API keys** to work. You will need to set up the required environment variables to access them. Copy the example environment file and update it with your own API keys.

```bash
cp .env.example.txt .env
```

Now, open the `.env` file and add the following keys:

```env
HUGGINGFACEHUB_API_TOKEN=your_hf_token
OPENAI_API_KEY=your_openai_key
```

- **HUGGINGFACEHUB_API_TOKEN**: You can get this token by signing up at [Hugging Face](https://huggingface.co/) and accessing your account settings.
- **OPENAI_API_KEY**: You can obtain this key from [OpenAI](https://beta.openai.com/signup/).

### 5. Additional Setup 

If your app uses additional services (like a database or cloud APIs), ensure the corresponding configuration and keys are set up in `.env`. You can add any other required variables as needed.

## Running the App

After the setup, you can run the Streamlit app using the following command:

```bash
streamlit run app.py
```

This will open the app in your web browser. You can now interact with the different modules of the HR Agentic AI App.

## Features

### 1. **Job Planning Agent**
   - **Generate Job Descriptions**: Based on the role/title, the app automatically generates a detailed job description using the **LangChain agent** and the **Hugging Face model**.

### 2. **Resume Filter Agent**
   - **Index Resumes**: The app creates an index of resumes and shortlists candidates using **embeddings** from **Hugging Face** models.

### 3. **Scheduler Agent**
   - **Interview Scheduler**: Automatically generates structured interview schedules based on the number of candidates and available slots.

### 4. **Onboarding Agent**
   - **Generate Onboarding Plan**: Customizes the 30-60-90 day onboarding plan for new hires.

### 5. **Memory Management**
   - **Context-Aware Interactions**: The app retains session data using **memory** (saved in `state.json`) for more personalized and context-aware interactions.

## Tech Stack

This project is built using the following technologies:

- **Python 3.11+**
- **Streamlit**: A framework for building interactive web applications.
- **LangChain**: A framework for building AI-powered agents.
- **Hugging Face**: Provides pre-trained models and embeddings for natural language processing.
- **Custom Utils**: Includes helpers for database management, memory handling, and generating interview slots.

## How the App Works

- **LangChain Agents** orchestrate the flow of tasks. For example, when you want to generate a job description, the app first collects input from the user (like role, experience, and skills), and then uses the **Job Planning Agent** to generate a detailed job description.

- **Memory** is utilized to store important session data such as the last generated job description or the list of candidates, making the app capable of contextually aware interactions.

## Next Steps (Future Enhancements)

### 1. **User Authentication**:
   - Add login and user roles for HR professionals, allowing them to store their data securely.

### 2. **Integrations**:
   - Integrate with external systems such as **Slack**, **Google Calendar**, and **ATS systems** to automate more HR processes.

### 3. **Deployment**:
   - **Docker**: Containerize the app for easy deployment.
   - **Cloud Deployment**: Deploy the app to cloud platforms like **AWS**, **GCP**, or **Azure** for scalable usage.

## Troubleshooting

- **App Not Starting**: Make sure all dependencies are installed and `.env` variables are correctly set.
- **API Key Issues**: If you encounter issues with API calls, ensure that the keys in the `.env` file are correct and that the respective APIs are active.

