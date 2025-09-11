def onboarding_plan(model, role):
    query = f"Suggest a 30-60-90 day onboarding plan for a new {role}."
    response = model.invoke(query)
    return response.content

