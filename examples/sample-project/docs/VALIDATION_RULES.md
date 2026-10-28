# Validation rules

## Input inventory
`TicketAPI.handle(method, path, body)` receives a byte string for `POST /tickets`. Evidence: `src/app.py`.

## Validation rules
| Field / input | Rule | Result |
| --- | --- | --- |
| Body | More than 16,384 bytes is rejected before decode/parse. | 413 `body_too_large` |
| JSON | Decode as UTF-8 and parse as JSON object. | 400 `invalid_json` for decode or parse failure |
| `title` | Must be a string with non-whitespace content; stored value is trimmed. | 422 `title_required` |
| `description` | Optional; if present must be a string. | 422 `description_must_be_text` |

These rules are observed in the fixture handler. No Unicode normalization or title-length maximum is implemented.

## Errors and accessibility
Errors are machine-readable dictionary values. There is no visual interface, localized message catalog or accessible UI error association. A future user-facing adapter should translate codes into clear, field-associated messages without weakening server-side checks.

## Not applicable or unresolved
- **Not applicable —** client-side validation: no client or visual UI exists in the fixture.
- **Unresolved —** title maximum length and accepted whitespace/Unicode policy: no business rule was supplied.
