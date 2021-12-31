"""
Integration tests for the raw_data module.
"""
# Standard library modules.
import hashlib
import pathlib

# Third party modules.
import pandas as pd
import pytest

# Local modules.
from src import settings
from src import raw_data


def test_create_data_frame__success():
    """Verify the shape and contents of the data frame."""
    df = raw_data.create_data_frame(settings.Settings())
    assert df.shape == (5115, 2443)
    digest = hashlib.sha1(pd.util.hash_pandas_object(df).values).hexdigest()
    assert digest == "b8b7eb00f7f51945fe2f75a115b44da53a1f6385"


def test_create_data_frame__file_does_not_exist():
    """Verify behavior when the data file does not exist."""
    config = settings.Settings()
    # pylint: disable=protected-access
    config._project_dir = pathlib.Path("/tmp/does_not_exist")
    with pytest.raises(ValueError) as excinfo:
        raw_data.create_data_frame(config)
    assert "Raw data file does not exist." in str(excinfo.value)
