# AI or developer prompts

## Runtime AI inventory
**Observed:** the fixture contains no LLM SDK, model configuration, runtime prompt registry, agent orchestration or MCP integration.

## Prompt and developer patterns
No runtime `PROMPT-###` records apply. A safe future code-review request may ask an agent to inspect only changed paths, cite evidence, label recommendations Proposed, and preserve unrelated text; that is a development pattern, not a prompt shipped by the application.

## Trust and evaluation
There is no model input/output boundary to evaluate. If an LLM is added, document prompt version, model/provider evidence, untrusted content handling, output schema, refusal/fallback and evaluation data before release.

## Not applicable or unresolved
- **Not applicable —** runtime prompt contracts and model evaluations: no LLM orchestration exists in the fixture.
- **Unresolved —** no AI capability is requested by the fixture brief.
