"""
Unit tests for the CLI module.
"""

import pytest
from io import StringIO
from unittest.mock import patch
from myapp.cli import create_parser, main


class TestCLI:
    """Test cases for CLI functionality."""

    def test_create_parser(self):
        """Test parser creation."""
        parser = create_parser()
        assert parser is not None

    def test_calc_add_command(self):
        """Test calculator add command."""
        with patch("sys.argv", ["cli.py", "calc", "add", "5", "3"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                main()
                output = mock_stdout.getvalue().strip()
                assert "Result: 8.0" in output

    def test_calc_divide_by_zero(self):
        """Test calculator divide by zero."""
        with patch("sys.argv", ["cli.py", "calc", "divide", "5", "0"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                with pytest.raises(SystemExit):
                    main()
                output = mock_stdout.getvalue().strip()
                assert "Error: Cannot divide by zero" in output

    def test_greet_command(self):
        """Test greet command."""
        with patch("sys.argv", ["cli.py", "greet", "--name", "Jenkins"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                main()
                output = mock_stdout.getvalue().strip()
                assert "Hello Jenkins from Jenkins Pipeline!" in output

    def test_greet_with_time(self):
        """Test greet command with time."""
        with patch("sys.argv", ["cli.py", "greet", "--name", "Test", "--time"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                main()
                output = mock_stdout.getvalue()
                assert "Hello Test from Jenkins Pipeline!" in output
                assert "Current time:" in output
