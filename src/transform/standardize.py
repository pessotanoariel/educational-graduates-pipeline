from src.transform.mappings import (
    COLUMN_MAPPINGS,
    GENDER_MAPPING
)
import pandas as pd

def standardize_column_names(df):
    """Standardize dataframe column names."""

    standardized_df = df.rename(
        columns=COLUMN_MAPPINGS
    )

    return standardized_df

def normalize_document_type_value(value):
    """Standardize a single document type value."""

    if pd.isna(value):
        return "SIN_DATO"

    value = str(value).strip().upper()

    value = (
        value.replace(".", "")
        .replace("Á", "A")
        .replace("É", "E")
        .replace("Í", "I")
        .replace("Ó", "O")
        .replace("Ú", "U")
    )

    # ==============================
    # Missing / Invalid Values
    # ==============================

    if value in [
        "",
        "NAN",
        "SIN DATOS",
        "SIN_DATO",
        "SIN DOCUMENTO",
        "NO POSEE",
        "SIN ASIGNAR",
        "NO IDENTIFICADO",
        "EN TRAMITE"
    ]:
        return "SIN_DATO"

    # ==============================
    # DNI Variants
    # ==============================

    if value in [
        "DNI",
        "DNT",
        "DNX",
        "DNI EXTRANJERO",
        "DNI TEMPORAL"
    ]:
        return "DNI"

    # ==============================
    # Passport Variants
    # ==============================

    if value in [
        "PAS",
        "PASAPORTE",
        "PASAPORTE EXTRANJERO"
    ]:
        return "PASAPORTE"

    # ==============================
    # Identity Card Variants
    # ==============================

    if value in [
        "CI",
        "CEDULA DE IDENTIDAD",
        "CEDULA DE IDENTIDAD EXTRANJERO",
        "CI PY",
        "CI BO",
        "CI BR",
        "CI EXT",
        "CIEXT",
        "CE CL"
    ]:
        return "CI"

    # ==============================
    # Enrollment Booklet Variants
    # ==============================

    if value in [
        "LE",
        "LIBRETA DE ENROLAMIENTO"
    ]:
        return "LE"

    # ==============================
    # Civic Booklet Variants
    # ==============================

    if value in [
        "LC",
        "LIBRETA CIVICA"
    ]:
        return "LC"

    # ==============================
    # Other Document Types
    # ==============================

    if value in [
        "CUIL",
        "PRE",
        "PE",
        "CC",
        "CDI",
        "CM",
        "CREDENCIAL RESIDENCIA PRECARIA",
        "PARTIDA DE NACIMIENTO",
        "OTRO",
        "OTROS"
    ]:
        return "OTRO"

    return "OTRO"

def normalize_document_type(df):
    """Normalize document type values."""

    if "document_type" in df.columns:

        df["document_type"] = (
            df["document_type"]
            .apply(normalize_document_type_value)
        )

    return df

def normalize_document_number(df):
    """Clean and normalize document number values."""

    if "document_number" in df.columns:

        df["document_number"] = (
            df["document_number"]
            .astype(str)
            .str.strip()
            .str.replace(".", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.replace(" ", "", regex=False)
            .replace("nan", pd.NA)
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
            .map(GENDER_MAPPING)
        )

    return df

def normalize_text_value(value):
    """Normalize generic text values."""

    if pd.isna(value):
        return pd.NA

    value = str(value).strip()

    value = " ".join(value.split())

    if value == "":
        return pd.NA

    return value

def normalize_text_fields(df):
    """Normalize generic text fields."""

    text_columns = [
        "first_name",
        "last_name",
        "full_name",
        "offer",
        "institution_name"
    ]

    for column in text_columns:

        if column in df.columns:

            df[column] = (
                df[column]
                .apply(normalize_text_value)
            )

    return df