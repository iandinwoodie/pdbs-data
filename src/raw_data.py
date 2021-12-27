"""
Module for code related to the raw data set.
"""
# Standard library modules.
import pathlib

# Third party modules.
import pandas as pd


def get_path(data_dir: pathlib.Path) -> pathlib.Path:
    """Get the path to the raw data set."""
    return data_dir / "raw" / "raw.csv"


def verify_data_frame(df: pd.DataFrame) -> bool:
    """Verify the raw data frame."""
    return df.shape == (5115, 2443)


def create_data_frame(raw_data_path: pathlib.Path) -> pd.DataFrame:
    """Create the raw data frame."""
    return pd.read_csv(raw_data_path, dtype=object, low_memory=False).apply(
        pd.to_numeric, errors="ignore"
    )  # pylint: disable=no-member
