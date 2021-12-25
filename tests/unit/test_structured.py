import pytest
import pandas as pd

from src import structured


def test_add_owner_id_col__returns_none():
    """Returns none to indicate that the data frame argument was modified."""
    rv = structured.add_owner_id_col(pd.DataFrame({"record_id": [1]}), {100: [1]})
    assert rv is None


def test_add_owner_id_col__dict_arg_empty_throws():
    """Owner ID dictionary argument is invalid if it is empty."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(pd.DataFrame(), {})
    assert "owner_id_dict argument is empty" in str(excinfo.value)


def test_add_owner_id_col__dict_arg_invalid_owner_id_type_throws():
    """Owner ID dictionary argument must have int owner IDs."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(pd.DataFrame(), {"100": [1]})
    assert "owner_id_dict keys must be int" in str(excinfo.value)


def test_add_owner_id_col__dict_arg_invalid_record_id_container_type_throws():
    """Owner ID dictionary argument record IDs must be in list."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(pd.DataFrame(), {100: {1}})
    assert "owner_id_dict values must be list of int" in str(excinfo.value)


def test_add_owner_id_col__dict_arg_invalid_record_id_element_type_throws():
    """Owner ID dictionary argument record IDs must be int."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(pd.DataFrame(), {100: ["1"]})
    assert "owner_id_dict values must be list of int" in str(excinfo.value)


def test_add_owner_id_col__dict_arg_missing_entry_throws():
    """Owner ID dictionary argument is invalid if it is missing an entry."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(pd.DataFrame({"record_id": [1, 2]}), {100: [1]})
    assert "owner_id_dict argument missing entries" in str(excinfo.value)


def test_add_owner_id_col__dict_arg_is_not_modified():
    """Owner ID dictionary argument is not modified."""
    owner_id_dict = {100: [1]}
    structured.add_owner_id_col(pd.DataFrame({"record_id": [1]}), owner_id_dict)
    assert owner_id_dict == {100: [1]}


def test_add_owner_id_col__df_arg_empty_throws():
    """Data frame argument is invalid if it is empty."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(pd.DataFrame(), {100: [1]})
    assert "df argument is empty" in str(excinfo.value)


def test_add_owner_id_col__df_arg_missing_record_id_column_throws():
    """Data frame argument is required to have a record_id column."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(pd.DataFrame({"data": ["A"]}), {100: [1]})
    assert "df argument missing record_id column" in str(excinfo.value)


def test_add_owner_id_col__df_arg_existing_id_column_throws():
    """Data frame argument is required to not have an owner_id column."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(
            pd.DataFrame({"record_id": [1], "owner_id": [100]}), {100: [1]}
        )
    assert "df argument already has owner_id column" in str(excinfo.value)


def test_add_owner_id_col__df_arg_invalid_record_id_type_throws():
    """Data frame argument record IDs must be int."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(pd.DataFrame({"record_id": ["1"]}), {100: [1]})
    assert "df record_id column must be int" in str(excinfo.value)


def test_add_owner_id_col__df_arg_missing_record_id_entry_throws():
    """Owner ID dictionary is invalid if it is missing record_id entries."""
    with pytest.raises(RuntimeError) as excinfo:
        structured.add_owner_id_col(pd.DataFrame({"record_id": [1]}), {100: [1, 2]})
    assert "df argument missing record_id entries" in str(excinfo.value)


def test_add_owner_id_col__df_arg_is_modified():
    """Data frame argument is modified."""
    df_actual = pd.DataFrame({"record_id": [1, 2, 3]})
    structured.add_owner_id_col(df_actual, {100: [1, 3], 200: [2]})
    assert df_actual.equals(
        pd.DataFrame({"record_id": [1, 2, 3], "owner_id": [100, 200, 100]})
    )
