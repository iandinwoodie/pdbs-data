"""
Main script resposible for creating the project data sets.
"""
# Third party modules.
import pandas as pd

# Local modules.
import raw_data
import settings
import structured_data
import trimmed_data


def main() -> None:
    """
    Main function from which all data sets are created.
    """
    config = settings.Settings()

    # Fetch the raw data.
    print("Loading raw data ... ", end="")
    df_raw = raw_data.create_data_frame(config)
    print("done")

    # Structure the raw data into an intuitive format.
    print("Creating structured data ... ", end="")
    df_structured = structured_data.create_data_frame(df_raw)
    df_structured.to_csv(config.structured_data_path, index=False)
    print("done")

    # Trim the data set to include only the columns and rows that are useful for
    # investigation.
    print("Creating trimmed data ... ", end="")
    df_trimmed = trimmed_data.create_data_frame(df_structured)
    df_trimmed.to_csv(config.intermediate_data_dir / "trimmed.csv", index=False)
    print("done")
    assert df_trimmed.shape == (5057, 490)

    df_refined = pd.read_csv(
        config.intermediate_data_dir / "refined.csv", dtype=object, low_memory=False
    ).apply(pd.to_numeric, errors="ignore")
    assert df_refined.shape == (5057, 503)

    df_demo = create_demographics_data_frame(df_refined)
    assert df_demo.shape == (4150, 151)

    df_treat = create_treatment_data_frame(df_refined)
    assert df_treat.shape == (2322, 502)


def create_demographics_data_frame(df_refined: pd.DataFrame) -> pd.DataFrame:
    """
    Create a data frame containing only the demographic data.
    """
    df_demo = df_refined.copy()
    # The following is the inclusion criteria.
    df_demo = df_demo.loc[
        (df_demo["question_reason_for_part_3"] == 0)
        | ((df_demo["question_reason_for_part_3"] == 1) & (df_demo["q01_main"] != 1))
    ]
    cols = df_demo.columns.to_series()["prof_help":"feedback_extra_2"]  # type: ignore
    df_demo = df_demo.drop(cols, axis=1)
    return df_demo


def create_treatment_data_frame(df_refined: pd.DataFrame) -> pd.DataFrame:
    """
    Create a data frame containing only the treatment data.
    """
    df_treat = df_refined.copy()
    # Drop incomplete responses for the second event.
    df_treat = df_treat.loc[df_treat["phase_2_complete"] == 2]
    df_treat = df_treat.drop(["phase_2_complete"], axis=1)
    return df_treat


if __name__ == "__main__":
    main()
