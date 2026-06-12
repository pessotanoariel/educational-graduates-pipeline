# Semantic Layer

## Overview

The semantic layer defines the business meaning of the analytical model.

Its purpose is to establish a common vocabulary, analytical definitions, and business rules that can be consistently applied across reporting, monitoring, and future analytical solutions.

The semantic layer sits on top of the curated dataset and provides the foundation for analytical consumption.

---

## Business Terminology

### Graduate

Definition:

A unique individual identified through the consolidation and deduplication process.

A graduate represents the central business entity of the analytical model.

---

### Graduate Record

Definition:

A source-specific representation of a graduate before consolidation.

Multiple graduate records may exist for the same individual across different source systems.

---

### Consolidated Graduate

Definition:

A unique graduate record produced after applying source prioritization, survivorship rules, and enrichment logic.

---

### Institution

Definition:

Educational organization associated with a graduate.

Examples:

* Talento Tech
* CFP
* IFTS

---

### Educational Offer

Definition:

Program, course, certification, microcredential, or technical degree completed by a graduate.

---

### Educational Sector

Definition:

Educational classification associated with a graduate record.

Examples:

* Technical Higher Education
* Adult Education
* Secondary Education
* Private Education

---

### Source System

Definition:

Operational system contributing graduate data to the consolidated dataset.

Examples:

* SiTED
* Talento Tech
* CFP
* ENOF
* CAC
* English Programs
* Microcredentials

---

## Analytical Attributes

### Graduate Attributes

* full_name
* gender
* birth_date
* nationality
* email
* phone_number

---

### Academic Attributes

* offer
* offer_type
* academic_year
* academic_period

---

### Institutional Attributes

* institution_name
* education_sector

---

### Source Attributes

* source_file

---

## Derived Attributes

### Implemented Attributes

#### contact_available

Definition:

Indicates whether at least one contact method is available for the graduate.

Values:

```text
YES
NO
```

---

#### contact_completeness

Definition:

Classifies the level of available contact information.

Values:

```text
EMAIL_AND_PHONE
EMAIL_ONLY
PHONE_ONLY
NO_CONTACT
```

---

### Evaluated Attributes

The following attributes were reviewed but intentionally excluded from the current scope:

* age
* age_group
* graduation_year

Reasons:

* Inconsistent source coverage
* Data quality limitations
* Better calculated at reporting layer when required

---

## Analytical Definitions

### Total Graduates

Definition:

Count of unique graduates after consolidation and deduplication.

Calculation:

```text
COUNT(graduates)
```

---

### Email Coverage

Definition:

Percentage of graduates with a valid email address.

Calculation:

```text
graduates_with_email
/
total_graduates
```

---

### Phone Coverage

Definition:

Percentage of graduates with a valid phone number.

Calculation:

```text
graduates_with_phone
/
total_graduates
```

---

### Contact Coverage

Definition:

Percentage of graduates with at least one available contact method.

Calculation:

```text
graduates_with_email_or_phone
/
total_graduates
```

---

### Source Contribution

Definition:

Number of graduates contributed by each source system.

Examples:

* SiTED
* Talento Tech
* CFP
* ENOF
* Microcredentials

---

## Modeling Notes

The current semantic layer is implemented through documentation and curated datasets.

Future analytical implementations may evolve into:

```text
Power BI Semantic Models
Dimensional Models
Data Marts
Analytics Engineering Workflows
```

The current approach prioritizes simplicity while preserving future scalability.

---

## Relationship with Curated Dataset

The semantic layer is currently exposed through:

```text
graduates_curated.csv
```

This dataset serves as the primary analytical dataset for reporting, exploration, monitoring, and future analytical modeling initiatives.
