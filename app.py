import os
import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForCausalLM
# from langchain.chat_models import ChatHuggingFace
 
# === Import Agents & Utils ===
from agents.job_planner import generate_job_description
from agents.resume_filter import build_resume_index, shortlist_candidates
from agents.scheduler import create_schedule
from agents.onboarding import onboarding_plan
from utils.db import CandidateDB
from utils.memory import HRMemory
from utils.calendar import generate_interview_slots
 
# === Load API Key ===
load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
 
# === Setup LLM + Embeddings ===
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
)
 
# Load the tokenizer and model
# model_name = "meta-llama/Meta-Llama-3-8B"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")  # device_map="auto" uses GPU if available
 
# Wrap it in LangChain's ChatHuggingFace
# llm = ChatHuggingFace(model=model, tokenizer=tokenizer)
 
 
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
model = ChatHuggingFace(llm=llm)
 
# === Initialize Utils ===
db = CandidateDB()
memory = HRMemory()
 
# === Streamlit App ===
st.set_page_config(page_title="Agentic HR App", layout="wide")
st.title("Agentic HR Assistant for Startups")
 
# Sidebar navigation
menu = st.sidebar.radio("Select Module", ["Job Planner", "Resume Filter", "Interview Scheduler", "Onboarding Plan", "Candidate DB"])
 
 
# --- RESUME FILTER ---
# --- JOB PLANNER ---
if menu == "Job Planner":
    st.subheader("Generate Job Description")
 
    with st.form("job_planner_form"):   # wrap inputs inside form
        role = st.text_input("Role", "Enter any role")
        experience = st.number_input("Experience Required (years)", min_value=0, max_value=20, value=2)
        skills = st.text_area("Enter Skills (comma separated)")
        submit_jd = st.form_submit_button("Generate JD")  # form submit button
 
    if submit_jd:  # will only run when button is clicked
        jd = generate_job_description(model, role, experience, skills)
        st.success("Job Description Generated")
        st.write(jd)
        memory.save_context("last_jd", jd)
 
       
       
 
# --- INTERVIEW SCHEDULER ---
elif menu == "Interview Scheduler":
    st.subheader("Plan Interviews")
 
    with st.form("interview_scheduler_form"):  # wrap in form
        num_candidates = st.number_input("Number of Candidates", min_value=1, max_value=20, value=3)
        submit_schedule = st.form_submit_button("Generate Schedule")  # submit button
 
    if submit_schedule:  # only runs when button clicked
        schedule = create_schedule(model, num_candidates)
        slots = generate_interview_slots(num_candidates=num_candidates)
        st.success("Interview Schedule Suggested")
        st.write(schedule)
        st.write("Interview Slots:", slots)
 
# --- ONBOARDING PLAN ---
elif menu == "Onboarding Plan":
    st.subheader("30-60-90 Day Onboarding Plan")
 
    with st.form("onboarding_plan_form"):  # wrap in form
        role = st.text_input("Role", "Data Analyst")
        submit_plan = st.form_submit_button("Generate Plan")  # submit button
 
    if submit_plan:  # only runs on submit
        plan = onboarding_plan(model, role)
        st.success("Onboarding Plan Generated")
        st.write(plan)
 
# --- CANDIDATE DB ---
elif menu == "Candidate DB":
    st.subheader("Candidate Database")
    candidates = db.list_candidates()
 
    # No need for form here since it's just displaying
    if candidates:
        st.table(candidates)
    else:
        st.info("No candidates stored yet.")