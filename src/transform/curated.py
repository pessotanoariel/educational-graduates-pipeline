import pandas as pd
from datetime import datetime

def build_curated_dataset(df):
    """Build analytics-ready curated dataset."""

    curated_columns = [
        "document_type",
        "document_number",
        "full_name",
        "gender",
        "birth_date",
        "nationality",
        "email",
        "phone_number",
        "offer",
        "offer_type",
        "institution_name",
        "education_sector",
        "academic_year",
        "academic_period",
        "source_file"
    ]

    curated_df = df[
        curated_columns
    ].copy()

    return curated_df

def add_derived_attributes(df):
    """Add analytical derived attributes."""

    derived_df = df.copy()

    # ==============================
    # Contact Available
    # ==============================

    derived_df["contact_available"] = (
        derived_df["email"].notna()
        | derived_df["phone_number"].notna()
    )

    derived_df["contact_available"] = (
        derived_df["contact_available"]
        .map(
            {
                True: "YES",
                False: "NO"
            }
        )
    )

    # ==============================
    # Contact Completeness
    # ==============================

    conditions = [
        (
            derived_df["email"].notna()
            & derived_df["phone_number"].notna()
        ),
        (
            derived_df["email"].notna()
            & derived_df["phone_number"].isna()
        ),
        (
            derived_df["email"].isna()
            & derived_df["phone_number"].notna()
        )
    ]

    values = [
        "EMAIL_AND_PHONE",
        "EMAIL_ONLY",
        "PHONE_ONLY"
    ]

    derived_df["contact_completeness"] = (
        pd.Series(
            pd.NA,
            index=derived_df.index
        )
    )

    for condition, value in zip(
        conditions,
        values
    ):
        derived_df.loc[
            condition,
            "contact_completeness"
        ] = value

    derived_df["contact_completeness"] = (
        derived_df["contact_completeness"]
        .fillna("NO_CONTACT")
    )

    return derived_df