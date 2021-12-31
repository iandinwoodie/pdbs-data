"""
Integration tests for the trimmed_data module.
"""
# Standard library modules.
import hashlib

# Third party modules.
import pandas as pd

# Local modules.
from src import settings, raw_data, structured_data, trimmed_data


def test_create_data_frame__success():
    """Verify the shape and contents of the data frame."""
    df_raw = raw_data.create_data_frame(settings.Settings())
    df_structured = structured_data.create_data_frame(df_raw)
    df = trimmed_data.create_data_frame(df_structured)
    assert df.shape == (5057, 490)
    assert df.query("phase_2_complete == 2").shape == (2322, 490)
    digest = hashlib.sha1(pd.util.hash_pandas_object(df).values).hexdigest()
    assert digest == "e22d2784feaa49b8c391348f7d62c88ceaeaf28f"
