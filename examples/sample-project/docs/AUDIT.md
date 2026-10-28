# Audit methodology

## Audit states
- **PASS:** performed mechanical checks have no findings.
- **PASS_WITH_WARNINGS:** no mechanical blocker; non-blocking warnings need review.
- **BLOCKED:** required evidence or decisions are unavailable for a meaningful readiness call.
- **FAIL:** at least one hard-fail condition is confirmed.

## Scoring rubric
| Category | Weight | Evidence |
| --- | ---: | --- |
| Structural completeness | 15 | Exact 21 filenames and required headings. |
| Evidence and anti-hallucination | 20 | Provenance labels, explicit unknowns and no unsupported verification claims. |
| Contract/schema coherence | 15 | Requirements, interface, model and validation consistency. |
| Traceability | 20 | Unique definitions, resolved references, justified N/A — each absent surface has a technical reason — and coverage. |
| Security and secret hygiene | 15 | Secret scan and evidence-backed security boundaries. |
| Usability/operations/accessibility | 10 | Applicable flows, states, accessibility and operational facts. |
| Change hygiene | 5 | Real changelog and stable IDs. |

An item marked not applicable earns no automatic points; exclude it only when technically inapplicable and explain why. Do not redistribute the weight. This score is a documentation-quality measurement, not product readiness.

## Hard fails
Missing required document, exposed secret, fabricated verified test/deployment/compliance claim, duplicate or dangling critical ID, destructive unapproved overwrite, broken required tool command, or a production design presented as fact without evidence.

## Human review
Confirm claims against the source, assess threat coverage, architecture feasibility, accessibility and user acceptance. The checker cannot certify these. A high score does not approve the product.
