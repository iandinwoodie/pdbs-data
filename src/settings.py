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

    @property
    def project_dir(self) -> pathlib.Path:
        """Return the path to the project root directory."""
        return self._project_dir

    @property
    def data_dir(self) -> pathlib.Path:
        """Return the path to the top-level data directory."""
        return self._project_dir / "data"

    @property
    def raw_data_dir(self) -> pathlib.Path:
        """Return the path to the raw data directory."""
        return self.data_dir / "raw"

    @property
    def raw_data_path(self) -> pathlib.Path:
        """Return the path to the raw data file."""
        return self.raw_data_dir / "raw.csv"

    @property
    def intermediate_data_dir(self) -> pathlib.Path:
        """Return the path to the intermediate data directory."""
        return self.data_dir / "intermediate"

    @property
    def structured_data_path(self) -> pathlib.Path:
        """Return the structured data path for this project."""
        return self.intermediate_data_dir / "structured.csv"
