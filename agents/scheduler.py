def create_schedule(model, num_candidates, start_date="Next Monday"):
    query = f"""
    Plan an interview schedule for {num_candidates} candidates starting {start_date}.
    Include:
    - Interview rounds
    - Estimated duration
    - Suggested tools (Zoom, Google Meet, etc.)
    """
    response = model.invoke(query)
    return response.content
