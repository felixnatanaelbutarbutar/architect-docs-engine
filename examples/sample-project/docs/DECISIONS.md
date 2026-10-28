# Architecture decisions

## Decision records

### **ADR-001** — Keep the fixture store process-local
- **Status:** Proposed — approval required.
- **Date:** Not recorded.
- **Context:** `src/app.py` stores ticket dictionaries in a list owned by each `TicketAPI` instance.
- **Options:** retain memory-only behavior for this demonstration; or select durable storage after recovery and retention needs are known.
- **Rationale:** the fixture brief is deliberately small and does not request persistence.
- **Trade-offs:** records disappear when the instance ends; no backup or cross-process sharing exists.
- **Evidence:** `project-brief.md`, `src/app.py`.
- **Impacted docs:** [Data model](DATA_MODEL.md), [Operations](OPERATIONS.md), [Security](SECURITY.md), [Acceptance](ACCEPTANCE.md).
- **Revisit when:** a deployment or data-retention requirement is approved.

## Proposed decisions
Authentication and a network server are intentionally undecided; no ADR claims them as implemented.

## Revisit conditions
Review ADR-001 when persistence, recovery, multiple workers, or real customer data become in scope.
