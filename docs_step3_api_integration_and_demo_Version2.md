# 🦴 Step 3: Integration & Demo – Perplexity, watsonx, Gemini, etc. 🐾

**After security closure, follow this order for integrations and demos.**

---

## 1. Perplexity Integration
- [ ] `PERPLEXITY_API_KEY` present in `.env`/GitHub Secrets
- [ ] Run demo:
  ```
  python integrations/perplexity/demo.py
  ```
- [ ] Document and test results

---

## 2. IBM watsonx Integration
- [ ] `WATSONX_API_KEY` and `WATSONX_PROJECT_ID` set
- [ ] Run demo:
  ```
  python integrations/watsonx/demo.py
  ```
- [ ] Document and test results

---

## 3. Gemini Integration (if enabled)
- [ ] `GEMINI_API_KEY` set
- [ ] Add `/integrations/gemini/` module if not present
- [ ] Document setup in `/docs/integrations/gemini.md`
- [ ] Update `README.md`, `CHANGELOG.md`, `SECURITY.md`
- [ ] Run demo/tests

---

## 4. General Security Reminders
- [ ] No secrets in code, logs, or docs
- [ ] All test results and integration steps are documented in the knowledge vault

---

**Block and escalate if any compliance/security issues arise during integration. 🐾**