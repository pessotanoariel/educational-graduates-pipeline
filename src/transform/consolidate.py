import pandas as pd

def load_processed_datasets(processed_data_dir):
    """Load processed CSV datasets from processed data directory."""

    processed_paths = [
        path
        for path in processed_data_dir.iterdir()
        if path.name.endswith("_processed.csv")
    ]

    datasets = []

    for path in processed_paths:

        df = pd.read_csv(
            path,
            dtype=str,
            low_memory=False
        )

        df["source_file"] = path.name

        datasets.append(df)

    return datasets

def concatenate_datasets(datasets):
    """Concatenate processed datasets into unified dataframe."""

    unified_df = pd.concat(
        datasets,
        ignore_index=True
    )

    return unified_df

def remove_duplicate_records(df):
    """Remove duplicated records based on document identity."""

    deduplicated_df = df.drop_duplicates(
        subset=[
            "document_type",
            "document_number"
        ]
    )

    return deduplicated_df