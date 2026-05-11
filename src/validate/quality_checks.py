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