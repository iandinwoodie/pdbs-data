"""
Integration tests for the structured_data module.
"""
# Standard library modules.
import hashlib

# Third party modules.
import pandas as pd

# Local modules.
from src import settings, raw_data, structured_data


def test_create_data_frame():
    """Verify the shape and contents of the raw data frame."""
    df = structured_data.create_data_frame(
        raw_data.create_data_frame(settings.Settings())
    )
    assert df.shape == (25575, 499)
    assert df.query("phase_1_complete == 2").shape == (5057, 499)
    assert df.query("phase_2_complete == 2").shape == (2322, 499)
    digest = hashlib.sha1(pd.util.hash_pandas_object(df).values).hexdigest()
    assert digest == "4e4e9671f36806be9c6cd856290e5dc66512dc46"
