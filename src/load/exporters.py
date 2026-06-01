import pandas as pd

def export_dataframe(df, output_path):
    """Export dataframe to CSV file."""

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )

def append_dataframe(df, output_path):
    """Append dataframe to CSV file."""

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if output_path.exists():

        existing_df = pd.read_csv(
            output_path
        )

        updated_df = pd.concat(
            [existing_df, df],
            ignore_index=True
        )

        updated_df.to_csv(
            output_path,
            index=False,
            encoding="utf-8-sig"
        )

    else:

        df.to_csv(
            output_path,
            index=False,
            encoding="utf-8-sig"
        )