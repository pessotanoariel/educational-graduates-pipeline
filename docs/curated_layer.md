# Curated Layer

## Overview

The curated layer provides analytics-ready datasets built on top of the consolidated graduates dataset.

Its objective is to expose business-oriented entities and attributes while reducing technical complexity for reporting and analysis.

---

## Data Flow

```text
Raw Datasets
      ↓
Processed Datasets
      ↓
Consolidated Dataset
      ↓
Curated Layer
      ↓
Analytical Consumption
```

---

## Curated Dataset

### graduates_curated.csv

Granularity:

```text
1 row = 1 graduate
```

Purpose:

* Reporting
* Business analysis
* Power BI consumption
* Analytical exploration

---

## Included Business Attributes

### Identity

* document_type
* document_number
* gender
* birth_date
* nationality

### Academic Information

* offer
* offer_type
* institution_name
* education_sector
* academic_year
* academic_period

### Contact Information

* email
* phone_number

---

## Derived Attributes (Future)

Potential derived fields:

* age
* age_group
* contact_available
* contact_completeness
* graduation_year

---

## Excluded Technical Fields

Examples:

* source_file
* source_priority
* badge_id
* event_id
* assertion_id

These fields remain available in the consolidated dataset but are not required for analytical consumption.

---

## Relationship with Other Outputs

### Consolidated Layer

```text
unified_graduates_dataset.csv
```

Technical dataset containing all available attributes and lineage information.

### Curated Outputs

```text
graduates_curated.csv
```

Analytics-ready dataset optimized for reporting and business analysis.

### Publication Layer

```text
base_graduados_unificada_latest.csv
```

Operational dataset intended for downstream systems and graduate validation.
