# 🦴 Next Steps: Audit & Architecture Enhancements

## 1. Add Coverage Tooling
- Integrate [`coverage.py`](https://coverage.readthedocs.io/) into the Python workflow.
- Update Makefile and CI to include `coverage run -m pytest` and `coverage report`.
- Upload the HTML or XML coverage report as a GitHub Actions artifact.
- Add a Shields.io coverage badge (see `/branding/` for custom SVGs).

## 2. Dependency Vulnerability Scanning
- Add a CI workflow step for `pip-audit` or `safety` to scan dependencies.
- (Initially set to warn, not block, PRs.)
- Document results and process in `scripts_README.md`.

## 3. Expand file_audit.py Features
- Add a `--json` flag to output audit results in machine-readable JSON.
- Update `scripts_README.md` with usage and output example.

## 4. Architecture Decision Records (ADR)
- Create `/architecture/adr/` directory.
- Add an index file (`README.md`) listing all ADRs.
- Write ADR-0001: "Serverless baseline architecture" using [Michael Nygard’s template](https://adr.github.io/madr/).
- Document the process in the knowledge vault.

## 5. Negative Test Cases for Lambda
- Expand tests for `lambda_woofy_handler.py` to cover invalid event shapes, missing keys, and error flows.
- Ensure coverage for edge cases and document rationale.

## 6. Archive/Consolidate Legacy Docs
- Use the archival script (`make audit` or manual run) to identify and move/prune versioned markdown files.
- Document results in a changelog or summary file.

---

**Prioritize in this order unless an urgent blocker is discovered.  
Check off each when complete and update team/knowledge vault accordingly.**

---