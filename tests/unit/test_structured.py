import pytest
import pandas as pd

from src import structured


def test_add_owner_id_col__empty_dict_throws():
    with pytest.raises(RuntimeError):
        structured.add_owner_id_col(
            pd.DataFrame({"record_id": [1, 2], "field_1": [3, 4]}), {}
        )


def test_add_owner_id_col__missing_record_id_column_throws():
    with pytest.raises(RuntimeError):
        structured.add_owner_id_col(
            pd.DataFrame({"field_1": [3, 4]}), {123: [1, 3], 456: [2]}
        )


def test_add_owner_id_col__missing_owner_id_value_throws():
    with pytest.raises(RuntimeError):
        structured.add_owner_id_col(
            pd.DataFrame({"record_id": [1, 2], "field_1": [3, 4]}), {123: [1, 3]}
        )


def test_add_owner_id_col__missing_record_id_value_succeeds():
    df_actual = structured.add_owner_id_col(
        pd.DataFrame({"record_id": [1, 2], "field_1": [3, 4]}), {123: [1, 3], 456: [2]}
    )
    df_expected = pd.DataFrame({"record_id": [1, 2], "field_1": [3, 4], "owner_id": [123.0, 456.0]})
    assert df_actual.equals(df_expected)


def test_add_owner_id_col__original_data_frame_is_modified():
    df_original = pd.DataFrame({"record_id": [1, 2], "field_1": [3, 4]})
    structured.add_owner_id_col(df_original, {123: [1], 456: [2]})
    df_expected = pd.DataFrame({"record_id": [1, 2], "field_1": [3, 4], "owner_id": [123.0, 456.0]})
    assert df_original.equals(df_expected)
