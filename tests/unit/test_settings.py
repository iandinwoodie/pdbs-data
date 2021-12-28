"""
Unit tests for the settings module.
"""
# Standard library modules.
import pathlib

# Local modules.
from src import settings


project_dir = pathlib.Path(__file__).parent.parent.parent
data_dir = project_dir / "data"
intermediate_data_dir = data_dir / "intermediate"


def test_settings__project_dir():
    """Test the project_dir property."""
    assert settings.Settings().project_dir == project_dir


def test_settings__raw_data_path():
    """Test the raw_data_path property."""
    assert settings.Settings().raw_data_path == data_dir / "raw" / "raw.csv"


def test_settings__structued_data_path():
    """Test the structued_data_path property."""
    assert (
        settings.Settings().structured_data_path
        == intermediate_data_dir / "structured.csv"
    )
