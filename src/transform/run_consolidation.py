import pandas as pd

from config.settings import (
    PROCESSED_DATA_DIR,
    CONSOLIDATED_OUTPUT_DIR,
    REPORTS_OUTPUT_DIR,
    VALIDATION_OUTPUT_DIR
)

from src.transform.consolidate import (
    load_processed_datasets,
    concatenate_datasets,
    remove_duplicate_records,
    validate_critical_fields,
    detect_missing_document_identities,
    analyze_null_distribution,
    review_duplicated_records,
    apply_source_priority,
    detect_unmapped_sources,
    enrich_email_fields
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

prioritized_df = apply_source_priority(
    unified_df
)

unmapped_sources_df = detect_unmapped_sources(
    prioritized_df
)

deduplicated_df = remove_duplicate_records(
    prioritized_df
)

emails_before_enrichment = (
    deduplicated_df["email"]
    .notna()
    .sum()
)

deduplicated_df = enrich_email_fields(
    prioritized_df,
    deduplicated_df
)

emails_after_enrichment = (
    deduplicated_df["email"]
    .notna()
    .sum()
)

emails_enriched = (
    emails_after_enrichment -
    emails_before_enrichment
)

# ==============================
# Quality Validation
# ==============================

critical_field_summary = validate_critical_fields(
    deduplicated_df
)

missing_identity_df = detect_missing_document_identities(
    deduplicated_df
)

null_distribution_df = analyze_null_distribution(
    deduplicated_df
)

duplicated_records_df = review_duplicated_records(
    unified_df
)

# ==============================
# Quality Validation Preview
# ==============================

print("\n=== CRITICAL FIELD VALIDATION ===")

for field, missing_count in critical_field_summary.items():

    print(
        f"{field}: {missing_count} missing values"
    )

print("\n=== MISSING DOCUMENT IDENTITIES ===")

print(
    missing_identity_df[
        [
            "document_type",
            "document_number",
            "source_file"
        ]
    ].head()
)

print("\n=== NULL DISTRIBUTION ===")

print(
    null_distribution_df.head(10)
)

print("\n=== DUPLICATED RECORDS ===")

print(
    duplicated_records_df.head(10)
)

print("\n=== UNMAPPED SOURCES ===")

print(
    unmapped_sources_df[
        [
            "source_file",
            "source_priority"
        ]
    ]
    .drop_duplicates()
    .head(10)
)

# ==============================
# Quality Validation Exports
# ==============================

duplicated_records_output_path = (
    REPORTS_OUTPUT_DIR /
    "duplicated_records_report.csv"
)

export_dataframe(
    duplicated_records_df,
    duplicated_records_output_path
)

missing_identity_output_path = (
    VALIDATION_OUTPUT_DIR /
    "missing_document_identities.csv"
)

export_dataframe(
    missing_identity_df,
    missing_identity_output_path
)

null_distribution_output_path = (
    REPORTS_OUTPUT_DIR /
    "null_distribution_report.csv"
)

export_dataframe(
    null_distribution_df,
    null_distribution_output_path
)

unmapped_sources_output_path = (
    VALIDATION_OUTPUT_DIR /
    "unmapped_sources.csv"
)

export_dataframe(
    unmapped_sources_df,
    unmapped_sources_output_path
)

# ==============================
# Consolidated Dataset Preview
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

print("\n=== EMAIL ENRICHMENT SUMMARY ===")

print(
    f"Emails before enrichment: "
    f"{emails_before_enrichment}"
)

print(
    f"Emails after enrichment: "
    f"{emails_after_enrichment}"
)

print(
    f"Emails enriched: "
    f"{emails_enriched}"
)

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