# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitCostWatch** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitCostWatch Automation Engine`
* **Responsibilities**:
  * Aggregates billing telemetry, identifies idle resources, and calculates committed-use optimization opportunities.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitCostWatch Verification & Policy Enforcer`
* **Responsibilities**:
  * Validates business unit chargeback tags and checks SLA constraints before suggesting scale-down.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Cloud Infrastructure Director / VP of Engineering (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
