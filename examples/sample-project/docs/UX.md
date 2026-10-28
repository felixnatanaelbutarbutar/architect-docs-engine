# User journeys and states

## Users and tasks
The fixture brief names fictional support staff as users. The present interaction is developer/operator-level because there is no network client or UI.

## Journey flows
**FLOW-001** — Create then list a ticket in one API instance (fixture):
```mermaid
flowchart LR
  Caller -->|POST selector| Validate[Validate body and title]
  Validate -->|valid| Store[Append to instance list]
  Validate -->|invalid| Error[Return 400, 413 or 422]
  Store -->|GET selector| List[Return current instance items]
```

## Form placement and overlays
**Not applicable —** the fixture has no visual forms, route, modal dialog, or popup. If a UI is later proposed, use a normal page/route for a primary or multi-field form and inline placement for short contextual tasks; do not open a modal/popup form by default.

## Interaction states
- Create: valid input returns a record; invalid JSON/field or oversize body returns an error object.
- List: returns an empty list before creation and records after creation; no pagination or persistence exists.
- Unknown selector: returns 404. Network loading, retry and offline UI states are absent because no client is implemented.

## Accessibility and recovery
**Not applicable —** keyboard and screen-reader screen behavior: there is no visual client. **Unresolved —** an eventual client must specify accessible form errors, focus movement, confirmation and retry behavior.
