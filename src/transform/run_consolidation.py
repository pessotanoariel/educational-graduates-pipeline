from config.settings import (
    PROCESSED_DATA_DIR,
    CONSOLIDATED_OUTPUT_DIR
)

from src.transform.consolidate import (
    load_processed_datasets,
    concatenate_datasets,
    remove_duplicate_records
)

from src.load.exporters import (
    export_dataframe
)

# ==============================
# Load Processed Datasets
# ==============================

datasets = load_processed_datasets(
    PROCESSED_DATA_DIR
)

# ==============================
# Concatenate Datasets
# ==============================

unified_df = concatenate_datasets(
    datasets
)

deduplicated_df = remove_duplicate_records(
    unified_df
)

# ==============================
# Preview
# ==============================

print("\n=== UNIFIED DATASET ===")
print(unified_df.info())

print("\n=== SAMPLE ROWS ===")
print(unified_df.head())

# ==============================
# Export Consolidated Dataset
# ==============================

consolidated_output_path = (
    CONSOLIDATED_OUTPUT_DIR /
    "unified_graduates_dataset.csv"
)

export_dataframe(
    deduplicated_df,
    consolidated_output_path
)

print("\n=== CONSOLIDATED DATASET EXPORTED ===")
print(consolidated_output_path)

print("\n=== DEDUPLICATION SUMMARY ===")

print(
    f"Rows before deduplication: {len(unified_df)}"
)

print(
    f"Rows after deduplication: {len(deduplicated_df)}"
)