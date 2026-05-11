def check_null_values(df):
    """Return null value counts per column."""
    null_summary = (
        df.isnull()
        .sum()
        .sort_values(ascending=False)
    )

    return null_summary

def check_duplicate_rows(df):
    """Return the count of duplicate rows in the dataset."""
    duplicate_count = df.duplicated().sum()

    return duplicate_count

def check_document_length(
    df,
    document_column,
    document_type_column,
    valid_document_type="DNI",
    min_length=7
):

    filtered_df = df[
        df[document_type_column] == valid_document_type
    ]

    invalid_documents = filtered_df[
        filtered_df[document_column]
        .str.len() < min_length
    ]

    return invalid_documents