# Standard library modules.
import pathlib
import subprocess

# Third party modules.
import pytest


project_dir = pathlib.Path(__file__).parent.parent.parent


def test_source_files_pass_mypy_check():
    """Properly structured source files should pass mypy."""
    cmd = ["python", "-m", "mypy", "--ignore-missing-imports", str(project_dir)]
    p = subprocess.run(cmd, capture_output=True)
    assert p.returncode == 0
