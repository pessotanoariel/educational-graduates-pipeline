COLUMN_MAPPING = {
    "Tipo de documento": "tipo_doc_std",
    "tipo_doc": "tipo_doc_std",

    "Nro de documento": "nro_doc_std",
    "nro_doc": "nro_doc_std"
}

def normalize_column_names(df):
    """Normalize dataframe column names using mapping."""

    normalized_columns = {}

    for column in df.columns:

        normalized_columns[column] = COLUMN_MAPPING.get(
            column,
            column
        )

    df = df.rename(columns=normalized_columns)

    return df