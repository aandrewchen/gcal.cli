from datetime import datetime, timedelta

def format_time(start_time, end_time):
    start_time = datetime.fromtimestamp(start_time)
    end_time = datetime.fromtimestamp(end_time)

    start_time = start_time.replace(second=0, microsecond=0)
    if end_time.second != 0 or end_time.microsecond != 0:
        end_time = end_time.replace(second=0, microsecond=0) + timedelta(minutes=1)
    
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S")
    end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S")

    return start_time, end_time