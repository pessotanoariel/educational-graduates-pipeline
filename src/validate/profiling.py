from config.settings import RAW_DATA_DIR
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

# ==============================
# Dataset Discovery
# ==============================

dataset_paths = get_dataset_paths(RAW_DATA_DIR)

# ==============================
# Dataset Processing
# ==============================

for dataset_path in dataset_paths:

    logger.info(
        f"Processing dataset: {dataset_path.name}"
    )

    df = load_dataset(dataset_path)

    process_dataset(df, dataset_name=dataset_path.name)

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