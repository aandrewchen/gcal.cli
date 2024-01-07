from unittest.mock import patch
from cli import app
from typer.testing import CliRunner
import cli
import unittest.mock
import time

runner = CliRunner()

def mock_get_auth():
    pass

@patch('cli.get_auth', new=mock_get_auth)
@patch('cli.get_upcoming_events')
def test_get_command_no_events(mock_get_upcoming_events):
    mock_get_upcoming_events.return_value = []

    result = runner.invoke(app, ["get"])

    assert result.exit_code == 0
    assert "No upcoming events found." in result.stdout

@patch('cli.get_auth', new=mock_get_auth)
@patch('cli.get_upcoming_events')
def test_get_command_one_event(mock_get_upcoming_events):
    mock_get_upcoming_events.return_value = [
        {
            'summary': 'Test',
            'start': {'dateTime': '2022-01-01T09:00:00'},
            'end': {'dateTime': '2022-01-01T10:00:00'},
        },
    ]

    result = runner.invoke(app, ["get"])

    assert result.exit_code == 0
    assert "Test" in result.stdout

@patch('cli.get_auth', new=mock_get_auth)
@patch('cli.create_event')
def test_create_command(mock_create_event):
    mock_create_event.return_value = None

    result = runner.invoke(app, ["create", "--summary", "Test", "--isrecurring", "n", "--date", "2025-01-06", "--start", "08:00", "--end", "12:00", "--color", "Lavendar", "--confirm", "y"])

    assert result.exit_code == 0
    assert "Creating an event" in result.stdout
    assert "Event created" in result.stdout

@patch('cli.get_auth', new=mock_get_auth)
@patch('cli.create_event')
def test_create_command(mock_create_event):
    mock_create_event.return_value = None

    result = runner.invoke(app, ["create", "--summary", "Test", "--isrecurring", "n", "--date", "2025-01-06", "--start", "10:00", "--end", "15:00", "--color", "Peacock", "--confirm", "n"])

    assert result.exit_code == 0
    assert "Event creation cancelled" in result.stdout

@patch('cli.get_auth', new=mock_get_auth)
@patch('cli.get_upcoming_events')
def test_listid_command(mock_get_upcoming_events):
    mock_get_upcoming_events.return_value = []

    result = runner.invoke(app, ["list-id"])

    assert result.exit_code == 0
    assert "Getting the next event's ID in your calendar" in result.stdout
    assert "No upcoming events found." in result.stdout

@patch('cli.get_auth', new=mock_get_auth)
@patch('cli.get_upcoming_events')
def test_listid_command_3_events(mock_get_upcoming_events):
    mock_get_upcoming_events.return_value = [
        {
            'summary': 'Test',
            'id': '1',
        },
        {
            'summary': 'Test 2',
            'id': '2',
        },
        {
            'summary': 'Test 3',
            'id': '3',
        },
    ]

    result = runner.invoke(app, ["list-id", "3"])

    assert result.exit_code == 0
    assert "Getting the upcoming 3 events' ID's in your calendar" in result.stdout
    assert "ID: 1 | Test" in result.stdout
    assert "ID: 2 | Test 2" in result.stdout
    assert "ID: 3 | Test 3" in result.stdout