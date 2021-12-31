"""
Module for code related to the raw data set.
"""
# Third party modules.
import pandas as pd

# Local modules.
import settings


def create_data_frame(config: settings.Settings) -> pd.DataFrame:
    """Create the raw data frame."""
    if not config.raw_data_path.exists():
        raise ValueError("Raw data file does not exist.")
    return pd.read_csv(config.raw_data_path, dtype=object, low_memory=False).apply(
        pd.to_numeric, errors="ignore"
    )  # pylint: disable=no-member
