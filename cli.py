import os

from auth import create_calendar_service
from get_event import get_upcoming_events
from create_event import create_event

calendar_id = os.environ.get("CALENDAR_ID")

def main():
    service = create_calendar_service()

    print("Getting the upcoming 10 events")
    events = get_upcoming_events(service, calendar_id)
    if not events:
        print("No upcoming events found.")
    else:
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])
    
    print("Creating an event")
    create_event(service, calendar_id)

if __name__ == "__main__":
 main()