# 🐾 Copilot: PR Packaging & Automation Instructions (Final Checklist)

## 🦴 1. Branching & Staging

- **Create feature branch:**  
  ```bash
  git checkout -b feat/oauth-docs-and-fastapi
  ```
- **Add all new/updated files:**  
  - `docs/oauth/README.md`
  - `docs/oauth/CLIENT_REGISTRATION_SETUP.md`
  - `integrations/extra_endpoint_fastapi.py`
  - `.env.example`
  - `knowledge-vault/ONBOARDING.md`
  - (If FastAPI adoption: `docs/adr/ADR-001-adopt-fastapi.md`, update `CHANGELOG.md`, `docs/api/endpoints.md`, and `requirements.txt` if needed)

## 🦴 2. FastAPI Variant & ADR

- Ensure `/woof-extra` FastAPI endpoint is present in `integrations/extra_endpoint_fastapi.py`.
- If introducing FastAPI, add initial ADR:
  - `docs/adr/ADR-001-adopt-fastapi.md` (stub as per template)
- Update OpenAPI docs and endpoints reference if changed.
- Amend `CHANGELOG.md`:
  ```
  ## [Unreleased]
  ### Added
  - FastAPI /woof-extra implementation (integrations/extra_endpoint_fastapi.py)
  - ADR-001 (proposed) for FastAPI adoption
  - OAuth registration docs and onboarding checklist
  ```

## 🦴 3. Commit, Test & Push

- **Stage and run checks:**
  ```bash
  git add docs/oauth/README.md docs/oauth/CLIENT_REGISTRATION_SETUP.md integrations/extra_endpoint_fastapi.py .env.example knowledge-vault/ONBOARDING.md docs/adr/ADR-001-adopt-fastapi.md docs/api/endpoints.md CHANGELOG.md requirements.txt
  flake8 . || exit 1
  pytest -q
  git commit -m "docs(oauth): add OAuth registration guide, FastAPI endpoint variant, ADR-001, onboarding checklist, and env example"
  git push -u origin feat/oauth-docs-and-fastapi
  ```

## 🦴 4. Open PR

- **Title:**  
  `docs(oauth): OAuth registration docs, FastAPI endpoint, ADR-001, onboarding`
- **Body:**  
  - Added OAuth registration README & setup docs
  - Added FastAPI `/woof-extra` endpoint variant
  - Proposed ADR-001 for FastAPI architecture
  - Updated onboarding checklist and env example
  - Docs + spec synced: ✅  
  - Tests pass: ✅  
  - No secrets introduced: ✅  
  - Compliance note: Patch set is consistent and compliant. No further action required before PR.
- **Labels:**  
  `api, docs, feature, fastapi, ready-for-review`
- **Request:**  
  Review before EOD for BoozeLee

## 🦴 5. Automation & Onboarding (Required)

- **Update onboarding checklist:**
  - Add reminder to rotate secrets and update authorized URIs after every environment/domain change.
- **(Optional) Add pre-launch env check script:**  
  - Script to verify all required ENV variables are set before app launch.

## 🦴 6. (Optional) Orchestrator Log

- Append to orchestrator log (if present):
  ```
  2025-09-08 | copilot | added OAuth docs, FastAPI /woof-extra, ADR-001, onboarding
  ```

---

**Confirm in chat/PR when ready. Ping BoozeLee if you need auth middleware, error handling, or further automation.**

**All files and docs must be committed and PR opened before BoozeLee's EOD.**