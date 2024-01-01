import os

import typer
from typing import Optional
from typing_extensions import Annotated

from auth import get_auth
from get_event import get_upcoming_events
from create_event import create_event

calendar_id = os.environ.get("CALENDAR_ID")


def main(start: Annotated[Optional[str], typer.Argument()] = None):
    service = get_auth()

    if start is None or start == "get":
        print("Getting the upcoming 10 events")
        events = get_upcoming_events(service, calendar_id)
        if not events:
            print("No upcoming events found.")
        else:
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                print(start, event["summary"])
    elif start =="create":
        print("Creating an event")
        create_event(service, calendar_id)

if __name__ == "__main__":
    typer.run(main)
