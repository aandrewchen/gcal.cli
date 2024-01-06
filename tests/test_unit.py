from typer.testing import CliRunner

from cli import app

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ["test"])
    assert result.exit_code == 0
    assert "Testing" in result.stdout

def test_get_command_no_number_specified():
    result = runner.invoke(app, ["get"])
    assert result.exit_code == 0
    assert "IET Work" in result.stdout

def test_get_command_5_specified():
    result = runner.invoke(app, ["get", "5"])
    assert result.exit_code == 0
    assert "IET Work" in result.stdout

def test_create_command_with_arguments_not_recurring():
    result = runner.invoke(app, ["create", "--summary", "Test", "--isrecurring", "n", "--date", "2025-01-06", "--start", "08:00", "--end", "12:00", "--color", "Lavendar"])
    assert result.exit_code == 0
    assert "Event created" in result.stdout

def test_create_command_with_arguments_recurring_one_day():
    result = runner.invoke(app, ["create", "--summary", "Test", "--isrecurring", "y", "--days", "Monday", "--enddate", "2025-01-06", "--date", "2024-01-08", "--start", "08:00", "--end", "12:00", "--color", "Banana"])
    assert result.exit_code == 0
    assert "Event created" in result.stdout

def test_create_command_with_arguments_recurring_multiple_days():
    result = runner.invoke(app, ["create", "--summary", "Test", "--isrecurring", "y", "--days", "Monday, Wednesday, Friday", "--enddate", "2025-01-06", "--date", "2024-01-08", "--start", "08:00", "--end", "12:00", "--color", "Basil"])
    assert result.exit_code == 0
    assert "Event created" in result.stdout

def test_create_command_with_arguments_recurring_multiple_days():
    result = runner.invoke(app, ["create", "--summary", "Test", "--isrecurring", "y", "--days", "Everyday", "--enddate", "2025-01-06", "--date", "2024-01-08", "--start", "08:00", "--end", "12:00", "--color", "Graphite"])
    assert result.exit_code == 0
    assert "Event created" in result.stdout