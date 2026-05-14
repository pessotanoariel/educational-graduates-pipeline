# Week 02 — Data Quality and Reusable Validation

## Objective

Transform the current profiling logic into reusable validation components capable of processing multiple educational datasets with consistent quality checks.

The focus of this week is not adding complexity, but improving automation, reusability and data quality visibility.

---

## Main Goals

- Create reusable profiling functions
- Add initial data quality validations
- Process multiple datasets automatically
- Generate structured validation outputs
- Improve logging and traceability

---

## Day 1 — Reusable Profiling Functions

- [X] Create reusable profiling functions
- [X] Separate profiling logic from execution flow
- [X] Create summary statistics outputs
- [ ] Reduce duplicated profiling code

---

## Day 2 — Initial Data Quality Checks

- [X] Validate null values
- [X] Validate duplicate documents
- [X] Detect invalid document lengths
- [X] Log quality warnings

---

## Day 3 — Multi-Source Processing

- [X] Iterate automatically through datasets in `data/raw`
- [X] Skip unsupported files safely
- [X] Process datasets sequentially
- [X] Improve execution logging

---

## Day 4 — Validation Outputs

- [ ] Export invalid records
- [ ] Generate profiling summaries
- [ ] Save outputs into `data/output`
- [ ] Create basic quality reports

---

## Day 5 — Refactor and Cleanup

- [ ] Refactor repeated logic
- [ ] Improve module organization
- [ ] Review naming conventions
- [ ] Update project documentation

---

## Expected Outcome

By the end of Week 02, the pipeline should:

- Process multiple datasets automatically
- Detect basic data quality issues
- Generate reusable profiling outputs
- Produce structured logs and validation artifacts
- Have cleaner reusable validation modules
  