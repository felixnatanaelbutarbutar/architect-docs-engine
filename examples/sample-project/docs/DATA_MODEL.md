# Data model

## Data inventory
There is no database or migration layer. `TicketAPI._tickets` is an in-memory Python list observed in `src/app.py`.

## Entities and relationships
**MODEL-001** — Ticket record (in-memory dictionary)

| Field | Python type | Required | Evidence / rule |
| --- | --- | --- | --- |
| `ticket_id` | `str` | yes | Generated as `T-0001`, incrementing within one instance. |
| `title` | `str` | yes | Trimmed, non-empty input. |
| `description` | `str` | yes | Defaults to an empty string; if supplied it must be text. |
| `status` | `str` | yes | Initialized to `open`. |
| `created_at` | ISO-8601 UTC string | yes | Created by `datetime.now(timezone.utc)`. |

The record is not persisted and has no database key/index/foreign-key semantics. A diagram is omitted because there are no relational entities.

## Lifecycle and retention
Records live in one object and are lost when that instance is discarded. There is no deletion, retention job, backup or migration logic. This is observed fixture behavior, not an acceptable production retention policy.

## Not applicable or unresolved
- **Not applicable —** database tables, SQL types, indexes and migrations: no database code or migration files exist.
- **Unresolved —** production retention/deletion and durable schema: define before storing real support data.
