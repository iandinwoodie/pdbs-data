"""
Tests for the raw data set file.
"""
# Standard library modules.
import hashlib

# Third party modules.
import pandas as pd

# Local modules.
from src import settings


def test_raw_data_set_exists():
    """Raw data set should always exist."""
    assert settings.Settings().raw_data_path.exists()


def test_raw_data_set_shape():
    """Raw data set shape is known and should not change."""
    df = pd.read_csv(settings.Settings().raw_data_path, dtype=object, low_memory=False)
    assert df.shape == (5115, 2443)


def test_raw_data_set_integrity():
    """Raw data set contents are known and should not change."""
    df = pd.read_csv(settings.Settings().raw_data_path, dtype=object, low_memory=False)
    digest = hashlib.sha1(pd.util.hash_pandas_object(df).values).hexdigest()
    assert digest == "63b99da8323d072fe291ed511584634a7898aaf4"
