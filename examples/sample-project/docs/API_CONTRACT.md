# Interface contracts

## Interface inventory
The observed integration boundary is the in-process Python method `TicketAPI.handle(method, path, body)` in `src/app.py`. There is **no network transport, server listener, base URL, authentication middleware or deployed endpoint**. Route strings below are dispatch selectors for this function, not public HTTP endpoints.

## Contracts
| ID | Selector | Input | Result |
| --- | --- | --- | --- |
| **EP-001** | `POST /tickets` | UTF-8 JSON object with string `title`; optional string `description`; maximum 16,384 body bytes. | 201 and `MODEL-001` record on success. |
| **EP-002** | `GET /tickets` | No body required. | 200 with `{"items": [...]}` from this instance. |

The handler returns `(status_code, response_dict)`. For EP-001, invalid JSON returns 400; invalid fields return 422; oversize body returns 413. Unknown method/path pairs return 404. Example values in this document are synthetic fixture data, not customer information.

## Errors and compatibility
| Code | Meaning | Applies |
| --- | --- | --- |
| 201 | Created | EP-001 |
| 200 | Listed | EP-002 |
| 400 | Malformed or non-UTF-8 JSON | EP-001 |
| 404 | Unknown method/path selector | Both |
| 413 | Body exceeds 16,384 bytes | EP-001 |
| 422 | Missing/blank title or non-string description | EP-001 |
| 401/403/409/429/500 | N/A — no auth, conflict, rate limiting, or server transport semantics are implemented. |

No pagination, versioning, retries or idempotency key exists. Ticket IDs are only unique within one handler instance.

## Not applicable or unresolved
- **Not applicable —** OpenAPI/network base path and transport-level auth: no network service is implemented.
- **Unresolved —** whether an external transport is needed and what authentication/authorization policy applies.
