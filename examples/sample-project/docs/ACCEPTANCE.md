# Acceptance criteria

## User or operator jobs
| ID | Job |
| --- | --- |
| **US-001** | As a fictional support staff caller, I want to submit a request with a meaningful title so the process can return a ticket record. |
| **US-002** | As a fictional support staff caller, I want to list the requests held by this API instance so I can inspect work created during this process. |

## Acceptance cases
- **US-001 / REQ-001:** Given a fresh instance and valid JSON title, when a caller selects `POST /tickets`, then the handler returns 201 and a record with an `open` status. Verify with `TC-001`.
- **US-001 / REQ-001:** Given a blank title, when submitted, then the handler returns 422 `title_required`. Verify with `TC-002`.
- **US-001 / NFR-001:** Given a body of 16,385 bytes, when submitted, then the handler returns 413 before parsing. Verify with `TC-004`.
- **US-002 / REQ-002:** Given a ticket created in this instance, when the caller selects `GET /tickets`, then the result contains that ticket. Verify with `TC-001`.
- **US-002:** Given no records, when listed, then the result contains an empty `items` array. **Observed by code; a dedicated test is unresolved.**

## Sign-off and readiness
These criteria are for a fictional fixture. No stakeholder sign-off is recorded. Production readiness is blocked on authentication, retention and exposure decisions; this sample is not a production service.
