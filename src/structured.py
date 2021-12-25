# Standard library modules.
import typing

# Third party modules.
import numpy as np
import pandas as pd


def add_owner_id_col(
    df: pd.DataFrame, owner_id_dict: typing.Dict[int, typing.List[int]]
) -> None:
    """
    Add a column to the data frame with the owner_id of the owner of the
    corresponding row as determined by record_id.
    """
    if not owner_id_dict:
        raise RuntimeError("owner_id_dict argument is empty")
    elif df.empty:
        raise RuntimeError("df argument is empty")
    elif not "record_id" in df.columns:
        raise RuntimeError("df argument missing record_id column")
    elif not df["record_id"].dtype == int:
        raise RuntimeError("df record_id column must be int")
    elif "owner_id" in df.columns:
        raise RuntimeError("df argument already has owner_id column")
    df["owner_id"] = -1
    record_ids_from_df = set(df["record_id"].to_list())
    record_ids_from_owner_id_dict = set()
    for key, vals in owner_id_dict.items():
        record_ids_from_owner_id_dict.update(vals)
        df.loc[df["record_id"].isin(vals), "owner_id"] = int(key)
    if len(record_ids_from_df - record_ids_from_owner_id_dict) > 0:
        raise RuntimeError("owner_id_dict argument missing entries")
    elif len(record_ids_from_owner_id_dict - record_ids_from_df) > 0:
        raise RuntimeError("df argument missing record_id entries")


def extract_owner_data_frame(df):
    """
    Extract the owner data frame from the main data frame.
    """
    df = df.loc[:, "record_id":"phase_1_welcome_complete"]
    df.columns = df.columns.str.replace("___", "_")
    return df
