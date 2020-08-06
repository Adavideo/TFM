from datetime import datetime

def get_date(date_string):
    date = datetime.fromisoformat(date_string)
    date_without_timezone = date.astimezone(tz=None)
    return date_without_timezone
