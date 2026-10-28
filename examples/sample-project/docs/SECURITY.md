# Security design

## Scope and evidence
This review covers only the synthetic local module `src/app.py`. Config labels the example internal; that label is not a certification or an access-control mechanism. No deployment or real data is in scope.

## Threat model
- Input is untrusted JSON bytes passed to `TicketAPI.handle`.
- The current module has no network listener or authentication; if exposed through a transport, caller identity and authorization are unresolved.
- The process-local list has no tenant boundary and should not contain real customer information.

## Controls and data handling
Observed checks: UTF-8/JSON parse errors return a client error; body size is limited to 16,384 bytes; title and description types are validated. No secret store, encryption, audit log, rate limiter, authorization matrix, backup or retention control exists. No external dependency is present in the fixture.

Relevant OWASP-style concerns are broken access control if an adapter exposes the handler, resource exhaustion beyond the body-size guard, and unsafe handling of data if persistence is later added. There is no SQL query layer or third-party runtime dependency to assess in this fixture. These observations are not an OWASP assessment or compliance claim.

## Open risks and response
- **Unresolved — high readiness risk:** define authentication, authorization and data classification before exposing this handler to users or a network.
- **Unresolved:** define retention, deletion and incident handling before storing real requests.
- **Not applicable —** cookie/session flags and RBAC/ABAC rules: no HTTP session or identity implementation exists.
- Do not deploy the fixture with customer data. If exposure occurs, isolate the process and review any adapter/storage added later; no production incident contact is specified.
