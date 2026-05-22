from src.transform.mappings import COLUMN_MAPPINGS

def standardize_column_names(df):
    """Standardize dataframe column names."""

    standardized_df = df.rename(
        columns=COLUMN_MAPPINGS
    )

    return standardized_df

def normalize_document_type(df):
    """Normalize document type values."""

    if "document_type" in df.columns:

        df["document_type"] = (
            df["document_type"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

    return df

def normalize_document_number(df):
    """Normalize document number values."""

    if "document_number" in df.columns:

        df["document_number"] = (
            df["document_number"]
            .astype(str)
            .str.strip()
        )

    return df

def normalize_gender(df):
    """Normalize gender values."""

    if "gender" in df.columns:

        df["gender"] = (
            df["gender"]
            .astype(str)
            .str.strip()
            .str.lower()
        )

    return df