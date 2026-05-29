# Consolidation Logic

## Overview

The consolidation process combines multiple educational graduates datasets into a unified master dataset.

The objective is to identify unique individuals across heterogeneous sources while preserving the highest quality information available.

---

## Consolidation Workflow

```text
Processed Datasets
        ↓
Dataset Concatenation
        ↓
Source Priority Assignment
        ↓
Duplicate Detection
        ↓
Record Deduplication
        ↓
Field Enrichment
        ↓
Consolidated Dataset
```

---

## Source Priority

Datasets are assigned a priority level based on reliability, completeness, and business relevance.

When multiple records exist for the same individual, the highest-priority source is preserved as the base record.

Examples of higher-priority sources include:

* SiTED
* CFP
* ENOF

Additional datasets may be used to enrich missing information.

---

## Person Identification

Individuals are identified using:

* document_type
* document_number

These fields are used as the primary matching key during consolidation.

---

## Record Deduplication

Duplicate records are removed after source prioritization.

The pipeline preserves a single record per unique document identity.

---

## Field Enrichment

After deduplication, selected attributes can be enriched using information from lower-priority sources.

Current enrichment logic includes:

* Email recovery

Future enrichment candidates include:

* Phone number
* Nationality
* Birth date

---

## Outputs

The consolidation stage generates:

* Consolidated dataset
* Deduplication metrics
* Null distribution reports
* Missing identity reports
* Duplicate record reports

All outputs are stored under:

```text
data/output/
```
