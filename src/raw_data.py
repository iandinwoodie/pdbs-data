"""
Module for code related to the raw data set.
"""
# Third party modules.
import pandas as pd

# Local modules.
import settings


def verify_data_frame(df: pd.DataFrame) -> bool:
    """Verify the raw data frame."""
    return df.shape == (5115, 2443)


def create_data_frame(config: settings.Settings) -> pd.DataFrame:
    """Create the raw data frame."""
    if not config.raw_data_file.exists():
        raise ValueError("Raw data file does not exist.")
    return pd.read_csv(config.raw_data_path, dtype=object, low_memory=False).apply(
        pd.to_numeric, errors="ignore"
    )  # pylint: disable=no-member
