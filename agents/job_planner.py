from langchain.prompts import PromptTemplate

def generate_job_description(model, role, experience, skills):
    template = """
    You are an HR assistant for a startup. Create a professional Job Description for the role below:

    Role: {role}
    Experience Required: {experience} years
    Must-have Skills: {skills}

    Provide:
    1. Short company intro
    2. Detailed role responsibilities
    3. Required skills
    4. Nice-to-have skills
    5. Hiring timeline (weeks)
    """
    prompt = PromptTemplate.from_template(template)
    response = model.invoke(prompt.format(role=role, experience=experience, skills=skills))
    return response.content
