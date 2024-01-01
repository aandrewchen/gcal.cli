import os

import typer
from typing_extensions import Annotated

import inquirer

from utils.auth import get_auth
from utils.get_event import get_upcoming_events
from utils.create_event import create_event

calendar_id = os.environ.get("CALENDAR_ID")

app = typer.Typer()

service = get_auth()

@app.command()
def create():
    """
    Create an upcoming event
    """
    summary = typer.prompt("What are you doing?")
    color = [
    inquirer.List('color',
                message="What color should this event be?",
                choices=['1', '2', '3', '4', '5', '6', '7', 'Graphite', '9', '10', '11'],
            ),
    ]
    answer = inquirer.prompt(color)
    
    print("Creating an event")
    create_event(service, calendar_id, summary, answer["color"])

@app.command()
def get(count: str):
    """
    Get the specified number of upcoming events
    """
    print(f"Getting the upcoming {count} events")
    events = get_upcoming_events(service, calendar_id, count)
    if not events:
        print("No upcoming events found.")
    else:
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

@app.command()
def test():
    colors = service.colors().get().execute()

    print(colors)

if __name__ == "__main__":
    app()