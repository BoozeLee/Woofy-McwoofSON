# 🦴 WOOFY McWOOFSON: Copilot Detailed Execution Plan

---

## Copilot Task List (Expanded & Detailed)

This plan integrates your last three queries, including instructions to work efficiently (less feedback, more action), and the latest TODO list.

---

### Copilot Workflow Guidance

- **Batch tasks:** Work through several related items before pausing for feedback.
- **Feedback intervals:** Only pause at major milestones or if blockers/uncertainties arise.
- **Status updates:** Summarize progress after a phase, not after every micro-task.

---

## Current TODO List (Step-by-Step with Details)

### 1. **Create ADR Structure**
   - Add `docs/architecture/adr/README.md` explaining the ADR process for this repo.
   - Add `docs/architecture/adr/ADR-0001-serverless-baseline.md`:
     - Describe the serverless baseline decision (e.g., AWS Lambda, API Gateway, CloudFormation).
     - Reference standards and rationale.
   - Link ADR directory from main `README.md`.

### 2. **Refactor Lambda Handler**
   - Update `lambda_woofy_handler.py`:
     - Accept an `action` in the input (e.g., "hello", "ping").
     - Return appropriate response for known actions.
     - Return error JSON for unknown/malformed input.
   - Ensure code is clear, commented, and security-compliant.

### 3. **Update Positive Test Case**
   - In `tests/test_api.py`:
     - Ensure the main positive test matches the new handler contract (sends `action=hello`).
     - Check expected output.

### 4. **Add Negative Tests**
   - Create `tests/test_lambda_woofy_handler_negative.py`:
     - Test for type errors (e.g., missing/incorrect `action` type).
     - Test unknown actions and malformed input.
     - Assert error JSON is returned.

### 5. **Enhance Security Test**
   - In `tests/test_security.py`:
     - Add scan to check all markdown docs (including token guides) for exposed secrets/tokens.
     - Reference `knowledge-vault/SECURITY_POLICY.md` for compliance criteria.

### 6. **Update README**
   - Add section referencing the ADR directory and process.
   - Mention security scan coverage (markdown/token guide) in documentation.

### 7. **Update CHANGELOG Unreleased**
   - Move all new features and planned work under "Unreleased".
   - Add entries for:
     - ADR directory / ADR-0001
     - Handler refactor
     - Test improvements (positive/negative/security)
     - Documentation updates

### 8. **Run Coverage**
   - Execute full test coverage.
   - Ensure all tests pass and coverage is sufficient.
   - Address and document any failures immediately.

### 9. **Final Summary**
   - Summarize all changes made.
   - List any remaining user-only credential rotations or manual actions.
   - Post summary as part of the PR or in the main thread.

---

## Efficiency and Workflow Instructions (from previous queries)

- **Copilot should:**
  - Do more tasks before feedback, stopping only at major checkpoints.
  - Provide clear, concise batch updates after several steps are complete.
  - Only request feedback when necessary (blockers, big design questions, handoff points).
- **Amazon Q:** Reviews security and compliance *after* Copilot completes implementation phases.

---

## Immediate Actions (From Previous Checklists)

- Configure AWS credentials in VS Code (if needed for local tests).
- Install AWS Toolkit extension (if relevant).
- Deploy infrastructure (if required for end-to-end testing).
- Test API endpoints and Lambda functions post-refactor.
- Activate monitoring and cost alerts (if live AWS resources are in use)—document in ADR or README.

---

## Security & Compliance Reminders

- **Do not commit credentials, tokens, or secrets.**
- **Rotate and document any test/exposed credentials, per `knowledge-vault/SECURITY_POLICY.md`.**
- **Log all remediation, audit, and security actions.**
- **No deployment or handoff until all security blockers are cleared.**

---

**Say “go” to begin executing from Item 1 with this detailed, efficiency-focused workflow.**