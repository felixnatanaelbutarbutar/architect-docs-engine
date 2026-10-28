# Engineering execution plan

## Current state
Observed: an in-process dispatch method, process-local list, input checks and four unit tests exist in `src/`. The memory-only approach is recorded as [ADR-001](DECISIONS.md). No web server, database, UI or deployment configuration is implemented.

## Milestones
1. **Fixture behavior (implemented):** create/list in-memory tickets and validate payload; tests cover create/list, blank title and body size.
2. **Identity and exposure review (proposed):** decide whether network access is required; if yes, define authentication, authorization, threat model and transport before writing an adapter.
3. **Persistence review (proposed):** decide recovery and retention needs; then select a schema and migration approach with deletion tests.
4. **Operational readiness (proposed):** define supported runtime, deploy/rollback, logs and incident process only after a deployment target is selected.

## Verification and rollback
From fixture root, `python -m unittest discover -s src -v` verifies the local handler. No deploy or migration command exists. Current fixture changes can be reverted in source control; no rollback procedure for a deployed service is claimed.

## Open dependencies
Authentication, data retention, transport and deployment decisions are prerequisites for any production-facing service.
