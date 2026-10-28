# Product requirements

## Problem and evidence
This is a fictional sample project. The supplied [fixture brief](../project-brief.md) describes a small internal support-ticket workflow. The inspected implementation is `src/app.py`; it accepts method/path/body values in process and contains no network listener.

## Users and constraints
- Fictional support staff use an in-process caller or test harness. **User-specified fixture.**
- Ticket data exists only for the lifetime of a `TicketAPI` instance. **Observed:** `src/app.py`.
- Authentication, persistent storage, production deployment and customer-data use are out of scope for this fixture; production needs remain unresolved.

## Scope
In scope: validate a title, create an in-memory ticket, list tickets, and enforce a 16,384-byte create-body limit. Out of scope: network serving, account management, database persistence, UI, email notifications and real customer records.

## Functional requirements
| ID | Priority | Requirement | Status / evidence |
| --- | --- | --- | --- |
| **REQ-001** | Must | A caller can create a ticket with a non-blank title and optional text description; success returns a ticket record. | User-specified fixture; implemented in `src/app.py`. |
| **REQ-002** | Must | A caller can list tickets held by the current API instance. | User-specified fixture; implemented in `src/app.py`. |

## Non-functional requirements
| ID | Requirement | Verification |
| --- | --- | --- |
| **NFR-001** | The create handler rejects a body larger than 16,384 bytes before JSON parsing. | **Observed:** byte-length guard in `src/app.py`; `TC-004` checks boundary overflow. This is a fixture guard, not a service capacity claim. |

## Open decisions
- **Unresolved — authentication:** the brief does not define caller identity or permissions. Evidence needed: deployment context, user roles and data sensitivity.
- **Unresolved — persistence/retention:** the current list is volatile. Evidence needed: recovery expectations and retention policy.
- **Unresolved — network transport:** no server adapter is implemented. Evidence needed: intended runtime and transport.
