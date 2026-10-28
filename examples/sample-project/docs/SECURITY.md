# Security design

## Scope and evidence
This review covers only the synthetic local module `src/app.py`. Config labels the example internal; that label is not a certification or an access-control mechanism. No deployment or real data is in scope.

## Assets, actors and trust boundaries
- The only observed data asset is the in-memory ticket list owned by one `TicketAPI` instance.
- Input bytes are untrusted; the current caller is an in-process test/future adapter. There is no network or authenticated-principal boundary in the fixture.
- There is no tenant, user identity, tool, agent, or external integration to authorize.

## Threat model
- Input is untrusted JSON bytes passed to `TicketAPI.handle`.
- The current module has no network listener or authentication; if exposed through a transport, caller identity and authorization are unresolved.
- The process-local list has no tenant boundary and should not contain real customer information.

## Identity and authorization
**Unresolved —** define caller identity, role/object policy, and tenant isolation before adding an adapter or exposing the handler outside the process. There is no authentication or authorization implementation.

## Bots, abuse and resource limits
**Not applicable —** bot traffic and network rate limiting: this fixture has no network listener. The 16,384-byte body limit is an observed single bound, not general DoS protection. Any future adapter needs route/account/source limits, concurrency and cost controls based on deployment evidence, plus abuse tests.

## Agentic AI and tool safeguards
**Not applicable —** no LLM, agent, tool, prompt, retrieval, or MCP integration exists in the fixture.

## Data, secrets and operations
Observed checks: malformed UTF-8/JSON returns a client error; body size is capped at 16,384 bytes; title and description types are validated. Ticket data is ephemeral in memory. No secret store, encryption, audit log, rate limiter, backup, or retention control exists. No external dependency or SQL query layer is present. These observations are not an OWASP assessment or compliance claim.

## Verification and incident response
The four fixture unit tests cover malformed JSON, size limit, blank title, and create/list behavior. They do not test network exposure, authorization, bots, concurrency, persistence, or penetration resistance. No production incident owner or runbook is established.

## Open risks and response
- **Unresolved — high readiness risk:** define authentication, authorization, tenant boundary and data classification before exposing this handler to users or a network.
- **Unresolved:** define retention, deletion and incident handling before storing real requests.
- **Unresolved:** define adapter-level bot controls, resource ceilings, monitoring and recovery after a transport/deployment target is selected.
- **Not applicable —** cookie/session flags and RBAC/ABAC rules: no HTTP session or identity implementation exists.
- Do not deploy the fixture with customer data. If exposure occurs, isolate the process and review any adapter/storage added later; no production incident contact is specified.
