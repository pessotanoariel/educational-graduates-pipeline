# Publication Layer

## Overview

The publication layer is responsible for generating stable operational datasets intended for downstream consumption.

Its objective is to provide a simplified and controlled representation of graduate information while hiding technical implementation details from consuming systems.

---

## Data Flow

```text
Raw Datasets
      ↓
Processed Datasets
      ↓
Consolidated Dataset
      ↓
Publication Layer
      ↓
Operational Consumption
```

---

## Purpose

The publication layer exists to:

* Provide a stable operational dataset
* Reduce complexity for consuming systems
* Isolate downstream consumers from internal transformations
* Standardize graduate validation processes
* Preserve compatibility across data refreshes

---

## Published Dataset

### base_graduados_unificada_latest.csv

Granularity:

```text
1 row = 1 graduate
```

Purpose:

* Graduate validation
* Operational consumption
* External system integration

---

## Included Fields

The publication dataset exposes a minimal set of attributes required for graduate identification and validation.

Current fields:

* clave_persona
* tipo_doc
* nro_doc
* genero
* nombre_apellido
* egresado

---

## Business Rules

### Graduate Status

The publication layer only contains graduates.

Therefore:

```text
egresado = T
```

for all published records.

---

### Identity Key

A unique operational identifier is generated:

```text
clave_persona =
document_type + "_" + document_number
```

Examples:

```text
DNI_12345678
PASAPORTE_A123456
CI_9876543
```

---

### Null Document Handling

Records without a valid document number are excluded from publication outputs.

This ensures that published records remain identifiable and usable by consuming systems.

---

### Gender Standardization

Missing gender values are standardized as:

```text
sin_datos
```

to avoid null values in operational datasets.

---

## Historical Snapshots

In addition to the latest operational dataset, the publication layer generates historical snapshots.

Example:

```text
base_graduados_unificada_2026-06-12.csv
```

Purpose:

* Historical traceability
* Auditability
* Change monitoring

---

## Relationship with Other Layers

### Consolidated Layer

```text
unified_graduates_dataset.csv
```

Technical dataset preserving all available attributes and lineage information.

---

### Curated Layer

```text
graduates_curated.csv
```

Analytics-ready dataset intended for reporting and analysis.

---

## Publication Outputs

```text
base_graduados_unificada_latest.csv
```

Operational dataset intended for downstream systems.

---

## Privacy Considerations

Published datasets may contain personally identifiable information (PII).

For this reason:

* Publication outputs are excluded from version control
* Publication outputs are never committed to the repository
* Publication outputs are not distributed publicly

Refer to:

```text
docs/privacy_review.md
docs/publication_rules.md
```

for additional information.

---

## Current Status

```text
Implemented
Operational
Actively Used
```
