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

## Derived Attributes

Implemented:

* contact_available
* contact_completeness

Evaluated but not implemented:

* age
* age_group
* graduation_year

Reason:

Current source data quality does not provide sufficient consistency for reliable age derivation and graduation year standardization across all datasets.

---

## Excluded Technical Fields

Examples:

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

## Analytical Modeling Findings

Initial exploratory analysis identified different levels of analytical entities within the consolidated dataset.

### Source Layer

The following entities represent operational data sources:

* SiTED
* CFP
* ENOF
* Talento Tech
* CAC
* English Programs
* Microcredentials
* SecundarT

These entities answer:

"What system generated the record?"

### Education Sector Layer

The field `education_sector` represents educational system classifications mainly provided by SiTED, including:

* Secondary Education
* Adult Education
* Technical Education
* Technical Higher Education
* Private Education

These entities answer:

"What educational sector does the graduate belong to?"

### Modeling Considerations

Current analytical exploration suggests that:

* `source_file` is a stable analytical dimension.
* `institution_name` is a stable analytical dimension.
* `education_sector` is partially available and source-dependent.
* `offer` should remain a descriptive attribute rather than a governed dimension due to high variability across sources.

Future modeling may require a standardized educational category layer to harmonize programs such as:

* CFP → Professional Training
* ENOF → Non-Formal Education
* Talento Tech → Technology Training
* CAC → Language Training
* Microcredentials → Digital Credentials

## Reporting Opportunities

Current reporting opportunities identified during analytical exploration:

### Monitoring Workbook

Focus:

* Data quality
* Coverage metrics
* Historical monitoring

### Graduate Analytics Workbook

Focus:

* Graduates by source
* Graduates by institution
* Graduates by education sector
* Academic year analysis

### Future Power BI Model

Focus:

* Analytical consumption
* Dimensional modeling
* Executive reporting
* Graduate trends
