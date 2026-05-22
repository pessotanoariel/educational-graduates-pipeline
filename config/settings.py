from pathlib import Path

# Root project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# Data directories
# ==============================

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DATA_DIR = DATA_DIR / "output"

# ==============================
# Output subdirectories
# ==============================

VALIDATION_OUTPUT_DIR = (
    OUTPUT_DATA_DIR / "validation"
)

PROFILING_OUTPUT_DIR = (
    OUTPUT_DATA_DIR / "profiling"
)

CONSOLIDATED_OUTPUT_DIR = (
    OUTPUT_DATA_DIR / "consolidated"
)

# ==============================
# Logs
# ==============================

LOGS_DIR = BASE_DIR / "logs"

# ==============================
# Docs
# ==============================

DOCS_DIR = BASE_DIR / "docs"