from datetime import datetime


def get_current_time():
    print("Common utility loaded")
    return datetime.utcnow().isoformat()