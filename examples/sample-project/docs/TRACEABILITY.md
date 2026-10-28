# Requirements graph

## Coverage graph
Edges are many-to-many: one user journey covers create/list operations; one unit test covers multiple requirements.

| Requirement | Story | Interface | Model | UI / flow | Test |
| --- | --- | --- | --- | --- | --- |
| [REQ-001](PRD.md) | [US-001](ACCEPTANCE.md) | [EP-001](API_CONTRACT.md) | [MODEL-001](DATA_MODEL.md) | N/A — no visual screen exists; the handler is called in process. [FLOW-001](UX.md) | [TC-001](TESTING.md), [TC-002](TESTING.md), [TC-003](TESTING.md) |
| [REQ-002](PRD.md) | [US-002](ACCEPTANCE.md) | [EP-002](API_CONTRACT.md) | [MODEL-001](DATA_MODEL.md) | N/A — no visual screen exists; the handler is called in process. [FLOW-001](UX.md) | [TC-001](TESTING.md) |
| [NFR-001](PRD.md) | US-001 | [EP-001](API_CONTRACT.md) | N/A — input-size guard does not introduce a separate entity. | N/A — no visual screen; request is dispatched in process. | [TC-004](TESTING.md) |

## Non-applicable mappings
- UI surface: **N/A —** no UI source, browser assets or screen is present. Do not invent a screen ID.
- Durable database and schema: **N/A —** the current record is an in-memory object; see [DATA_MODEL](DATA_MODEL.md).
- Network API surface: **N/A —** EP-001/EP-002 describe in-process selectors only, not live HTTP endpoints.

## Unresolved mappings
- Authentication/authorization has no requirement or implementation mapping; first define the trust boundary before any external exposure.
- A dedicated empty-list test and malformed-JSON test are not in the current test file; add them if those edge cases become release gates.

## Audit counts
Last recorded traceability check: **2026-10-28 16:32 UTC**. Counts: 14 defined, 14 referenced, 14 covered, 0 orphaned, 0 dangling, 0 duplicate, 10 non-applicable mappings with technical reasons, and 21 unresolved statements. See the detailed run record in [_AUDIT_REPORT](_AUDIT_REPORT.md).
