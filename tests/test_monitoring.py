from pathlib import Path

import pandas as pd

from src.load.exporters import (
    append_dataframe
)


def test_append_dataframe(tmp_path):

    output_path = (
        tmp_path /
        "quality_history.csv"
    )

    first_df = pd.DataFrame([
        {
            "execution_date": "2026-06-01",
            "source_records": 100
        }
    ])

    second_df = pd.DataFrame([
        {
            "execution_date": "2026-06-08",
            "source_records": 120
        }
    ])

    append_dataframe(
        first_df,
        output_path
    )

    append_dataframe(
        second_df,
        output_path
    )

    result = pd.read_csv(
        output_path
    )

    assert len(result) == 2

    assert (
        result.iloc[0]["source_records"]
        == 100
    )

    assert (
        result.iloc[1]["source_records"]
        == 120
    )