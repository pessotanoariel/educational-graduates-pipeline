# Project Architecture

## Overview

Educational Graduates Pipeline is a modular data engineering project designed to process, validate, consolidate, enrich, and monitor educational graduates datasets from multiple heterogeneous sources.

The project follows a staged architecture focused on reproducibility, data quality, maintainability, and readiness for downstream analytical or operational consumption.

---

## Architecture Layers

The pipeline is organized into independent processing layers. Each layer has a specific responsibility and produces outputs consumed by downstream stages.

### Extract

Responsible for discovering and loading raw source datasets into memory.

Main components:

- Dataset loaders
- Automatic source discovery

### Transform

Responsible for standardizing heterogeneous datasets and applying consolidation logic.

Main components:

- Column normalization
- Document type standardization
- Gender standardization
- Source priority assignment
- Record deduplication
- Field enrichment

### Validate

Responsible for profiling datasets and executing data quality validations.

Main components:

- Profiling reports
- Missing identity detection
- Duplicate detection
- Quality checks

### Load

Responsible for exporting processed datasets, reports, and consolidated outputs.

Main components:

- Dataset exports
- Report exports

### Pipeline

Responsible for orchestrating the end-to-end execution flow.

Main components:

- Profiling pipeline
- Consolidation pipeline

---

---

## Data Flow

The pipeline follows a staged processing workflow designed to progressively improve data quality and consolidate information from multiple educational sources.

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

## High-Level Architecture

```text
                ┌───────────────┐
                │ Raw Datasets  │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   Profiling   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │Standardization│
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ Quality Check │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ Consolidation │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │  Enrichment   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │  Monitoring   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ Reports/Output│
                └───────────────┘
```

### Processing Stages

#### Raw Datasets

Source files are collected from multiple educational programs and stored in the raw data layer.

#### Profiling

Initial dataset exploration is performed to understand structure, null values, duplicates, and general dataset characteristics.

#### Standardization

Source-specific schemas are transformed into a common structure using standardized field names and normalization rules.

#### Quality Validation

Validation rules identify missing identities, invalid documents, duplicates, and other data quality issues.

#### Processed Datasets

Validated and standardized datasets are stored as intermediate processing outputs.

#### Consolidation

Multiple datasets are merged into a unified dataset.

#### Source Prioritization

Records are ranked according to predefined source reliability rules.

#### Deduplication

Duplicate records are consolidated into a single person-level representation.

#### Field Enrichment

Missing information can be recovered from lower-priority sources.

Current enrichment strategies include:

- Email enrichment
- Phone enrichment
- Nationality enrichment

#### Data Quality Monitoring

Quality metrics and monitoring reports are generated to track completeness, duplicates, and overall dataset health.

#### Reports & Exports

Final datasets and monitoring reports are exported for downstream consumption.

---

## Project Structure

The repository is organized into modular components that separate extraction, transformation, validation, loading, and orchestration responsibilities.

```text
config/
data/
docs/
src/
tests/
```

### config

Centralized project configuration and settings.

### data

Storage layer for raw datasets, processed datasets, and generated outputs.

### docs

Technical documentation, architecture references, and project roadmap.

### src

Core application logic.

Submodules include:

- extract
- transform
- validate
- load
- pipeline
- utils

### tests

Automated tests and validation of reusable components.

---

## Outputs

The pipeline generates multiple categories of outputs.

### Processed Outputs

- Standardized datasets
- Consolidated datasets

### Validation Outputs

- Missing identity reports
- Duplicate record reports
- Unmapped source reports

### Monitoring Outputs

- Quality summary reports
- Null distribution reports
- Enrichment reports
- Consolidation summary reports

All outputs are stored under:

```text
data/output/
```

---

## Future Evolution

Planned future improvements include:

- Historical quality monitoring
- Additional enrichment strategies
- Expanded automated testing
- Database integration
- Analytics engineering practices
- Orchestration and automation
