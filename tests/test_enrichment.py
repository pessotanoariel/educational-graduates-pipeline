import pandas as pd

from src.transform.consolidate import (
    enrich_email_fields
)


def test_enrich_email_fields():

    source_df = pd.DataFrame({
        "document_type": [
            "DNI",
            "DNI"
        ],
        "document_number": [
            "12345678",
            "12345678"
        ],
        "email": [
            None,
            "test@email.com"
        ],
        "source_priority": [
            1,
            3
        ]
    })

    deduplicated_df = pd.DataFrame({
        "document_type": [
            "DNI"
        ],
        "document_number": [
            "12345678"
        ],
        "email": [
            None
        ]
    })

    result = enrich_email_fields(
        source_df,
        deduplicated_df
    )

    assert (
        result.iloc[0]["email"]
        == "test@email.com"
    )