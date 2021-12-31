"""
Integration tests for the raw_data module.
"""
# Standard library modules.
import hashlib

# Third party modules.
import pandas as pd

# Local modules.
from src import settings
from src import raw_data


def test_create_data_frame():
    """Verify the shape and contents of the raw data frame."""
    df = raw_data.create_data_frame(settings.Settings())
    assert df.shape == (5115, 2443)
    digest = hashlib.sha1(pd.util.hash_pandas_object(df).values).hexdigest()
    assert digest == "b8b7eb00f7f51945fe2f75a115b44da53a1f6385"
