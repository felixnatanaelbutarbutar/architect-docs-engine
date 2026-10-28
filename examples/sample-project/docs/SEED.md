# Fixture and seed strategy

## Fixture inventory
`src/test_app.py` creates a fresh `TicketAPI` per test and uses synthetic titles. It does not load real customer records or print usable credentials.

## Safety and repeatability
The fixture is held in memory and initialized empty. There is no seed command, persistence, reset script or production database. Tests should use fictional data and fresh instances; never add credentials or customer exports.

## Not applicable or unresolved
- **Not applicable —** persistent database seed/migration fixtures: there is no database layer.
- **Unresolved —** safe data seeding for any future persistent environment.
