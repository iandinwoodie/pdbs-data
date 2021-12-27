"""
Module for code related to the structured data set.
"""
# Standard library modules.
import pathlib

# Third party modules.
import numpy as np
import pandas as pd


def get_path(data_dir: pathlib.Path) -> pathlib.Path:
    """Return the path to the structured data set."""
    return data_dir / "intermediate" / "structured_data.csv"


def extract_event_1(df: pd.DataFrame) -> pd.DataFrame:
    """Return the event 1 data frame."""
    df_e1 = df.query("redcap_event_name == 'event_1_arm_1'")
    assert df_e1.shape == (3392, 2443)

    # Drop the columns that are not needed for event 1.
    def drop_other_event_columns(df: pd.DataFrame) -> pd.DataFrame:
        """Drop columns that are not needed for event 1."""
        idx1 = df.columns.get_loc("record_id")
        idx2 = df.columns.get_loc("phase_1_feedback_complete") + 1
        return df.iloc[:, idx1:idx2]

    df_e1 = drop_other_event_columns(df_e1)
    assert df_e1.shape == (3392, 689)

    # Separate out the A-E phases.
    def get_phase_columns(df: pd.DataFrame, phase: str) -> pd.DataFrame:
        """Return the event 2 data frame."""
        range_ = np.r_[
            df_e1.columns.get_loc("record_id") : df_e1.columns.get_loc(
                "phase_1_welcome_complete"
            )
            + 1,
            df_e1.columns.get_loc(f"dog_name_1{phase}") : df_e1.columns.get_loc(
                f"phase_1{phase}_complete"
            )
            + 1,
        ]
        df = df.iloc[:, range_]
        if phase != "e":
            df = df.drop(columns=[f"phase_1_repeat_1{phase}"])
        df = df.drop(columns=["redcap_event_name"])
        df.columns = df.columns.str.replace(
            r"phase_1[a-e]_complete", "phase_1_complete", regex=True
        )
        df.columns = df.columns.str.replace(r"_[1-2][a-e]", "", regex=True)
        df.columns = df.columns.str.replace("___", "_")
        return df

    e1_df_list = []
    df_e1_a = get_phase_columns(df_e1, "a")
    assert df_e1_a.shape == (3392, 144)
    assert df_e1_a.query("phase_1_complete == 2").shape == (3027, 144)
    e1_df_list.append(df_e1_a)
    df_e1_b = get_phase_columns(df_e1, "b")
    assert df_e1_b.shape == (3392, 144)
    assert df_e1_b.query("phase_1_complete == 2").shape == (1375, 144)
    e1_df_list.append(df_e1_b)

    df_e1_c = get_phase_columns(df_e1, "c")
    assert df_e1_c.shape == (3392, 144)
    assert df_e1_c.query("phase_1_complete == 2").shape == (442, 144)
    e1_df_list.append(df_e1_c)

    df_e1_d = get_phase_columns(df_e1, "d")
    assert df_e1_d.shape == (3392, 144)
    assert df_e1_d.query("phase_1_complete == 2").shape == (153, 144)
    e1_df_list.append(df_e1_d)

    df_e1_e = get_phase_columns(df_e1, "e")
    assert df_e1_e.shape == (3392, 144)
    assert df_e1_e.query("phase_1_complete == 2").shape == (60, 144)
    e1_df_list.append(df_e1_e)

    assert len(e1_df_list) == 5
    return e1_df_list


def extract_event_2(df: pd.DataFrame) -> pd.DataFrame:
    """Return the event 2 data frame."""
    df_e2 = df.query("redcap_event_name == 'event_2_arm_1'")
    assert df_e2.shape == (1723, 2443)

    # Drop the columns that are not needed for event 2.
    def drop_other_event_columns(df: pd.DataFrame) -> pd.DataFrame:
        """Drop columns that are not needed for event 2."""
        idx1 = df.columns.get_loc("record_id")
        idx2 = df.columns.get_loc("redcap_event_name") + 1
        idx3 = df.columns.get_loc("phase_2_welcome_complete")
        idx4 = df.columns.get_loc("phase_2_feedback_complete") + 1
        return df.iloc[:, np.r_[idx1:idx2, idx3:idx4]]

    df_e2 = drop_other_event_columns(df_e2)
    assert df_e2.shape == (1723, 1756)

    # Separate out the A-E phases.
    def get_phase_columns(df: pd.DataFrame, phase: str) -> pd.DataFrame:
        """Return the columns for the given phase."""
        range_ = np.r_[
            df.columns.get_loc("record_id") : df.columns.get_loc("redcap_event_name")
            + 1,
            df.columns.get_loc("phase_2_welcome_complete"),
            df.columns.get_loc(f"prof_help_2{phase}") : df.columns.get_loc(
                f"phase_2{phase}_complete"
            )
            + 1,
            df.columns.get_loc("feedback_length_2") : df.columns.get_loc(
                "phase_2_feedback_complete"
            )
            + 1,
        ]
        df = df.iloc[:, range_]
        df = df.drop(columns=["redcap_event_name"])
        df.columns = df.columns.str.replace(
            r"phase_2[a-e]_complete", "phase_2_complete", regex=True
        )
        df.columns = df.columns.str.replace(r"_[1-2][a-e]", "", regex=True)
        df.columns = df.columns.str.replace("___", "_")
        return df

    e2_df_list = []
    df_e2_a = get_phase_columns(df_e2, "a")
    assert df_e2_a.shape == (1723, 355)
    assert df_e2_a.query("phase_2_complete == 2").shape == (1423, 355)
    e2_df_list.append(df_e2_a)

    df_e2_b = get_phase_columns(df_e2, "b")
    assert df_e2_b.shape == (1723, 355)
    assert df_e2_b.query("phase_2_complete == 2").shape == (634, 355)
    e2_df_list.append(df_e2_b)

    df_e2_c = get_phase_columns(df_e2, "c")
    assert df_e2_c.shape == (1723, 355)
    assert df_e2_c.query("phase_2_complete == 2").shape == (181, 355)
    e2_df_list.append(df_e2_c)

    df_e2_d = get_phase_columns(df_e2, "d")
    assert df_e2_d.shape == (1723, 355)
    assert df_e2_d.query("phase_2_complete == 2").shape == (65, 355)
    e2_df_list.append(df_e2_d)

    df_e2_e = get_phase_columns(df_e2, "e")
    assert df_e2_e.shape == (1723, 355)
    assert df_e2_e.query("phase_2_complete == 2").shape == (19, 355)
    e2_df_list.append(df_e2_e)

    assert len(e2_df_list) == 5
    return e2_df_list


def create_data_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Create the structured data frame."""
    # Data can be first be partitioned by event.
    e1_df_list = extract_event_1(df)
    e2_df_list = extract_event_2(df)
    # Then form complete entries by combining the event data frames.
    df_struct = None
    for idx, df_e1 in enumerate(e1_df_list):
        df_e2 = e2_df_list[idx]
        df_tmp = pd.concat([df_e1, df_e2], axis=1)
        df_struct = pd.concat([df_struct, df_tmp]) if df_struct is not None else df_tmp
    return df_struct


def verify_data_frame(df: pd.DataFrame) -> None:
    """Verify the structured data frame."""
    return (
        df.shape == (25575, 499)
        and df.query("phase_1_complete == 2").shape == (5057, 499)
        and df.query("phase_2_complete == 2").shape == (2322, 499)
    )
