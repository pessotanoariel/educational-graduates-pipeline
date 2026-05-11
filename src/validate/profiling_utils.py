def run_basic_profile(df):
    """Display basic profiling information for a dataset."""
    print("\n=== INFO GENERAL ===")
    df.info()

    print("\n=== COLUMNAS ===")
    print(df.columns.tolist())

    print("\n=== PRIMERAS FILAS ===")
    print(df.head())

def generate_dataset_summary(df):
    """"Generate basic dataset metadata summary."""
    summary = {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": df.duplicated().sum(),
        "memory_mb": round(
            df.memory_usage(deep=True).sum() / 1024**2,
            2
        )
    }

    return summary