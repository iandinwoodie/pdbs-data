"""
Main script resposible for creating the project data sets.
"""
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

    # IRD TODO: Generate a readable data set.

    # IRD TODO: Generate a refined data set via OpenRefine.

    # IRD TODO: Append manually cleaned columns.

    # IRD TODO: Handle "other" columns.

    # IRD TODO: Save final processed data set.

    ## IRD NOTE: Demographic study
    # df = df_structured
    ## The following is the inclusion criteria.
    # df = df.loc[
    #    (df['question_reason_for_part_3'] == 0)
    #    | ((df['question_reason_for_part_3'] == 1)
    #        & (df['q01_main'] != 1))]
    ## Drop incomplete responses for the first event.
    # df = df.loc[df['phase_1_complete'] == 2]
    # df = df.drop(["phase_1_complete"], axis=1)
    # assert df.shape == (4150, 498)
    ## NOTE: All event 2 columns can be dropped for this study.

    ## IRD NOTE: Treatment studies
    # df = df_structured
    ## Drop incomplete responses for the second event.
    # df = df.loc[df['phase_2_complete'] == 2]
    # df = df.drop(["phase_1_complete", "phase_2_complete"], axis=1)
    # assert df.shape == (2322, 497)


if __name__ == "__main__":
    main()
