import pandas as pd

from src.transform.standardize import (
    normalize_document_type_value,
    normalize_document_number
)




def test_normalize_document_type_value():

    assert (
        normalize_document_type_value(
            "D.N.I."
        ) == "DNI"
    )

    assert (
        normalize_document_type_value(
            "pasaporte"
        ) == "PASAPORTE"
    )

    assert (
        normalize_document_type_value(
            None
        ) == "SIN_DATO"
    )

def test_normalize_document_number():

    df = pd.DataFrame({
        "document_number": [
            "12.345.678",
            " 20-12345678-9 ",
            None
        ]
    })

    normalized_df = (
        normalize_document_number(df)
    )

    result = (
        normalized_df["document_number"]
        .tolist()
    )

    assert result[0] == "12345678"

    assert result[1] == "20-12345678-9"

    assert pd.isna(result[2])