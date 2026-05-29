import pandas as pd

from src.transform.source_priority import (
    SOURCE_PRIORITY
)

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
    """Remove duplicated records using source priority."""

    sorted_df = df.sort_values(
        by="source_priority"
    )

    deduplicated_df = sorted_df.drop_duplicates(
        subset=[
            "document_type",
            "document_number"
        ],
        keep="first"
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

def apply_source_priority(df):
    """Apply source priority rules."""

    df["source_priority"] = 999

    for source_name, priority in SOURCE_PRIORITY.items():

        mask = df["source_file"].str.contains(
            source_name,
            case=False,
            na=False
        )

        df.loc[
            mask,
            "source_priority"
        ] = priority

    return df

def detect_unmapped_sources(df):
    """Detect records without mapped source priority."""

    unmapped_df = df[
        df["source_priority"] == 999
    ]

    return unmapped_df

def consolidate_person_records(df):
    """Consolidate person records using field enrichment."""

    grouped_records = []

    grouped_df = df.groupby(
        [
            "document_type",
            "document_number"
        ],
        dropna=False
    )

    for _, group in grouped_df:

        sorted_group = group.sort_values(
            by="source_priority"
        )

        best_record = (
            sorted_group.iloc[0]
            .copy()
        )

        if pd.isna(best_record["email"]):

            available_emails = (
                sorted_group["email"]
                .dropna()
            )

            if len(available_emails) > 0:

                best_record["email"] = (
                    available_emails.iloc[0]
                )

        grouped_records.append(best_record)

    consolidated_df = pd.DataFrame(
        grouped_records
    )

    return consolidated_df

def enrich_email_fields(df, deduplicated_df):
    """Enrich missing email values."""

    email_df = (
        df[
            [
                "document_type",
                "document_number",
                "email",
                "source_priority"
            ]
        ]
        .dropna(subset=["email"])
        .sort_values(by="source_priority")
        .drop_duplicates(
            subset=[
                "document_type",
                "document_number"
            ],
            keep="first"
        )
    )

    deduplicated_df = deduplicated_df.merge(
        email_df[
            [
                "document_type",
                "document_number",
                "email"
            ]
        ],
        on=[
            "document_type",
            "document_number"
        ],
        how="left",
        suffixes=("", "_enriched")
    )

    deduplicated_df["email"] = (
        deduplicated_df["email"]
        .fillna(
            deduplicated_df["email_enriched"]
        )
    )

    deduplicated_df = deduplicated_df.drop(
        columns=["email_enriched"]
    )

    return deduplicated_df

def enrich_phone_fields(df, deduplicated_df):
    """Enrich missing phone number values."""

    phone_df = (
        df[
            [
                "document_type",
                "document_number",
                "phone_number",
                "source_priority"
            ]
        ]
        .dropna(subset=["phone_number"])
        .sort_values(by="source_priority")
        .drop_duplicates(
            subset=[
                "document_type",
                "document_number"
            ],
            keep="first"
        )
    )

    deduplicated_df = deduplicated_df.merge(
        phone_df[
            [
                "document_type",
                "document_number",
                "phone_number"
            ]
        ],
        on=[
            "document_type",
            "document_number"
        ],
        how="left",
        suffixes=("", "_enriched")
    )

    deduplicated_df["phone_number"] = (
        deduplicated_df["phone_number"]
        .fillna(
            deduplicated_df["phone_number_enriched"]
        )
    )

    deduplicated_df = deduplicated_df.drop(
        columns=["phone_number_enriched"]
    )

    return deduplicated_df

def enrich_nationality_fields(
    df,
    deduplicated_df
):
    """Enrich missing nationality values."""

    nationality_df = (
        df[
            [
                "document_type",
                "document_number",
                "nationality",
                "source_priority"
            ]
        ]
        .dropna(subset=["nationality"])
        .sort_values(by="source_priority")
        .drop_duplicates(
            subset=[
                "document_type",
                "document_number"
            ],
            keep="first"
        )
    )

    deduplicated_df = deduplicated_df.merge(
        nationality_df[
            [
                "document_type",
                "document_number",
                "nationality"
            ]
        ],
        on=[
            "document_type",
            "document_number"
        ],
        how="left",
        suffixes=("", "_enriched")
    )

    deduplicated_df["nationality"] = (
        deduplicated_df["nationality"]
        .fillna(
            deduplicated_df["nationality_enriched"]
        )
    )

    deduplicated_df = deduplicated_df.drop(
        columns=["nationality_enriched"]
    )

    return deduplicated_df