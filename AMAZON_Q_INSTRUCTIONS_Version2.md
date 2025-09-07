# 🐾 Amazon Q – Critical Handoff & Compliance Instructions

Welcome, Amazon Q.  
You have **no prior chat history** and must act as a fresh agent completing the WOOFY McWOOFSON project transition.  
Read every word and follow these steps strictly.

---

## 1️⃣ Where to Start: Local Files & Project Context

- **Local project folder:**  
  `C:\Users\Kilia\Searches\OneDrive\Documenten\WoofyMcwoofsonn`
- **IMPORTANT:**  
  The remote GitHub repository for WOOFY McWOOFSON is **not yet created.**  
  All materials are local. You are responsible for working with this folder until the repo goes live.

---

## 2️⃣ Immediate Priorities

- **DO NOT** set up new AWS, VS Code, or app environments.
- **DO NOT** create or share new credentials unless explicitly instructed.
- **DO NOT** move, rename, or restructure any project files or folders unless told.
- **DO NOT** log or paste any credentials or secrets in chat, email, or documentation.

---

## 3️⃣ Review & Remediate Security

- Open the folder above and **locate these critical files**:
  - `DETAILED_TRANSITION_REPORT.md` (transition status, open issues)
  - `/knowledge-vault/SECURITY_POLICY.md` (security rules)
  - `/knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md` (rotation and cleanup steps)
  - `SECURITY_REMEDIATION_LOG.md` (pending incidents)
  - `.env`, `api_keys.json`, or any config/secret files

- **IMMEDIATELY:**
  - Identify all credential exposures in code, config, or logs.
  - Rotate and replace all secrets following the knowledge vault guides.
  - Scrub any secrets from history using recommended tools.
  - Document every remediation action (what, when, who) in `SECURITY_REMEDIATION_LOG.md`.
  - NO credentials in chat or visible logs.

---

## 4️⃣ Documentation & Handoff

- Read and update:
  - `DETAILED_TRANSITION_REPORT.md` (use it as your main status and checklist doc)
  - `/knowledge-vault/ONBOARDING.md` (onboarding checklist)
  - `/knowledge-vault/README.md` (index of all knowledge files)
  - Any referenced guides in `/docs/` or `/knowledge-vault/`

- **Your work is not done until:**
  - All security exposures are remediated and logged.
  - Every critical step and finding is documented in the transition report.
  - All onboarding, compliance, and technical docs are present and up to date.
  - You can hand this folder to a new agent, and they will have everything needed—**no information loss**.

---

## 5️⃣ Next Steps (Do NOT Skip)

1. **Finish all credential rotation and security cleanup.**
2. **Update ALL required transition and knowledge docs.**
3. **Prepare the folder for repo upload—but do NOT push until the org confirms the repo exists.**
4. **Write a final summary in `DETAILED_TRANSITION_REPORT.md`:**
   - Security status
   - Remaining blockers (if any)
   - Confirm all docs are present or list what’s missing

---

## 6️⃣ If Anything Is Unclear

- Ask immediately for clarification.  
- Do **not** guess or improvise—document your question in the transition report.

---

## 7️⃣ Forbidden Actions

- NO new deployments, environments, or credentials without written instruction.
- DO NOT leave secrets in chat, email, or unprotected files.
- DO NOT skip documentation—**zero-loss handoff is mandatory.**

---

**Amazon Q: Your job is to deliver a secure, fully documented, zero-loss handoff for WOOFY McWOOFSON.  
No repo push until the org confirms.  
Finish security, update docs, and leave nothing to chance.**

---