# Privacy Review

## Overview

This project processes educational graduate datasets originating from multiple operational systems.

Several datasets contain personally identifiable information (PII) and therefore require strict handling procedures.

---

## Sensitive Fields

The following fields are considered sensitive:

* document_number
* full_name
* email
* phone_number
* birth_date

These fields may appear in raw, processed, consolidated, curated, and published datasets.

---

## Risk Assessment

### Raw Datasets

Risk Level:

```text
HIGH
```

Contains operational source data and personally identifiable information.

Public release is prohibited.

---

### Processed Datasets

Risk Level:

```text
HIGH
```

Contains standardized records derived from operational sources.

Public release is prohibited.

---

### Consolidated Dataset

Risk Level:

```text
HIGH
```

Contains unified graduate records and personally identifiable information.

Public release is prohibited.

---

### Curated Dataset

Risk Level:

```text
HIGH
```

Contains analytics-ready graduate records with personally identifiable information.

Public release is prohibited.

---

### Published Dataset

Risk Level:

```text
HIGH
```

Contains operational graduate information used by downstream systems.

Public release is prohibited.

---

## Repository Controls

Current repository protections include:

* Raw datasets excluded from version control
* Processed datasets excluded from version control
* Generated outputs excluded from version control
* Environment files excluded from version control
* Logs excluded from version control

---

## Public Repository Policy

The public repository must never contain:

* Real graduate records
* Personal information
* Operational exports
* Production outputs

The repository is intended to expose source code, project architecture, documentation, and development practices only.

---

## Review Status

```text
Privacy Review Completed
```
