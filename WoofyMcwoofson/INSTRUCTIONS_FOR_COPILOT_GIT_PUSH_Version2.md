# 🐾 Copilot Launch & GitHub Push Instructions

**BoozeLee is heading to bed soon! Please launch and push all work to GitHub before end of day.**

---

## What to Do

1. **Commit All Changes**
   - Stage and commit:
     - FastAPI endpoint variant (e.g. `integrations/extra_endpoint_fastapi.py`)
     - Any updated or new docs (README, OAuth setup, onboarding, etc.)
     - `.env.example` or config templates (no real secrets)
   - Use a clear, semantic commit message (example:  
     `feat(api): add FastAPI /woof-extra endpoint, docs, onboarding updates`)

2. **Push to GitHub**
   - Push your branch to the remote repo:
     ```bash
     git push -u origin <your-branch-name>
     ```
   - If this is a new feature, use a branch like `feat/api-woof-extra-fastapi`.

3. **Open a Pull Request**
   - Go to GitHub and open a PR from your feature branch to `main` (or the default base).
   - In the PR description:
     - List what’s included (endpoints, docs, onboarding, etc.)
     - Copy/paste your compliance note:  
       _"Patch set is consistent and compliant. No further action required before PR."_
     - Add “Ready for review. BoozeLee requests push before EOD.”

4. **Tag for Review**
   - Assign to BoozeLee (or appropriate reviewers).
   - Add labels: `api`, `docs`, `fastapi`, `ready-for-review`

5. **(Optional) Request Additions**
   - If you want auth, error handling, or pagination in `/woof-extra`, mention it in the PR or ping BoozeLee.

---

## ⏰ Deadline

- **Push and open PR before BoozeLee goes to bed.**
- Confirm in chat or PR comments when done.

---

**Great work! This keeps the project on track and BoozeLee can sleep easy. 💤**