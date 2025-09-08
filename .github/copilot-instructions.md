# 🤖 WOOFY McWOOFSON AI Assistant Operating Guide

Author: Automation Layer
Status: Draft v1
Last Updated: 2025-09-07

---
## 1. Mission
Provide secure, compliant, auditable assistance for the WOOFY platform: documentation upkeep, test expansion, security hygiene, API evolution, and workflow reliability — without ever exposing or hardcoding secrets.

---
## 2. Architecture Snapshot
- Runtime Pattern: Serverless (AWS Lambda + API Gateway planned) with supporting security scans & policy docs.
- Current Code Surface: `integrations/lambda_woofy_handler.py` (hello stub) + tests in `tests/`.
- API Spec: `integrations/openapi.yaml` + docs in `docs/api/` (endpoints, authentication, examples).
- Security & Compliance: Policies in `knowledge-vault/` and `docs/compliance/`.
- Workflows: `.github/workflows/*.yml` (lint/test, compliance, deploy placeholder, token audit).

Planned expansions must update: OpenAPI spec, `docs/api/*`, relevant tests, and CHANGELOG.

---
## 3. Golden Rules (DO / DO NOT)
DO:
- Keep secrets out of repo. Enforce secret patterns via `tests/test_security.py`.
- Update docs & tests in same PR as code changes.
- Add entries to `CHANGELOG.md` for user-impacting changes.
- Respect zero-touch credential policy (no manual token insertion).
- Use small, focused PRs with clear titles.
- Tag security-sensitive changes with label: `security`.

DO NOT:
- Store API keys, tokens, passwords, or raw credentials anywhere.
- Invent architecture not already ratified in docs without creating an ADR (Architecture Decision Record) stub in `docs/architecture/`.
- Modify historical versioned snapshots (create a new version or consolidate via archive note).

---
## 4. Branching & PR Flow
- Base Branch: `main` (protected; all changes via PR).
- Feature Branch Naming: `feat/<scope>-<short>`
- Fix Branch Naming: `fix/<area>-<issue#>`
- Security Patch: `sec/<vector>-<short>`
- Documentation Only: `docs/<section>-<short>`

PR Checklist (auto + human):
1. Tests pass (CI).
2. Lint passes.
3. No secrets added (security test).
4. Updated docs (API/spec/policy if needed).
5. CHANGELOG updated (if externally visible change).
6. Labels: `feature`, `bug`, `security`, `docs` as appropriate.

---
## 5. Workflows Overview
| Workflow | File | Purpose | Key Triggers |
|----------|------|---------|--------------|
| Lint & Test | `woofy-lint-test.yml` | Run lint + unit tests | PR |
| Compliance | `woofy-compliance.yml` | Policy / structure checks (placeholder) | PR / Schedule |
| Deploy | `woofy-deploy.yml` | Deployment scaffold (not fully wired) | Manual / Tag |
| Enterprise CI | `enterprise-ci.yml` | Aggregated enterprise tasks | PR |
| Token Access Check | `token-access-check.yml` | Validates token environment & permissions | PR |

Any new workflow must be: documented here + minimal + idempotent.

---
## 6. Documentation Update Protocol
When adding/modifying an endpoint:
1. Update `integrations/openapi.yaml`.
2. Sync `docs/api/endpoints.md`, `authentication.md` (if auth changes), and `examples.md`.
3. Add/adjust tests in `tests/`.
4. Update `CHANGELOG.md` section: `### Added`/`### Changed`.
5. Mention in PR body: `Docs+Spec synced: yes`.

---
## 7. Security Guardrails
- Secret Pattern Enforcement: Extend patterns only in `tests/test_security.py` (never relax without security label).
- Credential Lifecycle: Refer to `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`.
- Incident Documentation: Record in `SECURITY_TEST_RESULTS.md` + follow `docs/compliance/incident-response.md`.
- Data Retention: Respect `docs/compliance/data-retention.md` when proposing storage features.

If a security-sensitive change is detected (auth logic, scanning, data retention), add a SECURITY NOTE block in PR.

---
## 8. Communication & Triggers
- BADABING: Triggers a light-hearted acknowledgment (do not overuse; keep professional context).
- Orchestrator Log: Major automation events appended to `ORCHESTRATOR_COMMUNICATION_LOG.md`.
- Transition Report: Significant cross-agent coordination steps -> `DETAILED_TRANSITION_REPORT.md`.

---
## 9. Testing Standards
Minimum per feature:
- Happy path test.
- Failure mode test (bad input, unauthorized, or error path).
- Security regression test (if applicable).

Future: Add coverage tracking (placeholder). Avoid test brittleness; prefer deterministic inputs.

---
## 10. Linting & Style
- Python: Use `flake8` (add to `requirements.txt`).
- YAML: Keep two-space indent.
- Markdown: Favor concise sections; emoji acceptable but purposeful.
- Naming: snake_case for Python; kebab-case for files except Python modules.

---
## 11. Adding Dependencies
1. Justify in PR body (purpose + security review note).
2. Pin versions in `requirements.txt`.
3. Avoid heavy frameworks unless architecture doc updated.

---
## 12. Common Tasks (Playbooks)
Add new endpoint:
- Create branch `feat/api-new-endpoint`.
- Implement handler (or stub) under `integrations/`.
- Update OpenAPI + docs + tests + CHANGELOG.
- Run local: lint + pytest.
- Open PR with checklist confirmation.

Tighten security scan:
- Update `tests/test_security.py` with new regex.
- Document rationale in PR.
- Increment SECURITY section in CHANGELOG (Changed).

Archive old doc version:
- Move outdated file to `archive/` (create if absent) or append "(Archived YYYY-MM-DD)" header tag.

---
## 13. Escalation Paths
- Security Concern -> label `security` + add SECURITY NOTE.
- Compliance Gap -> open issue with category `compliance`.
- Architecture Change -> create ADR stub: `docs/architecture/adr-<number>-<title>.md`.

---
## 14. Future Enhancements (Backlog Hints)
- Add coverage report & badge.
- Add dependency vulnerability scan workflow.
- Implement deploy automation gated by security scan pass.
- Introduce ADR index file.

---
## 15. Verification Footer
If you're an AI agent consuming this file, confirm in your operation log: "Copilot instructions loaded v1".

End of file.
