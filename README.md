# Educational Graduates Pipeline

Pipeline de datos diseñado para consolidar registros de graduados provenientes de múltiples fuentes educativas heterogéneas en un dataset unificado, validado y listo para consumo operativo y analítico.

El proyecto nació para resolver un problema real de integración de datos educativos, donde distintas plataformas generaban información duplicada, incompleta o inconsistente sobre una misma persona.

Actualmente funciona como un Data Product con capacidades de perfilado, validación, consolidación, enriquecimiento, monitoreo y publicación de datos.

---

## Problema

Las organizaciones educativas suelen administrar información de graduados desde múltiples sistemas independientes.

Esto genera desafíos como:

* Registros duplicados
* Información incompleta
* Diferencias de formato entre fuentes
* Falta de trazabilidad
* Dificultad para generar indicadores confiables

Este proyecto busca resolver esos problemas mediante un pipeline reproducible y documentado.

---

## Principales Capacidades

* Procesamiento de múltiples fuentes educativas
* Descubrimiento automático de datasets
* Estandarización y normalización de datos
* Perfilado automático de calidad
* Validaciones de integridad
* Detección de registros inválidos
* Consolidación y deduplicación de personas
* Priorización de fuentes
* Reglas de survivorship
* Enriquecimiento de información de contacto
* Monitoreo histórico de calidad
* Publicación de datasets operativos
* Generación de datasets analíticos
* Arquitectura modular y testeable

---

## Resultados del Proyecto

Estado actual del entorno de producción:

* Más de 800.000 registros procesados
* Más de 379.000 graduados únicos consolidados
* Más de 420.000 registros duplicados eliminados
* Enriquecimiento automático de emails
* Enriquecimiento automático de teléfonos
* Enriquecimiento automático de nacionalidad
* Monitoreo histórico de calidad

---

## Tecnologías Utilizadas

* Python
* Pandas
* Pytest
* Pathlib
* Logging
* Power Query
* Git

Conceptos aplicados:

* ETL
* Data Quality
* Data Profiling
* Data Validation
* Data Consolidation
* Deduplication
* Survivorship Rules
* Data Product Design
* Analytical Modeling

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

Dataset técnico consolidado que preserva la totalidad de los atributos disponibles y la trazabilidad de las fuentes.

Archivo principal:

```text
unified_graduates_dataset.csv
```

Documentación:

```text
docs/consolidation_logic.md
```

---

### Curated Layer

Dataset optimizado para análisis y reporting.

Archivo principal:

```text
graduates_curated.csv
```

Documentación:

```text
docs/curated_layer.md
```

---

### Publication Layer

Genera datasets estables para sistemas consumidores.

Archivo principal:

```text
base_graduados_unificada_latest.csv
```

Documentación:

```text
docs/publication_layer.md
```

---

### Monitoring Layer

Genera reportes históricos de calidad y cobertura.

Ejemplos:

* quality_history.csv
* quality_summary.csv
* enrichment_summary.csv
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
│
├── docs/
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

Ejecutar pipeline:

```bash
python main.py
```

---

## Privacidad y Datos

Este repositorio no incluye datasets reales.

Los datos utilizados en producción contienen información personal y se encuentran excluidos del control de versiones mediante reglas de Git.

Para más información:

```text
docs/privacy_review.md
docs/publication_rules.md
```

---

## Documentación

### Arquitectura

* docs/architecture.md
* docs/consolidation_logic.md
* docs/publication_layer.md
* docs/curated_layer.md

### Modelado Analítico

* docs/analytical_entities.md
* docs/analytical_dimensions.md
* docs/semantic_layer.md

### Gobierno y Publicación

* docs/privacy_review.md
* docs/publication_rules.md
* docs/public_release_checklist.md

### Roadmap

* docs/roadmap.md
* docs/technical_backlog.md

---

## Limitaciones Actuales

Actualmente el proyecto:

* No incluye integración con bases de datos
* No implementa procesamiento incremental
* No incluye orquestación automática
* No incluye CI/CD
* No distribuye datasets de ejemplo

Estas capacidades forman parte de futuras fases del roadmap.

---

## Estado Actual

Versión actual:

```text
v1.3 — Analytical Modeling Foundation
```

Estado:

```text
Operativo
Documentado
Auditado para publicación
Preparado para evolución hacia Database Integration
```

---

## Próximas Fases

### Phase 6 — Database Integration

* SQLite
* PostgreSQL
* SQL Transformations
* Incremental Processing

### Phase 7 — Analytics Engineering

* Data Contracts
* Data Lineage
* dbt Concepts
* Automated Testing Expansion

### Phase 8 — Production & Automation

* Scheduled Executions
* Monitoring
* Deployment Automation
* Cloud Integration

## Licencia

Este proyecto está bajo la licencia MIT.
