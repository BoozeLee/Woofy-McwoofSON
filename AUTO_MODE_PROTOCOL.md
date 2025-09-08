# 🚦 WOOFY McWOOFSON AUTO-MODE PROTOCOL

---

## Purpose
Allow Amazon Q and Copilot to continue safe, productive work autonomously when the Orchestrator (project owner) is unavailable for real-time approvals.

---

## ✅ AUTO-APPROVED ACTIONS (Proceed Without Orchestrator)

- Documentation updates and improvements
- Code quality refactors (no breaking changes)
- Repository management, file organization
- Monitoring, reporting, and compliance checks
- Adding non-critical tests or workflows
- Standard onboarding and knowledge vault maintenance
- **ENHANCED:** Software downloads and installations for development tools
- **ENHANCED:** System configuration changes for project requirements
- **ENHANCED:** Environment setup and tool installations

---

## 🚫 ACTIONS REQUIRING ORCHESTRATOR APPROVAL

- Credential rotation, security/secret updates
- Production deployments or releases
- Major policy/process changes
- Introduction of new external integrations/services
- Destructive actions (deletions, force-pushes, etc.)

---

## 📊 LOGGING & TRANSPARENCY

- All auto-mode activity must be logged in `AUTO_MODE_ACTIVITY_LOG.md` (see template below).
- Blocked actions must be clearly flagged with [AUTO-MODE BLOCKED] for orchestrator review.
- Upon return, the Orchestrator will review the log and approve or address any flagged items.

---

## 🧾 ACTIVITY LOG TEMPLATE

```markdown
# AUTO-MODE ACTIVITY LOG

## [YYYY-MM-DD HH:MM] – [Action Type]
**Agent:** [Copilot or Amazon Q]
**Description:** [Brief summary of activity]
**Status:** [Completed/Blocked]
**Details/Notes:** [Any additional context]

---

## [EXAMPLE]
## 2025-09-07 18:10 – Documentation Update
**Agent:** Copilot  
**Description:** Added onboarding clarification to `knowledge-vault/ONBOARDING.md`  
**Status:** Completed  
**Details/Notes:** Improved checklist clarity based on new agent feedback.

## 2025-09-07 18:20 – Credential Rotation
**Agent:** Amazon Q  
**Description:** Attempted to rotate Gmail OAuth credentials  
**Status:** [AUTO-MODE BLOCKED]  
**Details/Notes:** Action requires orchestrator approval before proceeding.
```