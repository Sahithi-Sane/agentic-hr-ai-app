from datetime import datetime, timedelta

def generate_interview_slots(start_date=None, num_candidates=3):
    if start_date is None:
        start_date = datetime.now() + timedelta(days=1)  # start tomorrow

    slots = []
    for i in range(num_candidates):
        slot_time = start_date + timedelta(hours=2 * i)
        slots.append(slot_time.strftime("%Y-%m-%d %H:%M"))
    return slots
