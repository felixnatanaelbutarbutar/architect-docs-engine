# Test strategy

## Evidence and commands
`src/test_app.py` uses Python `unittest`. From the fixture root, run `python -m unittest discover -s src -v`. The result status below reflects the last recorded execution of that command only.

## Test cases
| ID | Preconditions | Action | Expected result | Layer / status |
| --- | --- | --- | --- | --- |
| **TC-001** | Fresh `TicketAPI`. | POST valid title, then GET. | 201 with ticket; 200 list contains it. | Unit; run with fixture suite. |
| **TC-002** | Fresh `TicketAPI`. | POST blank title. | 422 `title_required`. | Unit; run with fixture suite. |
| **TC-003** | Fresh `TicketAPI`. | POST malformed JSON. | 400 `invalid_json`. | Unit; run with fixture suite. |
| **TC-004** | Fresh `TicketAPI`. | POST body of 16,385 bytes. | 413 `body_too_large`. | Unit; run with fixture suite. |

## Last execution
- **2026-10-28 17:04 UTC:** `python -m unittest discover -s src -v` from the sample-project root — PASS, 4 tests.
- The repository-level suite and its Windows symlink-specific skips are recorded in [_AUDIT_REPORT](_AUDIT_REPORT.md).

## Coverage and nonfunctional checks
The tests are deterministic but do not measure performance, concurrency, network behavior, accessibility or security certification. No coverage threshold or benchmark is configured.

## Not run
Network/API contract, persistence, concurrency, and deployment tests are **Not run** because those components do not exist. Do not interpret local unit tests as release validation.
