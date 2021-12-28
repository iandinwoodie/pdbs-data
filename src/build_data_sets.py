"""
Main script resposible for creating the project data sets.
"""
# Local modules.
import raw_data
import settings
import structured_data


def main() -> None:
    """
    Main function from which all data sets are created.
    """
    config = settings.Settings()

    # Fetch the raw data.
    print("Loading raw data ... ", end="")
    df_raw = raw_data.create_data_frame(config)
    if not raw_data.verify_data_frame(df_raw):
        raise ValueError("Raw data frame is not valid.")
    print("done")

    # Structure the raw data into an intuitive format.
    print("Creating structured data ... ", end="")
    df_structured = structured_data.create_data_frame(df_raw)
    if not structured_data.verify_data_frame(df_structured):
        raise ValueError("Structured data frame is not valid.")
    print("done")

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
