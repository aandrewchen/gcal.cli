import os

import typer
from typing_extensions import Annotated

import inquirer

from datetime import datetime, timedelta

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

    isRecurring = typer.prompt("Is this a recurring event? (y/n)")

    if isRecurring == "y":
        days = [
            inquirer.Checkbox('days',
                message="Which days does this event occur?",
                choices=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Everyday'],
                carousel=True,
            ),
        ]

        days = inquirer.prompt(days)

        endDate = typer.prompt("When does this recurring event end? (YYYY-MM-DD)").replace("-", "")

    if isRecurring == "y":
        date = typer.prompt("What date is the first event? (YYYY-MM-DD)")
    else:
        date = typer.prompt("What date is the event? (YYYY-MM-DD)")

    startHrMin = typer.prompt("What time does this event start? (HH:MM)")
    endHrMin = typer.prompt("What time does this event end? (HH:MM)")

    startTime = f"{date}T{startHrMin}:00"
    endTime = f"{date}T{endHrMin}:00"

    color = [
    inquirer.List('color',
                message="What color should this event be?",
                choices=['Lavendar', 'Sage', 'Grape', 'Flamingo', 'Banana', 'Tangerine', 'Peacock', 'Graphite', 'Blueberry', 'Basil', 'Tomato'],
            ),
    ]
    color = inquirer.prompt(color)

    print("Creating an event")
    print(startTime)
    print(endTime)
    create_event(
        service, 
        calendar_id, 
        summary, 
        color["color"], 
        startTime, 
        endTime,
        isRecurring,
        days["days"] if isRecurring == "y" else None,
        endDate if isRecurring == "y" else None,
    )

@app.command()
def get(count: Annotated[str, typer.Argument()] = "10"):
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