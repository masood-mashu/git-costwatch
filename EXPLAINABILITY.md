# Explainability, Auditability & Decision Logic: GitCostWatch

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitCostWatch**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitCostWatch** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **AWS**: AWS Cost and Usage Reports (CUR) and GCP Cloud Billing BigQuery exports.
- **CloudWatch**: CloudWatch / Stackdriver resource utilization metrics (CPU, IOPS, Network).
- **Organization**: Organization FinOps budget allocations and tagged ownership rosters.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **detect_spend_anomalies**: Uses `spend-anomaly-detector` to calculate computes daily spend z-score relative to rolling historical baseline.
   - **reclaim_idle_resources**: Uses `idle-resource-reclaimer` to calculate audits compute and storage for zero-utilization thresholds across multi-cloud accounts.
   - **score_reservation_coverage**: Uses `reservation-coverage-scorer` to calculate calculates percentage of eligible compute instances covered by ris or savings plans.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When billing or infrastructure metrics are submitted, the agent runs spend_anomaly_detector, idle_resource_reclaimer, and reservation_coverage_scorer. If spend is on budget and coverage >= 75%, it returns APPROVED. If anomalies between 15% and 30% are detected, it issues NEEDS_REVIEW. If uncontrolled runaway spend (> 50% spike) or massive unattached disks are found, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on statistical standard deviation models.
- **Requires**: Requires billing export latency windows of at least 6 hours for accurate ingestion.
- **Does**: Does not terminate running primary compute instances without human approver sign-off.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
