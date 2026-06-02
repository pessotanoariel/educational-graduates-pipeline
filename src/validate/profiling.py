import pandas as pd
from config.settings import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    VALIDATION_OUTPUT_DIR,
    PROFILING_OUTPUT_DIR
)
from src.utils.logger import logger
from src.extract.loaders import load_dataset
from src.validate.profiling_utils import (
    process_dataset,
    get_dataset_paths
)
from src.validate.quality_checks import (
    check_null_values,
    check_duplicate_rows,
    check_document_length,
    columns_exist,
    validate_standardized_schema
)
from src.load.exporters import export_dataframe

from src.transform.standardize import (
    transform_dataset
)

# ==============================
# Dataset Discovery
# ==============================

dataset_paths = get_dataset_paths(RAW_DATA_DIR)

profiling_summaries = []

# ==============================
# Dataset Processing
# ==============================

for dataset_path in dataset_paths:

    logger.info(
        f"Processing dataset: {dataset_path.name}"
    )

# ==============================
# Dataset Loading
# ==============================

    df = load_dataset(dataset_path)

# ==============================
# Dataset Transformation
# ==============================

    standardized_df = transform_dataset(
        df,
        dataset_name=dataset_path.name
    )

    processed_output_path = (
        PROCESSED_DATA_DIR /
        f"{dataset_path.stem}_processed.csv"
    )

    export_dataframe(
        standardized_df,
        processed_output_path
    )

    logger.info(
        f"Processed dataset exported: {processed_output_path.name}"
    )

    logger.info(
        f"Rows exported: {len(standardized_df)}"
    )

# ==============================
# Dataset Profiling
# ==============================

    summary = process_dataset(
        standardized_df,
        dataset_name=dataset_path.name
    )

    profiling_summaries.append(summary)

# ==============================
# Quality Checks
# ==============================

    null_summary = check_null_values(standardized_df)

    print("\n=== NULL VALUES ===")
    print(null_summary)

    duplicate_rows = check_duplicate_rows(standardized_df)

    print("\n=== DUPLICATE ROWS ===")
    print(duplicate_rows)

# ==============================
# Schema Validation
# ==============================

    expected_columns = [
        "document_number",
        "document_type"
    ]

    missing_columns = validate_standardized_schema(
        standardized_df,
        expected_columns
    )

    if len(missing_columns) > 0:

        logger.warning(
            f"Missing standardized columns: {missing_columns}"
        )

# ==============================
# Document Validation
# ==============================

    required_columns = [
        "document_type",
        "document_number"
    ]

    if columns_exist(
        standardized_df,
        required_columns
        ):

        invalid_documents = check_document_length(
            standardized_df,
            document_column="document_number",
            document_type_column="document_type"
        )

        print("\n=== INVALID DOCUMENTS ===")
        print(invalid_documents)

        if len(invalid_documents) > 0:

            output_path = (
                VALIDATION_OUTPUT_DIR /
                f"{dataset_path.stem}_invalid_documents.csv"
            )

            export_dataframe(
                invalid_documents,
                output_path
            )

            logger.warning(
                f"{len(invalid_documents)} invalid documents detected"
            )

    else:

        logger.warning(
            "Document validation skipped: required columns not found"
        )
    
    logger.info(
        f"Finished processing dataset: {dataset_path.name}"
    )

# ==============================
# Profiling Summary Export
# ==============================

profiling_summary_df = pd.DataFrame(
    profiling_summaries
)

summary_output_path = (
    PROFILING_OUTPUT_DIR /
    "profiling_summary.csv"
)

export_dataframe(
    profiling_summary_df,
    summary_output_path
)