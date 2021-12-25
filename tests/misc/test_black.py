# Standard library modules.
import pathlib
import subprocess

# Third party modules.
import pytest


project_dir = pathlib.Path(__file__).parent.parent.parent


def test_source_files_are_formatted_with_black():
    """Properly formatted source files should pass black."""
    cmd = ["python", "-m", "black", "--check", str(project_dir)]
    p = subprocess.run(cmd, capture_output=True)
    assert p.returncode == 0
