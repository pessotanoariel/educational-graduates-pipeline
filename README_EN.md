# Educational Graduates Pipeline

A data engineering project designed to consolidate graduate records from multiple heterogeneous educational sources into a unified, validated, and analytics-ready dataset.

The project was created to solve a real-world educational data integration problem, where multiple operational systems generated duplicate, incomplete, or inconsistent information about the same individual.

It currently operates as a Data Product with profiling, validation, consolidation, enrichment, monitoring, and publication capabilities.

---

## Problem Statement

Educational organizations often manage graduate information across multiple independent systems.

This creates challenges such as:

* Duplicate records
* Incomplete information
* Inconsistent schemas across sources
* Limited traceability
* Difficulty producing reliable reporting

This project addresses those challenges through a reproducible and well-documented data pipeline.

---

## Key Features

* Multi-source graduate processing
* Automatic dataset discovery
* Data standardization and normalization
* Automated data profiling
* Data quality validation
* Invalid record detection
* Person consolidation and deduplication
* Source prioritization
* Survivorship rules
* Contact information enrichment
* Historical quality monitoring
* Operational dataset publication
* Analytics-ready dataset generation
* Modular and testable architecture

---

## Project Results

Current production-scale metrics:

* 800,000+ source records processed
* 379,000+ unique graduates consolidated
* 420,000+ duplicate records removed
* Automated email enrichment
* Automated phone enrichment
* Automated nationality enrichment
* Historical monitoring and quality reporting

---

## Technologies

* Python
* Pandas
* Pytest
* Pathlib
* Logging
* Power Query
* Git

Applied concepts:

* ETL
* Data Quality
* Data Profiling
* Data Validation
* Data Consolidation
* Deduplication
* Survivorship Rules
* Data Product Design
* Analytical Modeling

---

## High-Level Architecture

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
Curated Layer
      ↓
Publication Layer
      ↓
Monitoring & Reports
```

---

## Project Layers

### Consolidated Layer

Technical dataset preserving all available attributes and source lineage.

Main output:

```text
unified_graduates_dataset.csv
```

Documentation:

```text
docs/consolidation_logic.md
```

---

### Curated Layer

Analytics-ready dataset optimized for reporting and business analysis.

Main output:

```text
graduates_curated.csv
```

Documentation:

```text
docs/curated_layer.md
```

---

### Publication Layer

Stable operational dataset intended for downstream systems.

Main output:

```text
base_graduados_unificada_latest.csv
```

Documentation:

```text
docs/publication_layer.md
```

---

### Monitoring Layer

Produces historical quality and coverage reports.

Examples:

* quality_history.csv
* quality_summary.csv
* enrichment_summary.csv
* duplicated_records_report.csv

---

## Project Structure

```text
project/
│
├── config/
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
│
├── docs/
├── src/
├── tests/
│
├── main.py
├── README.md
├── README_EN.md
└── requirements.txt
```

---

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
source venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Execution

Run the pipeline:

```bash
python main.py
```

---

## Privacy & Data Handling

This repository does not include real datasets.

Production datasets contain personally identifiable information (PII) and are excluded from version control through repository policies and Git ignore rules.

For additional information:

```text
docs/privacy_review.md
docs/publication_rules.md
```

---

## Documentation

### Architecture

* docs/architecture.md
* docs/consolidation_logic.md
* docs/publication_layer.md
* docs/curated_layer.md

### Analytical Modeling

* docs/analytical_entities.md
* docs/analytical_dimensions.md
* docs/semantic_layer.md

### Governance & Publication

* docs/privacy_review.md
* docs/publication_rules.md
* docs/public_release_checklist.md

### Roadmap

* docs/roadmap.md
* docs/technical_backlog.md

---

## Current Limitations

The project currently:

* Does not include database integration
* Does not implement incremental processing
* Does not include workflow orchestration
* Does not include CI/CD pipelines
* Does not provide sample datasets

These capabilities are planned for future roadmap phases.

---

## Current Status

Current version:

```text
v1.4 — Public Release Readiness
```

Status:

```text
Operational
Documented
Repository Audited
Ready for public portfolio use
```

---

## Next Phases

### Phase 6 — Database Integration

* SQLite
* PostgreSQL
* SQL Transformations
* Incremental Processing

### Phase 7 — Analytics Engineering

* Data Contracts
* Data Lineage
* dbt Concepts
* Expanded Automated Testing

### Phase 8 — Production & Automation

* Scheduled Executions
* Monitoring
* Deployment Automation
* Cloud Integration

## License

This project is licensed under the MIT License.
