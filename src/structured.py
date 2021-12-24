import numpy as np


def add_owner_id_col(frame, owner_id_dict):
    """
    Add a column to the frame with the owner_id of the owner of the
    corresponding row.
    """
    if not owner_id_dict:
        raise RuntimeError("owner_id_dict is empty")
    elif not "record_id" in frame.columns:
        raise RuntimeError("missing record_id column")
    frame["owner_id"] = np.nan
    for key, vals in owner_id_dict.items():
        frame.loc[frame["record_id"].isin(vals), "owner_id"] = key
    if frame["owner_id"].isnull().values.any():
        raise RuntimeError("owner_id was not fully populated")
    return frame
