# Analytical Dimensions

## Overview

Analytical dimensions provide descriptive context for the core business entities identified in the analytical model.

These dimensions support filtering, grouping, segmentation, and reporting across the curated dataset.

---

## Identity Dimensions

Identity dimensions describe the graduate as an individual.

### document_type

Examples:

```text
DNI
CI
PASAPORTE
```

Purpose:

* Graduate identification
* Identity quality analysis

---

### gender

Examples:

```text
femenino
masculino
no_binario
sin_datos
```

Purpose:

* Demographic analysis
* Population segmentation

---

### nationality

Purpose:

* Population characterization
* Graduate diversity analysis

---

## Academic Dimensions

Academic dimensions describe the educational achievement associated with the graduate.

### offer

Examples:

```text
Data Analytics con Python
English Programs
Technical Degrees
Microcredentials
```

Purpose:

* Program-level analysis
* Graduate distribution by educational offer

---

### offer_type

Examples:

```text
Course
Learning Path
Technical Degree
Microcredential
```

Purpose:

* Educational offering classification
* Program comparison

---

### academic_year

Examples:

```text
2023
2024
2025
2026
```

Purpose:

* Historical analysis
* Graduation trends

---

### academic_period

Purpose:

* Academic cycle analysis
* Temporal reporting

---

## Institutional Dimensions

Institutional dimensions describe the organization responsible for the educational experience.

### institution_name

Examples:

```text
Talento Tech
CFP
IFTS
```

Purpose:

* Institution-level reporting
* Graduate distribution analysis

---

### education_sector

Examples:

```text
Technical Higher Education
Adult Education
Secondary Education
Private Education
```

Purpose:

* Educational system analysis
* Sector-level reporting

---

## Source Dimensions

Source dimensions describe the operational origin of the data.

### source_file

Examples:

```text
SiTED
Talento Tech
CFP
ENOF
CAC
English Programs
Microcredentials
```

Purpose:

* Data lineage
* Source monitoring
* Coverage analysis
* Data quality assessment

---

## Modeling Notes

Dimensions currently remain as descriptive attributes within the curated dataset.

Future dimensional modeling may evolve these dimensions into dedicated dimension tables for analytical reporting and semantic modeling.

Examples:

```text
dim_graduate
dim_institution
dim_offer
dim_education_sector
dim_source
```

The current approach prioritizes simplicity while preserving future modeling flexibility.

---

## Relationship with Curated Dataset

Current dimensions are exposed through:

```text
graduates_curated.csv
```

This dataset serves as the primary analytical dataset for reporting, exploration, and future semantic layer development.
