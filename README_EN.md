# Educational Graduates Pipeline

## Overview

Educational Graduates Pipeline is a modular data pipeline designed to process, validate, profile, consolidate, enrich, and publish educational graduate datasets from multiple heterogeneous sources.

The project was developed to automate graduate data consolidation, improve data quality, and generate stable datasets for both operational and analytical consumption.

It currently operates as a Data Product with monitoring, publication, and quality control capabilities.

---

## Key Features

* Multi-source dataset processing
* Automatic dataset discovery
* Data standardization and normalization
* Dataset profiling
* Data quality validation
* Record deduplication
* Source prioritization
* Field enrichment
* Historical quality monitoring
* Operational dataset publication
* Analytical dataset generation
* Modular and testable architecture

---

## Architecture

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
data/output/consolidated/unified_graduates_dataset.csv
```

---

### Curated Layer

Analytics-ready datasets designed for reporting and business analysis.

Documentation:

```text
docs/curated_layer.md
```

---

### Publication Layer

Stable datasets intended for downstream systems.

Operational dataset:

```text
data/output/published/base_graduados_unificada_latest.csv
```

Historical snapshots:

```text
data/output/historical/
```

---

### Monitoring Layer

Automated quality and monitoring reports.

Main outputs:

* quality_summary.csv
* quality_history.csv
* enrichment_summary.csv
* null_distribution_report.csv
* duplicated_records_report.csv

---

## Project Structure

```text
project/
│
├── config/
├── data/
├── docs/
├── logs/
├── monitoring/
├── notebooks/
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

## Usage

Run the complete pipeline:

```bash
python main.py
```

---

## Main Outputs

### Operational Dataset

```text
base_graduados_unificada_latest.csv
```

Used by downstream systems to validate graduate records.

### Analytical Dataset

```text
unified_graduates_dataset.csv
```

Enriched dataset designed for analysis and monitoring.

### Monitoring Reports

Automated reports for quality, enrichment, duplicate detection, and historical monitoring.

---

## Documentation

* docs/architecture.md
* docs/consolidation_logic.md
* docs/curated_layer.md
* docs/roadmap.md
* docs/technical_backlog.md

---

## Current Status

Version:

```text
v1.1
```

Status:

```text
Publication Layer completed
Monitoring Layer operational
Phase 5 — Analytical Modeling in progress
```

---

## Future Roadmap

* Curated datasets
* Analytical modeling
* Database integration
* Analytics Engineering concepts
* Automation and deployment
