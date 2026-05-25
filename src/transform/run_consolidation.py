import pandas as pd

from config.settings import (
    PROCESSED_DATA_DIR,
    CONSOLIDATED_OUTPUT_DIR,
    REPORTS_OUTPUT_DIR
)

from src.transform.consolidate import (
    load_processed_datasets,
    concatenate_datasets,
    remove_duplicate_records
)

from src.load.exporters import (
    export_dataframe
)

from src.utils.logger import logger

# ==============================
# Load Processed Datasets
# ==============================

datasets = load_processed_datasets(
    PROCESSED_DATA_DIR
)

# ==============================
# Dataset Consolidation
# ==============================

unified_df = concatenate_datasets(
    datasets
)

# ==============================
# Record Deduplication
# ==============================

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

# ==============================
# Consolidation Metrics
# ==============================

print("\n=== DEDUPLICATION SUMMARY ===")

print(
    f"Rows before deduplication: {len(unified_df)}"
)

print(
    f"Rows after deduplication: {len(deduplicated_df)}"
)

duplicates_removed = (
    len(unified_df) -
    len(deduplicated_df)
)

print(
    f"Duplicated records removed: {duplicates_removed}"
)

# ==============================
# Consolidation Summary Report
# ==============================

consolidation_summary_df = pd.DataFrame([
    {
        "total_records": len(unified_df),
        "unique_people": len(deduplicated_df),
        "duplicates_removed": duplicates_removed
    }
])

summary_output_path = (
    REPORTS_OUTPUT_DIR /
    "consolidation_summary.csv"
)

export_dataframe(
    consolidation_summary_df,
    summary_output_path
)

print("\n=== CONSOLIDATION SUMMARY EXPORTED ===")
print(summary_output_path)

logger.info(
    "Dataset consolidation pipeline completed"
)