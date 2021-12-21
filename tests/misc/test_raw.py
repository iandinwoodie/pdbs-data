import pytest
import pandas as pd
import pathlib
import hashlib

project_dir = pathlib.Path(__file__).parent.parent.parent
raw_data_path = project_dir / "data" / "raw" / "raw.csv"


def test_raw_data_set_exists():
    assert raw_data_path.exists()


def test_raw_data_set_shape():
    df = pd.read_csv(raw_data_path, dtype=object, low_memory=False)
    assert df.shape == (5115, 2443)


def test_raw_data_set_integrity():
    df = pd.read_csv(raw_data_path, dtype=object, low_memory=False)
    digest = hashlib.sha1(pd.util.hash_pandas_object(df).values).hexdigest()
    assert digest == "63b99da8323d072fe291ed511584634a7898aaf4"
