from unittest.mock import patch
from cli import app
from typer.testing import CliRunner

runner = CliRunner()

@patch('cli.get_upcoming_events')
def test_get_command_no_events(mock_get_upcoming_events):
    mock_get_upcoming_events.return_value = []

    result = runner.invoke(app, ["get"])

    assert result.exit_code == 0
    assert "No upcoming events found." in result.stdout

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