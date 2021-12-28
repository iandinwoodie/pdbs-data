"""
Module for settings.
"""
# Standard library modules.
import pathlib


class Settings:
    """Stores settings for the project."""

    def __init__(self):
        """Initialize the settings."""
        self._project_dir = pathlib.Path(__file__).parent.parent
        self._data_dir = self._project_dir / "data"
        self._raw_data_path = self._data_dir / "raw" / "raw.csv"
        self._structured_data_path = self._data_dir / "intermediate" / "structured.csv"

    @property
    def project_dir(self) -> pathlib.Path:
        """Return the root directory for this project."""
        return self._project_dir

    @property
    def raw_data_path(self) -> pathlib.Path:
        """Return the raw data path for this project."""
        return self._raw_data_path

    @property
    def structured_data_path(self) -> pathlib.Path:
        """Return the structured data path for this project."""
        return self._structured_data_path
