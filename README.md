# Educational Graduates Pipeline

## Project Overview

Educational Graduates Pipeline is a modular data pipeline designed to process, validate, profile, and consolidate educational graduates datasets from multiple heterogeneous sources.

The project aims to progressively evolve into a reproducible and scalable data engineering workflow for educational analytics and graduate validation processes.

---

## Current Features

- Multi-source dataset processing
- Automatic dataset discovery
- Modular dataset loaders
- Dataset profiling
- Data quality validations
- Invalid record exports
- Profiling summary reports
- Execution logging
- Centralized project configuration

---

## Project Structure

```text
project/
│
├── config/         # Centralized project settings
├── data/
│   ├── raw/        # Raw input datasets
│   ├── processed/  # Intermediate processed datasets
│   └── output/     # Pipeline outputs and reports
│
├── docs/           # Technical documentation and roadmap
├── logs/           # Execution logs
├── notebooks/      # Exploratory notebooks
├── src/
│   ├── extract/    # Dataset loaders
│   ├── load/       # Export utilities
│   ├── transform/  # Future transformation logic
│   ├── utils/      # Shared utilities
│   └── validate/   # Profiling and quality checks
│
├── tests/          # Future automated tests
├── main.py
└── requirements.txt
```

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
source venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run profiling pipeline:

```bash
python -m src.validate.profiling
```

---

## Outputs

The pipeline automatically generates:

- Profiling summary reports
- Invalid record exports
- Execution logs

Outputs are stored in:

```text
data/output/
```

---

## Current Status

Current version includes:

- Multi-source profiling
- Initial quality reporting
- Validation exports
- Modular project architecture

---

## Next Steps

Planned future improvements:

- Schema normalization
- Unified graduate datasets
- Advanced quality validations
- Automated transformations
- Historical profiling tracking
- Consolidated master datasets
- API integration
- Data warehouse integration

---
