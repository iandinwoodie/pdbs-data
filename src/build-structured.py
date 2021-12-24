import pathlib
import pandas as pd

import structured


def main():
    project_dir = pathlib.Path(__file__).parent.parent
    data_dir = project_dir / "data"
    raw_data_path = data_dir / "raw" / "raw.csv"
    if not raw_data_path.exists():
        raise FileNotFoundError(f"{raw_data_path} does not exist.")
    df = process_raw_data(raw_data_path)
    assert df.shape == (8378, 496)
    structured_data_path = data_dir / "intermediate" / "structured.csv"
    df.to_csv(structured_data_path, index=False)
    print(f"Structured data saved to {structured_data_path}.")


def process_raw_data(raw_data_path):
    df = pd.read_csv(raw_data_path, dtype=object, low_memory=False)
    assert df.shape == (5115, 2443)
    df = df.apply(pd.to_numeric, errors="ignore")
    # Create two derived dataframes: one for owners and one for dogs.
    df_owner = structured.extract_owner_dataframe(df)
    assert df_owner.shape == (5115, 11)
    df_dog = create_dog_dataframe(df)
    # Owners were only allowed to input data for 5 dogs at a time (due to
    # constraints imposed by the version of REDCap being utilized to serve the
    # survey. As a result, our owner dataframe may include duplicate entries,
    # but each with a different record_id. The record_id is what ties a dog to
    # its owner. If we want to squash duplicate owner entries, then we will need
    # to create a new link between owners and dogs. We introduce a new owner_id
    # column to accomplish this.
    id_dict = generate_owner_id_dict(df_owner)
    # assert len(id_dict) == 3198
    # We then apply the mapping to the two dataframes to be linked.
    df_owner = structured.add_owner_id_col(df_owner, id_dict)
    df_dog = structured.add_owner_id_col(df_dog, id_dict)
    # Retain information about owners that actually completed the initial owner
    # (i.e., registration) survey.
    df_owner = df_owner.loc[df_owner["phase_1_welcome_complete"] == 2]
    assert df_owner.shape == (3308, 12)
    # Now we can drop duplicate owner and dog entries, keeping the most recent
    # submission.
    df_owner = df_owner.drop_duplicates(subset=["owner_id"], keep="last")
    df_owner = df_owner.drop(columns=["record_id"])  # Drop due to redundancy.
    df_dog = df_dog.drop_duplicates(subset=["owner_id", "dog_name"], keep="last")
    return pd.merge(df_owner, df_dog, on="owner_id")


def create_dog_dataframe(frame):
    def create_event_1_slices(frame):
        id_ = ["record_id"]
        cols = id_ + list(frame.loc[:, "dog_name_1a":"phase_1e_complete"])
        df = frame.query("redcap_event_name == 'event_1_arm_1'")[cols]
        # Drop the repeat column since they were for control flow logic only.
        df = df[df.columns.drop(list(df.filter(regex=r"phase_1_repeat_1[a-e]")))]
        slices = []
        beg = "dog_name_1{}"
        end = "phase_1{}_complete"
        for i in ["a", "b", "c", "d", "e"]:
            s = df[id_ + list(df.loc[:, beg.format(i) : end.format(i)])]
            s.columns = s.columns.str.replace(
                r"phase_1[a-e]_complete", "phase_1_complete", regex=True
            )
            s.columns = s.columns.str.replace(r"_1[a-e]", "", regex=True)
            s.columns = s.columns.str.replace("___", "_")
            slices.append(s)
        return slices

    def create_event_2_slices(frame):
        id_ = ["record_id"]
        cols = id_ + list(frame.loc[:, "prof_help_2a":"phase_2e_complete"])
        df = frame.query("redcap_event_name == 'event_2_arm_1'")[cols]
        slices = []
        beg = "prof_help_2{}"
        end = "phase_2{}_complete"
        for i in ["a", "b", "c", "d", "e"]:
            s = df[id_ + list(df.loc[:, beg.format(i) : end.format(i)])]
            s.columns = s.columns.str.replace(
                r"phase_2[a-e]_complete", "phase_2_complete", regex=True
            )
            s.columns = s.columns.str.replace(r"_2[a-e]", "", regex=True)
            s.columns = s.columns.str.replace("___", "_")
            slices.append(s)
        return slices

    e1_slices = create_event_1_slices(frame)
    assert [x.shape[0] for x in e1_slices] == [3392, 3392, 3392, 3392, 3392]
    e2_slices = create_event_2_slices(frame)
    assert [x.shape[0] for x in e2_slices] == [1723, 1723, 1723, 1723, 1723]
    slices = []
    for i in range(len(e1_slices)):
        s = pd.merge(e1_slices[i], e2_slices[i], on="record_id", how="left")
        slices.append(s)
    assert [x.shape[0] for x in slices] == [3392, 3392, 3392, 3392, 3392]
    return pd.concat(slices)


def generate_owner_id_dict(frame):
    email_dict = {}  # key = email, value = owner_id
    owner_id_dict = {}  # key = owner_id, value = [record_id, ...]
    next_owner_id = 1
    for index, owner in frame.iterrows():
        email = owner.email
        owner_id = None
        if not email in email_dict.keys():
            owner_id = next_owner_id
            next_owner_id += 1
            email_dict[email] = owner_id
        else:
            owner_id = email_dict[email]
        assert owner_id  # sanity check
        record_ids = None
        if not owner_id in owner_id_dict.keys():
            owner_id_dict[owner_id] = []
            record_ids = []
        else:
            record_ids = owner_id_dict[owner_id]
        assert record_ids is not None  # sanity check
        record_ids.append(owner.record_id)
        owner_id_dict[owner_id] = record_ids
    return owner_id_dict


if __name__ == "__main__":
    main()
