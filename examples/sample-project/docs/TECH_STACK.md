# Technology choices

## Observed stack
- Python source uses standard-library `json`, `datetime`, `typing`, and `unittest`. Evidence: `src/app.py` and `src/test_app.py`.
- No package manifest, dependency lock, framework, database driver, web server or CI workflow exists in the fixture.
- Example configuration labels the runtime policy `Python 3.11+`; this is supplied fixture configuration, not a tested minimum.

## Proposed choices
- **Proposed — approval required:** keep the demonstration on the Python standard library until a deployment/runtime requirement justifies a server framework or persistence package.
- The config's Python 3.11+ value should be treated as an intended compatibility policy; no version matrix was executed for this documentation fixture.

## Alternatives and risks
- A network adapter could expose the dispatch method, but transport, authentication and deployment are not specified. Adding it would change the security boundary.
- Durable storage could replace the in-memory list, but schema, retention, backup and migration requirements are unresolved.

## Support and upgrade policy
No lockfile or support matrix is present. **Unresolved:** confirm the supported Python range and run the test suite across that matrix before claiming compatibility.
