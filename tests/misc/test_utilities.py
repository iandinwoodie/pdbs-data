"""
Tests for utilities (e.g., linters, formatters, type checkers).
"""
# Standard library modules.
import pathlib
import subprocess


project_dir = pathlib.Path(__file__).parent.parent.parent


def test_files_pass_black_check():
    """Properly formatted source files should pass black."""
    cmd = ["python", "-m", "black", "--check", project_dir]
    p = subprocess.run(cmd, capture_output=True, check=False)
    assert p.returncode == 0


def test_files_pass_mypy_check():
    """Properly structured source files should pass mypy."""
    cmd = ["python", "-m", "mypy", "--ignore-missing-imports", project_dir]
    p = subprocess.run(cmd, capture_output=True, check=False)
    assert p.returncode == 0


def test_files_pass_pylint_check():
    """Properly structured source files should pass pylint."""
    cmd = ["python", "-m", "pylint", project_dir / "src", project_dir / "tests"]
    p = subprocess.run(cmd, capture_output=True, check=False)
    assert p.returncode == 0
