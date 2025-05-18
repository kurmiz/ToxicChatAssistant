from datetime import datetime

def get_date():
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    return f"Today's date is {current_date}."