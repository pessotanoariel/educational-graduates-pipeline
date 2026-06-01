import pandas as pd

from src.transform.consolidate import (
    remove_duplicate_records
)


def test_remove_duplicate_records():

    df = pd.DataFrame({
        "document_type": [
            "DNI",
            "DNI"
        ],
        "document_number": [
            "12345678",
            "12345678"
        ],
        "source_priority": [
            1,
            3
        ]
    })

    result = remove_duplicate_records(
        df
    )

    assert len(result) == 1

    assert (
        result.iloc[0]["source_priority"]
        == 1
    )