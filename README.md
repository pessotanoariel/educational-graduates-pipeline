# Pipeline de Graduados Educativos

## Descripción General

Pipeline de datos modular diseñado para procesar, validar, perfilar, consolidar y publicar datasets de graduados provenientes de múltiples fuentes educativas heterogéneas.

El proyecto surgió para automatizar la consolidación de registros educativos, mejorar la calidad de los datos y generar datasets estables tanto para consumo operativo como para análisis.

Actualmente funciona como un Data Product con capacidades de monitoreo, enriquecimiento y publicación de datos.

---

## Principales Capacidades

* Procesamiento de múltiples fuentes de graduados
* Descubrimiento automático de datasets
* Estandarización y normalización de datos
* Perfilado automático de datasets
* Validaciones de calidad
* Detección de registros inválidos
* Consolidación y deduplicación de personas
* Priorización de fuentes
* Enriquecimiento de información de contacto
* Monitoreo de calidad histórico
* Generación de datasets operativos y analíticos
* Arquitectura modular y testeable

---

## Arquitectura General

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

## Capas del Proyecto

### Consolidated Layer

```text
data/output/consolidated/
```

Dataset técnico consolidado que preserva la totalidad de los atributos disponibles y la trazabilidad de las fuentes.

Archivo principal:

```text
unified_graduates_dataset.csv
```

---

### Curated Layer

Diseñada para consumo analítico.

Documentación:

```text
docs/curated_layer.md
```

Dataset planificado:

```text
graduates_curated.csv
```

---

### Publication Layer

Genera datasets estables para sistemas consumidores.

Dataset operativo:

```text
data/output/published/base_graduados_unificada_latest.csv
```

Snapshots históricos:

```text
data/output/historical/
```

---

### Monitoring Layer

Genera reportes automáticos de calidad y monitoreo.

Principales outputs:

* quality_summary.csv
* quality_history.csv
* enrichment_summary.csv
* null_distribution_report.csv
* duplicated_records_report.csv

---

## Estructura del Proyecto

```text
project/
│
├── config/
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
│       ├── consolidated/
│       ├── historical/
│       ├── profiling/
│       ├── published/
│       ├── reports/
│       └── validation/
│
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

## Instalación

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno:

```bash
source venv/Scripts/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Ejecución completa:

```bash
python main.py
```

---

## Outputs Principales

### Operativos

```text
base_graduados_unificada_latest.csv
```

Utilizado para validación de graduados por sistemas consumidores.

### Analíticos

```text
unified_graduates_dataset.csv
```

Dataset enriquecido para análisis y monitoreo.

### Monitoreo

Reportes automáticos de calidad, duplicados, cobertura y enriquecimiento.

---

## Documentación

* docs/architecture.md
* docs/consolidation_logic.md
* docs/curated_layer.md
* docs/roadmap.md
* docs/technical_backlog.md

---

## Estado Actual

Versión actual:

```text
v1.1
```

Estado:

```text
Publication Layer completa
Monitoring Layer operativa
Inicio de Phase 5 — Analytical Modeling
```

---

## Próximos Pasos

* Diseño de datasets curados
* Modelado analítico
* Integración con bases de datos
* Analytics Engineering
* Automatización y despliegue
