# Contributing

Contributions that improve safe scanning, evidence quality, traceability, portability or documentation templates are welcome.

## Local workflow

1. Use Python 3.11+; the core tools use only the standard library.
2. Make focused changes and keep the synthetic example clearly labeled as fictional.
3. Run `python -m unittest discover -s tests -v` from the repository root.
4. Run `python .agents/skills/architect-docs-engine/scripts/cli.py validate-skill`, `audit --project ./examples/sample-project`, and `traceability --project ./examples/sample-project`.
5. Update manifest, templates, docs blueprint and example suite together when changing the 21-file contract.

## Style and review

- Keep Python cross-platform and read-only by default; never execute inspected project code.
- Add tests for path safety, ID parsing, redaction or CLI behavior that changes.
- Keep docs concise and evidence-based; distinguish observed facts, fixture data, proposals and unresolved items.
- Do not add a dependency unless a checked-in declaration and offline rationale justify it.
- Use semantic versions and Keep a Changelog conventions. Never add fake test results, commits, badges or CI states.

Pull requests should summarize behavior, safety impact, tested commands and remaining limitations. Reviewers should inspect fixture changes for secrets and verify that updates preserve human-authored text.
