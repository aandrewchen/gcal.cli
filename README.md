# gcal.cli

gcal.cli is a command-line interface tool built with Python3, Pytest, Typer, and the Google Calendar API. It's designed to automate procedures and manage Google Calendar events.

## Features

- Create, read, update, and delete Google Calendar events.
- List upcoming events.
- Support for recurring events.
- Display events in a table format.
- Start a timer for a quick event.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/aandrewchen/gcal.cli.git
cd gcal.cli
pip install -r requirements.txt
```

## Usage
You can use the `--help` flag with any command to get information about how to use it.

### Here are some examples of how to use gcal.cli:

#### Get the next 3 events and display them in a table
```bash
python cli.py get 3 --table y
```

#### Create a new event
```bash
python cli.py create
```

#### Delete an event
```bash
python cli.py delete "id"
```
Replace "id" with the ID of the event you want to delete.

## Testing
You can run the tests with Pytest:
```bash
pytest
```

## Contributing
Contributions are welcome! Please create a new issue if you find a bug or have a feature request. If you want to contribute code, please fork the repository and create a pull request.
