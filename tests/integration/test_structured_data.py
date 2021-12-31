"""
Integration tests for the structured_data module.
"""
# Standard library modules.
import hashlib

# Third party modules.
import pandas as pd

# Local modules.
from src import settings, raw_data, structured_data


def test_create_data_frame__success():
    """Verify the shape and contents of the data frame."""
    df = structured_data.create_data_frame(
        raw_data.create_data_frame(settings.Settings())
    )
    assert df.shape == (16960, 498)
    assert df.query("phase_1_complete == 2").shape == (5057, 498)
    assert df.query("phase_2_complete == 2").shape == (2322, 498)
    digest = hashlib.sha1(pd.util.hash_pandas_object(df).values).hexdigest()
    assert digest == "8a5a2192f215e1d28b812927e7dc767f43d53031"
