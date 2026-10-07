from datetime import datetime


def get_current_datetime():
    now = datetime.now()

    return now.strftime("%A, %B %d, %Y %I:%M %p")