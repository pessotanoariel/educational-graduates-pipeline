import pandas as pd

from datetime import date

from config.settings import (
    PROCESSED_DATA_DIR,
    CONSOLIDATED_OUTPUT_DIR,
    REPORTS_OUTPUT_DIR,
    VALIDATION_OUTPUT_DIR,
    PUBLISHED_OUTPUT_DIR,
    HISTORICAL_OUTPUT_DIR
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
    enrich_email_fields,
    enrich_phone_fields,
    enrich_nationality_fields
)

from src.load.exporters import (
    export_dataframe,
    append_dataframe
)

from src.utils.logger import logger

from src.transform.publish import (
    build_operational_dataset
)

def run_consolidation_pipeline():
    """Run dataset consolidation pipeline."""
    
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

    phones_before_enrichment = (
        deduplicated_df["phone_number"]
        .notna()
        .sum()
    )

    deduplicated_df = enrich_phone_fields(
        prioritized_df,
        deduplicated_df
    )

    phones_after_enrichment = (
        deduplicated_df["phone_number"]
        .notna()
        .sum()
    )

    phones_enriched = (
        phones_after_enrichment -
        phones_before_enrichment
    )

    nationalities_before_enrichment = (
        deduplicated_df["nationality"]
        .notna()
        .sum()
    )

    deduplicated_df = enrich_nationality_fields(
        prioritized_df,
        deduplicated_df
    )

    nationalities_after_enrichment = (
        deduplicated_df["nationality"]
        .notna()
        .sum()
    )

    nationalities_enriched = (
        nationalities_after_enrichment -
        nationalities_before_enrichment
    )

    # ==============================
    # Data Quality Monitoring
    # ==============================

    source_records = len(unified_df)

    unique_people = len(deduplicated_df)

    email_coverage_pct = round(
        deduplicated_df["email"]
        .notna()
        .mean()
        * 100,
        2
    )

    phone_coverage_pct = round(
        deduplicated_df["phone_number"]
        .notna()
        .mean()
        * 100,
        2
    )

    nationality_coverage_pct = round(
        deduplicated_df["nationality"]
        .notna()
        .mean()
        * 100,
        2
    )

    missing_document_number_pct = round(
        deduplicated_df["document_number"]
        .isna()
        .mean()
        * 100,
        2
    )

    missing_document_type_pct = round(
        deduplicated_df["document_type"]
        .isna()
        .mean()
        * 100,
        2
    )

    missing_identity_pct = round(
        (
            deduplicated_df["document_number"].isna()
            &
            deduplicated_df["document_type"].isna()
        )
        .mean()
        * 100,
        2
    )

    duplicates_removed = (
        source_records
        - unique_people
    )

    duplicate_records_pct = round(
        duplicates_removed
        / source_records
        * 100,
        2
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
    # Operational Dataset
    # ==============================

    operational_df = build_operational_dataset(
        deduplicated_df
    )

    # ==============================
    # Export Operational Dataset
    # ==============================

    latest_output_path = (
        PUBLISHED_OUTPUT_DIR /
        "base_graduados_unificada_latest.csv"
    )

    export_dataframe(
        operational_df,
        latest_output_path
    )

    historical_output_path = (
        HISTORICAL_OUTPUT_DIR /
        f"base_graduados_unificada_{date.today()}.csv"
    )

    export_dataframe(
        operational_df,
        historical_output_path
    )

    print("\n=== OPERATIONAL DATASET EXPORTED ===")
    print(latest_output_path)

    print("\n=== HISTORICAL DATASET EXPORTED ===")
    print(historical_output_path)

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

    print("\n=== PHONE ENRICHMENT SUMMARY ===")

    print(
        f"Phones before enrichment: {phones_before_enrichment}"
    )

    print(
        f"Phones after enrichment: {phones_after_enrichment}"
    )

    print(
        f"Phones enriched: {phones_enriched}"
    )

    print("\n=== NATIONALITY ENRICHMENT SUMMARY ===")

    print(
        f"Nationalities before enrichment: {nationalities_before_enrichment}"
    )

    print(
        f"Nationalities after enrichment: {nationalities_after_enrichment}"
    )

    print(
        f"Nationalities enriched: {nationalities_enriched}"
    )

    print("\n=== DEDUPLICATION SUMMARY ===")

    print(
        f"Rows before deduplication: {len(unified_df)}"
    )

    print(
        f"Rows after deduplication: {len(deduplicated_df)}"
    )

    print(
        f"Duplicated records removed: {duplicates_removed}"
    )

    # ==============================
    # Pipeline Summary Reports
    # ==============================

    # ==============================
    # Consolidation Reports
    # ==============================

    consolidation_summary_df = pd.DataFrame([
        {
            "total_records": source_records,
            "unique_people": unique_people,
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

    enrichment_summary_df = pd.DataFrame([
        {
            "field": "email",
            "before": emails_before_enrichment,
            "after": emails_after_enrichment,
            "enriched": emails_enriched
        },
        {
            "field": "phone_number",
            "before": phones_before_enrichment,
            "after": phones_after_enrichment,
            "enriched": phones_enriched
        },
        {
            "field": "nationality",
            "before": nationalities_before_enrichment,
            "after": nationalities_after_enrichment,
            "enriched": nationalities_enriched
        }
    ])

    enrichment_summary_output_path = (
        REPORTS_OUTPUT_DIR /
        "enrichment_summary.csv"
    )

    export_dataframe(
        enrichment_summary_df,
        enrichment_summary_output_path
    )

    # ==============================
    # Data Quality Reports
    # ==============================

    quality_summary_df = pd.DataFrame([
        {"metric": "total_records", "value": source_records},
        {"metric": "unique_people", "value": unique_people},
        {"metric": "duplicates_removed", "value": duplicates_removed},
        {"metric": "email_coverage_pct", "value": email_coverage_pct},
        {"metric": "phone_coverage_pct", "value": phone_coverage_pct},
        {"metric": "nationality_coverage_pct", "value": nationality_coverage_pct},
        {"metric": "missing_document_number_pct", "value": missing_document_number_pct},
        {"metric": "missing_document_type_pct", "value": missing_document_type_pct},
        {"metric": "missing_identity_pct", "value": missing_identity_pct},
        {"metric": "duplicate_records_pct", "value": duplicate_records_pct}
    ])

    quality_summary_output_path = (
        REPORTS_OUTPUT_DIR /
        "quality_summary.csv"
    )

    export_dataframe(
        quality_summary_df,
        quality_summary_output_path
    )

    quality_history_df = pd.DataFrame([
        {
            "execution_date": date.today(),
            "source_records": source_records,
            "unique_people": unique_people,
            "duplicate_records_pct": duplicate_records_pct,
            "email_coverage_pct": email_coverage_pct,
            "phone_coverage_pct": phone_coverage_pct,
            "nationality_coverage_pct": nationality_coverage_pct,
            "missing_document_type_pct": missing_document_type_pct
        }
    ])

    quality_history_output_path = (
        REPORTS_OUTPUT_DIR /
        "quality_history.csv"
    )

    append_dataframe(
        quality_history_df,
        quality_history_output_path
    )

    print("\n=== CONSOLIDATION SUMMARY EXPORTED ===")
    print(summary_output_path)

    print("\n=== ENRICHMENT SUMMARY EXPORTED ===")
    print(enrichment_summary_output_path)

    logger.info(
        "Dataset consolidation pipeline completed"
    )
    
    pass