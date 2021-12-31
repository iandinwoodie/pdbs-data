"""
Unit tests for the settings module.
"""
# Standard library modules.
import pathlib

# Local modules.
from src import settings


# Global Settings object for testing.
config = settings.Settings()
# Helper variables to simplify assertions.
project_dir = pathlib.Path(__file__).parent.parent.parent
data_dir = project_dir / "data"
raw_data_dir = data_dir / "raw"
intermediate_data_dir = data_dir / "intermediate"


def test_settings__project_dir():
    """Test the project_dir property."""
    assert config.project_dir == project_dir


def test_settings__data_dir():
    """Test the data_dir property."""
    assert config.data_dir == data_dir


def test_settings__raw_data_dir():
    """Test the raw_data_dir property."""
    assert config.raw_data_dir == raw_data_dir


def test_settings__raw_data_path():
    """Test the raw_data_path property."""
    assert config.raw_data_path == raw_data_dir / "raw.csv"


def test_settings__intermediate_data_dir():
    """Test the intermediate_data_dir property."""
    assert config.intermediate_data_dir == intermediate_data_dir


def test_settings__structued_data_path():
    """Test the structued_data_path property."""
    assert config.structured_data_path == intermediate_data_dir / "structured.csv"
