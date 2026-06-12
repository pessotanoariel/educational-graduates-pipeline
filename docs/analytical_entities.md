# Analytical Entities

## Overview

The analytical layer is built around a small set of business entities extracted from the consolidated graduates dataset.

These entities represent the core analytical concepts required for reporting, monitoring, and future dimensional modeling.

---

## Entity: Graduate

Description:

Represents a unique graduate identified through the consolidation and deduplication process.

Granularity:

```text
1 row = 1 graduate
```

Primary Identifier:

```text
document_type + document_number
```

Examples of attributes:

* full_name
* gender
* birth_date
* nationality
* email
* phone_number

Business Questions:

* Who graduated?
* What demographic characteristics are available?
* Can the graduate be contacted?

---

## Entity: Institution

Description:

Represents the educational institution associated with the graduate.

Current Representation:

```text
institution_name
```

Business Questions:

* Where did the graduate study?
* Which institutions generate the highest number of graduates?

---

## Entity: Educational Offer

Description:

Represents the educational program, course, certification, or training completed by the graduate.

Current Representation:

```text
offer
offer_type
```

Business Questions:

* What did the graduate complete?
* Which educational offers generate the most graduates?

---

## Entity: Educational Sector

Description:

Represents the educational classification associated with the graduate record.

Current Representation:

```text
education_sector
```

Examples:

* Technical Higher Education
* Adult Education
* Secondary Education
* Private Education

Business Questions:

* Which educational sectors generate graduates?
* How are graduates distributed across sectors?

---

## Entity: Source System

Description:

Represents the operational origin of the graduate record.

Current Representation:

```text
source_file
```

Examples:

* SiTED
* Talento Tech
* CFP
* ENOF
* CAC
* English Programs
* Microcredentials

Business Questions:

* Which systems contribute graduates?
* What is the coverage and quality of each source?

---

## Entity Relationships

```text
Graduate
    │
    ├── Institution
    │
    ├── Educational Offer
    │
    ├── Educational Sector
    │
    └── Source System
```

---

## Modeling Notes

Current analytical modeling treats Graduate as the central business entity.

Institution, Educational Offer, Educational Sector, and Source System behave as analytical dimensions that may evolve into future dimension tables if a dimensional model is implemented.

The current curated dataset preserves these entities as descriptive attributes while maintaining a simple analytics-ready structure.
