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

def validate_critical_fields(df):
    """Validate critical identity fields."""

    critical_fields = [
        "document_type",
        "document_number"
    ]

    validation_summary = {}

    for field in critical_fields:

        missing_count = (
            df[field]
            .isna()
            .sum()
        )

        validation_summary[field] = missing_count

    return validation_summary

def detect_missing_document_identities(df):
    """Return records with missing document identity."""

    missing_identity_df = df[
        (
            df["document_type"].isna()
        ) |
        (
            df["document_number"].isna()
        )
    ]

    return missing_identity_df

def analyze_null_distribution(df):
    """Analyze null distribution across dataframe columns."""

    null_summary_df = pd.DataFrame({
        "column_name": df.columns,
        "null_count": df.isna().sum().values,
        "null_percentage": (
            (
                df.isna().sum() / len(df)
            ) * 100
        ).round(2).values
    })

    return null_summary_df

def review_duplicated_records(df):
    """Review duplicated document identities."""

    duplicated_df = (
        df.groupby(
            [
                "document_type",
                "document_number"
            ]
        )
        .size()
        .reset_index(name="duplicate_count")
    )

    duplicated_df = duplicated_df[
        duplicated_df["duplicate_count"] > 1
    ]

    duplicated_df = duplicated_df.sort_values(
        by="duplicate_count",
        ascending=False
    )

    return duplicated_df