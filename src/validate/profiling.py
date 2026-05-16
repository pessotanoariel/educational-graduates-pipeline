import pandas as pd
from config.settings import (
    RAW_DATA_DIR,
    OUTPUT_DATA_DIR
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
    columns_exist
)
from src.load.exporters import export_dataframe

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

    df = load_dataset(dataset_path)

    summary = process_dataset(
    df,
    dataset_name=dataset_path.name
    )

    profiling_summaries.append(summary)

# ==============================
# Quality Checks
# ==============================

    null_summary = check_null_values(df)

    print("\n=== NULL VALUES ===")
    print(null_summary)

    duplicate_rows = check_duplicate_rows(df)

    print("\n=== DUPLICATE ROWS ===")
    print(duplicate_rows)

# ==============================
# Document Validation
# ==============================

    required_columns = [
        "Tipo de documento",
        "Nro de documento"
    ]

    if columns_exist(df, required_columns):

        invalid_documents = check_document_length(
            df,
            document_column="Nro de documento",
            document_type_column="Tipo de documento"
        )

        print("\n=== INVALID DOCUMENTS ===")
        print(invalid_documents)

        if len(invalid_documents) > 0:

            output_path = (
                OUTPUT_DATA_DIR /
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
    OUTPUT_DATA_DIR /
    "profiling_summary.csv"
)

export_dataframe(
    profiling_summary_df,
    summary_output_path
)