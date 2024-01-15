# googleCal.cli

googleCal.cli is a command-line interface tool built with Python3, Pytest, Typer, Google client library, and the Google Calendar API. It's designed to automate procedures and manage Google Calendar events.

## Features

- **Create, read, update, and delete** Google Calendar events 📅
- **List** upcoming events 🖊️
- **Support** for recurring events ✅
- **Display** events in a table format 📋
- **Start** a timer for a quick event ⏱️ 

## Requirements
Python 3.6+

## Installation

#### Step 1:
Clone the repository and install the dependencies:

```bash
git clone https://github.com/aandrewchen/googleCal.cli.git
cd googleCal.cli
pip install -r requirements.txt
```

#### Step 2:
Create a Google Cloud project! Go to "Credentials" > "Create Credentials" > "OAuth client ID" (please select "Desktop app")

Download the ```credentials.json``` file and place it in the same directory as googleCal.cli!

#### Step 3:
Head over to your Google Calendar and find the calendar you want to manage!

Click on the three buttons on the side and go to "Settings and Sharing" > "Integrate calendar" > "Calendar ID" (it should end in @group.calendar.google.com).

Create a ```.env ``` file with CALENDAR_ID="Calendar ID"

#### Step 4:
When you use googleCal.cli for the first time, the CLI will ask you to allow the application to access your Google Calendar. **After that, you can start automating and managing your Google Calendar 📅 !**

## Usage
You can use the `--help` flag with any command to get information about how to use it.

![Screenshot 2024-01-14 at 3 11 58 AM](https://github.com/aandrewchen/googleCal.cli/assets/125727520/0561c821-0f16-48e3-a9b2-3e30c7f5a5ab)

### Here are some examples of how to use googleCal.cli:

#### Get the next 3 events and display them in a table
```bash
python cli.py get 3 --table y
```
![Screenshot 2024-01-14 at 3 09 31 AM](https://github.com/aandrewchen/googleCal.cli/assets/125727520/2029d77c-008c-47e0-aa1b-8a0bcad53eb1)

#### Create a new event
```bash
python cli.py create
```
![Kapture 2024-01-14 at 22 36 35](https://github.com/aandrewchen/googleCal.cli/assets/125727520/80f6e414-73ff-4126-a218-b6f7cd00848c)

Here is how to create that same event with arguments:
```bash
python cli.py create --summary "Dentist Appointment" --isrecurring n --date 2024-01-17 --start 11:00 --end 12:00 --color Peacock --confirm y
```

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
![Screenshot 2024-01-14 at 3 24 58 AM](https://github.com/aandrewchen/googleCal.cli/assets/125727520/ecf5a6f7-1348-409e-9a85-95d4549639a3)

#### Start a timer for a quick event
```bash
python cli.py start
```

#### Stop timer
```bash
python cli.py stop
```
![Screenshot 2024-01-14 at 11 15 51 PM](https://github.com/aandrewchen/googleCal.cli/assets/125727520/b0d10c1e-bfbe-49ce-9be9-663a6b3a2256)

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
