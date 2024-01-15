import os
import time

import typer
from typing_extensions import Annotated
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.text import Text

import inquirer

from InquirerPy import prompt as promptpy

from utils.auth import get_auth
from utils.get_event import get_upcoming_events, get_event_by_id, convert_time, convert_date
from utils.delete_event import delete_event_by_id
from utils.create_event import create_event
from utils.format_time import format_time

from googleapiclient.errors import HttpError

calendar_id = os.environ.get("CALENDAR_ID")

app = typer.Typer(help="📅 CLI Tool to automate procedures & manage Google Calendar 📅", rich_markup_mode="rich", epilog="Made with :heart: by Andrew Chen")

start_time_file = "start_time.txt"

@app.command()
def create(
    summary: Annotated[str, typer.Option(help="What is the event? 📝", show_default=False)] = None,
    isRecurring: Annotated[str, typer.Option(help="Is the event recurring? [italic bold](y/n)[/italic bold] 🔁", show_default=False)] = None,
    days: Annotated[str, typer.Option(help="If recurring, what days does this event occur? [italic bold]['day', 'day', 'etc.'][/italic bold] 📆", show_default=False)] = None,
    endDate: Annotated[str, typer.Option(help="If recurring, when does this recurring event end? [italic bold](YYYY-MM-DD)[/italic bold] ✋", show_default=False)] = None,
    date: Annotated[str, typer.Option(help="What date is the (first) event? [italic bold](YYYY-MM-DD)[/italic bold] 🗓️", show_default=False)] = None,
    start: Annotated[str, typer.Option(help="What time does this event start? [italic bold](HH:MM)[/italic bold] ⏳", show_default=False)] = None,
    end: Annotated[str, typer.Option(help="What time does this event end? [italic bold](HH:MM)[/italic bold] ⌛️", show_default=False)] = None,
    color: Annotated[str, typer.Option(help="What color should this event be? 🎨", show_default=False)] = None,
    confirm: Annotated[str, typer.Option(help="Are you sure you want to create this event? [italic bold](y/n)[/italic bold] ✅", show_default=False)] = None,
):
    """
    [green bold]Create[/green bold] an upcoming event with specified properties :sparkles:
    """
    if summary is None:
        summary = typer.prompt("What are you doing?")

    if isRecurring is None:
        isRecurring = typer.prompt("Is this a recurring event? (y/n)")

    if isRecurring == "y":
        if days is None:
            days = [
                inquirer.Checkbox('days',
                    message="Which days does this event occur?",
                    choices=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Everyday'],
                    carousel=True,
                ),
            ]

            days = inquirer.prompt(days)
        else:

            days = {
                "days": [day.strip() for day in days.split(',')],
            }

        if endDate is None:
            endDate = typer.prompt("When does this recurring event end? (YYYY-MM-DD)").replace("-", "")
        else:
            endDate = endDate.replace("-", "")

    if date is None:
        if isRecurring == "y":
            date = typer.prompt("What date is the first event? (YYYY-MM-DD)")
        else:
            date = typer.prompt("What date is the event? (YYYY-MM-DD)")

    if start is None:
        start = typer.prompt("What time does this event start? (HH:MM)")
    if end is None:
        end = typer.prompt("What time does this event end? (HH:MM)")

    startTime = f"{date}T{start}:00"
    endTime = f"{date}T{end}:00"

    if color is None:
        color = [
            {
                "type": "fuzzy",
                "message": "What color should this event be?",
                "choices": ['Lavendar', 'Sage', 'Grape', 'Flamingo', 'Banana', 'Tangerine', 'Peacock', 'Graphite', 'Blueberry', 'Basil', 'Tomato'],
                "name": "color",
            }
        ]

        color = promptpy(color)
        color = color["color"]

    date = convert_date(start)
    converted_start = convert_time(start)
    converted_end = convert_time(end)

    if confirm is None:
        console = Console()
        prompt_text = Text("Are you sure you want to create this event? (y/n) (" + converted_start + ' to ' + converted_end + ", " + date + " | " + summary + ")", style="bold green")
        console.print(prompt_text, end="")
        confirm = typer.prompt("")

    if confirm == "n":
        print("Event creation cancelled")
        return
    else:
        print("Creating an event")
        create_event(
            calendar_id, 
            summary if summary is None else summary, 
            color, 
            startTime, 
            endTime,
            isRecurring,
            days["days"] if isRecurring == "y" else None,
            endDate if isRecurring == "y" else None,
        )

@app.command()
def get(
    count: Annotated[str, typer.Argument(help="How many upcoming events do you want to get? 🔢", show_default=False)] = "1",
    table: Annotated[str, typer.Option(help="Display events in a table? [italic bold](y/n)[/italic bold] 📊", show_default="n")] = "n",
):
    """
    [yellow bold]Get[/yellow bold] the specified number of upcoming events. If no number is specified, gets the next event 📋
    """
    if count == '1':
        print("Getting the next event in your calendar")
    else:
        print(f"Getting the upcoming {count} events in your calendar")
    events = get_upcoming_events(calendar_id, count)
    if not events:
        print("No upcoming events found.")
    else:
        if table == "y":
            console = Console()
            tb = Table("Event", "Time", "Date")
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            end = event["end"].get("dateTime", event["end"].get("date"))
            date = convert_date(start)
            converted_start = convert_time(start)
            converted_end = convert_time(end)
            if table == "n":
                print(converted_start + ' to ' + converted_end + ", " + date + " | " + event["summary"])
            else:
                tb.add_row(event["summary"], converted_start + ' to ' + converted_end, date)
        if table == "y":
            console.print(tb)

@app.command()
def list_id(count: Annotated[str, typer.Argument(help="How many IDs do you want to list? 📋", show_default=False)] = "1"):
    """
    [yellow bold]List[/yellow bold] the ID's of the specified number of upcoming events. If no number is specified, gets the next event 🖊️
    """
    if count == '1':
        print("Getting the next event's ID in your calendar")
    else:
        print(f"Getting the upcoming {count} events' ID's in your calendar")
    events = get_upcoming_events(calendar_id, count)
    if not events:
        print("No upcoming events found.")
    else:
        for event in events:
            print("ID: " + event["id"] + " | " + event["summary"])

@app.command()
def delete(
    id: Annotated[str, typer.Argument(help="The ID of the event to be [red]deleted[/red] 🗑️", show_default=False)], 
    confirm: Annotated[str, typer.Option(help="Are you sure you want to delete this event? [italic bold](y/n)[/italic bold] :boom:", show_default=False)] = None
):
    """
    [red bold]Delete[/red bold] an event with the specified ID 🗑️
    """
    try:
        event = get_event_by_id(calendar_id, id)
        
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))

        date = convert_date(start)
        converted_start = convert_time(start)
        converted_end = convert_time(end)

        if confirm is None:
            console = Console()
            prompt_text = Text("Are you sure you want to delete this event? (y/n) (" + converted_start + ' to ' + converted_end + ", " + date + " | " + event["summary"] + ")", style="bold red")
            console.print(prompt_text, end="")
            confirm = typer.prompt("")

        if confirm == "n":
            print("Event deletion cancelled")
            return
        else:
            print("Deleting event")
            delete_event_by_id(calendar_id, id)
            print("Event deleted")
    except HttpError:
        print("No event found with specified ID")

@app.command()
def start():
    """
    [green bold]Start[/green bold] a timer for a quick event ⏱️
    """
    start_time = time.time()
    with open(start_time_file, 'w') as f:
        f.write(str(start_time))
    print("Timer started")

@app.command()
def stop(event: Annotated[str, typer.Argument(help="What quick event do you want to add? [bold italic](Work, Homework, Study, Exercise, Break, Appointment, Other)[/bold italic] 🗓️", metavar="✨EVENT✨", show_default=False)] = None):
    """
    [red bold]Stop[/red bold] the timer and add a quick event 📝
    """
    if not os.path.exists(start_time_file):
        print("Timer was never started")
        return
    else:
        with open(start_time_file, 'r') as f:
            start_time = float(f.read())
        os.remove(start_time_file)
        end_time = time.time()
        elapsed_time = int(end_time - start_time)
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        elapsed_time = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
        print("Elapsed time: " + elapsed_time)
    
    startTime, endTime = format_time(start_time, end_time)

    if event is None:   
        event = [
                {
                    "type": "fuzzy",
                    "message": "What is the event?",
                    "choices": ['Work', 'Homework', 'Study', 'Exercise', 'Break', 'Appointment', 'Other'],
                    "name": "event",
                }
            ]

        event = promptpy(event)
        event = event["event"]

    color_mapping = {
        "Work": "Lavendar",
        "Homework": "Sage",
        "Study": "Grape",
        "Exercise": "Flamingo",
        "Break": "Banana",
        "Appointment": "Tangerine",
        "Other": "Peacock",
    }

    color = color_mapping[event]

    create_event(
        calendar_id, 
        event, 
        color, 
        startTime, 
        endTime,
        "n",
        None,
        None,
    )

if __name__ == "__main__":
    app()