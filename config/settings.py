from pathlib import Path

# Root project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DATA_DIR = DATA_DIR / "output"

# Logs
LOGS_DIR = BASE_DIR / "logs"

# Docs
DOCS_DIR = BASE_DIR / "docs"