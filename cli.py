import os

import typer
from typing_extensions import Annotated

from utils.auth import get_auth
from utils.get_event import get_upcoming_events
from utils.create_event import create_event

calendar_id = os.environ.get("CALENDAR_ID")

app = typer.Typer()

service = get_auth()

@app.command()
def create():
    print("Creating an event")
    create_event(service, calendar_id)

@app.command()
def get():
    print("Getting the upcoming 10 events")
    events = get_upcoming_events(service, calendar_id)
    if not events:
        print("No upcoming events found.")
    else:
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

@app.command()
def test():
    print("Testing")

if __name__ == "__main__":
    app()