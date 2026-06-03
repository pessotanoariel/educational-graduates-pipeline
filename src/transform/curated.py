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