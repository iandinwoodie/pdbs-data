"""
Module for code related to the trimmed data set.
"""
# Third party modules.
import pandas as pd


def create_data_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Create the trimmed data frame."""
    drop_cols = []
    # Drop responses where the welcome page was not completed.
    col = "phase_1_welcome_complete"
    df_trimmed = df.loc[df[col] == 2]
    drop_cols.append(col)
    # Drop responses where the first phase was not completed.
    col = "phase_1_complete"
    df_trimmed = df.loc[df[col] == 2]
    drop_cols.append(col)
    # Survey branching logic used for EDC platform.
    drop_cols.extend(
        [
            "phase_1_test",
            "q02_score",
            "q03_count",
            "q04_count",
            "phase_2_welcome_complete",
            "phase_2_feedback_complete",
        ]
    )
    df_trimmed = df_trimmed.drop(drop_cols, axis=1)
    return df_trimmed
