from typer.testing import CliRunner

from cli import app

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ["test"])
    assert result.exit_code == 0
    assert "Testing" in result.stdout

def test2_app():
    result = runner.invoke(app, ["create"])
    assert result.exit_code == 0
    assert "Creating an event" in result.stdout