# googleCal.cli

gcal.cli is a command-line interface tool built with Python3, Pytest, Typer, and the Google Calendar API. It's designed to automate procedures and manage Google Calendar events.

## Features

- **Create, read, update, and delete** Google Calendar events 📅
- **List** upcoming events 🖊️
- **Support** for recurring events ✅
- **Display** events in a table format 📋
- **Start** a timer for a quick event ⏱️ 

## Installation

#### Step 1:
Clone the repository and install the dependencies:

```bash
git clone https://github.com/aandrewchen/gcal.cli.git
cd gcal.cli
pip install -r requirements.txt
```

#### Step 2:
Head over to your Google Calendar and find the calendar you want to manage!

Click on the three buttons on the side and go to "Settings and Sharing" > "Integrate calendar" > "Calendar ID" (it should end in @group.calendar.google.com).

Create a ```.env ``` file with CALENDAR_ID="Calendar ID"

#### Step 3:
When you use googleCal.cli for the first time, the CLI will ask you to allow the application to access your Google Calendar. After that, you can start automating and managing your Google Calendar!

## Usage
You can use the `--help` flag with any command to get information about how to use it.
![Screenshot 2024-01-14 at 3 11 58 AM](https://github.com/aandrewchen/gcal.cli/assets/125727520/0369b174-f370-4634-8ba2-426b77185991)

### Here are some examples of how to use gcal.cli:

#### Get the next 3 events and display them in a table
```bash
python cli.py get 3 --table y
```
![Screenshot 2024-01-14 at 3 09 31 AM](https://github.com/aandrewchen/gcal.cli/assets/125727520/211789ec-b5a7-4c59-b4e8-650c653479f1)

#### Create a new event
```bash
python cli.py create
```
![Kapture 2024-01-14 at 22 36 35](https://github.com/aandrewchen/googleCal.cli/assets/125727520/80f6e414-73ff-4126-a218-b6f7cd00848c)

#### List ID of the next event in your calendar
*Optionally include count to get the specified number of upcoming events*
```bash
python cli.py list-id <count>
```

#### Delete an event by ID
*Replace required id with the ID of the event you want to delete*
```bash
python cli.py delete <id>
```
![Screenshot 2024-01-14 at 3 24 58 AM](https://github.com/aandrewchen/gcal.cli/assets/125727520/37438305-0044-4f4a-99c2-27bc9e41dabc)

#### Start a timer for a quick event
```bash
python cli.py start
```

#### Stop timer
```bash
python cli.py stop
```

## Testing
You can run the tests with Pytest:
```bash
pytest
```
To see test converage, run:
```bash
coverage run -m pytest
```

## Contributing
Contributions are welcome! Please create a new issue if you find a bug or have a feature request. If you want to contribute code, please fork the repository and create a pull request.
