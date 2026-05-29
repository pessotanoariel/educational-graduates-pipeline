# Educational Graduates Pipeline

## Project Overview

Educational Graduates Pipeline is a modular data pipeline designed to process, validate, profile, and consolidate educational graduates datasets from multiple heterogeneous sources.

The project aims to progressively evolve into a reproducible and scalable data engineering workflow for educational analytics and graduate validation processes.

---

## Documentation

Additional project documentation is available under:

- docs/architecture.md
- docs/consolidation_logic.md
- docs/roadmap.md

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
- Dataset consolidation
- Source prioritization
- Record deduplication
- Field enrichment
- Data quality monitoring
- Quality reporting

---

## Current Pipeline Stages

```text
Raw Datasets
      ↓
Profiling
      ↓
Standardization
      ↓
Quality Validation
      ↓
Processed Datasets
      ↓
Consolidation
      ↓
Source Prioritization
      ↓
Deduplication
      ↓
Field Enrichment
      ↓
Data Quality Monitoring
      ↓
Reports & Exports
```

## Standardization

- Column normalization
- Document type normalization
- Gender normalization
- Text field cleaning

## Validation

- Invalid document detection
- Missing identity detection
- Quality checks

## Profiling

- Dataset statistics
- Null analysis
- Profiling reports

## Consolidation

- Dataset concatenation
- Source priority assignment
- Record deduplication
- Email enrichment
- Phone enrichment
- Nationality enrichment
  
## Project Structure

```text
project/
│
├── config/         # Centralized project settings
├── data/
│   ├── raw/        # Raw input datasets
│   ├── processed/  # Intermediate processed datasets
│   └── output/     # Pipeline outputs and reports
│       ├── consolidated/
│       ├── profiling/
│       ├── reports/
│       └── validation/
│
├── docs/           # Technical documentation and roadmap
├── logs/           # Execution logs
├── notebooks/      # Exploratory notebooks
├── src/
│   ├── extract/    # Dataset loaders
│   ├── load/       # Export utilities
│   ├── transform/  # Dataset transformation and consolidation
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

Run consolidation pipeline:

```bash
python -m src.transform.run_consolidation
```

---

## Outputs

The pipeline automatically generates:

- Processed standardized datasets
- Profiling summary reports
- Validation reports
- Consolidated datasets
- Deduplication summaries
- Consolidation reports
- Execution logs

Outputs are stored in:

```text
data/output/
```

### Monitoring Reports

- Quality summary reports
- Null distribution reports
- Duplicate record reports
- Enrichment summary reports

---

## Current Status

Current version includes:

- Multi-source dataset ingestion
- Dataset standardization and normalization
- Modular transformation architecture
- Data quality validations
- Processed dataset generation
- Dataset consolidation
- Record deduplication
- Consolidation summary reporting
- Centralized configuration and logging

---

## Next Steps

Planned future improvements:

- Advanced survivorship rules
- Additional field enrichment
- Pipeline orchestration
- Quality monitoring
- Performance optimization
- API integration
- Data warehouse integration
  
---
