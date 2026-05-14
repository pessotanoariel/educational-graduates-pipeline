def run_basic_profile(df, dataset_name=None):
    """Display basic profiling information for a dataset."""
    
    print("\n=== INFO GENERAL ===")

    if dataset_name:
        print(f"Dataset: {dataset_name}")

    df.info()

    print("\n=== COLUMNAS ===")
    print(df.columns.tolist())

    print("\n=== PRIMERAS FILAS ===")
    print(df.head())

def generate_dataset_summary(df, dataset_name=None):
    """Generate basic dataset metadata summary."""

    summary = {
        "dataset_name": dataset_name,
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": df.duplicated().sum(),
        "memory_mb": round(
            df.memory_usage(deep=True).sum() / 1024**2,
            2
        )
    }

    return summary

def get_dataset_paths(raw_data_dir):
    """Return dataset file paths from raw data directory."""

    valid_extensions = [".csv", ".xlsx"]

    dataset_paths = [
        path
        for path in raw_data_dir.iterdir()
        if path.suffix.lower() in valid_extensions
    ]

    return dataset_paths

def process_dataset(df, dataset_name=None):
    """Run basic profiling and summary generation for a dataset."""
    
    run_basic_profile(df, dataset_name)

    summary = generate_dataset_summary(df, dataset_name)

    print("\n=== DATASET SUMMARY ===")

    for key, value in summary.items():
        print(f"{key}: {value}")