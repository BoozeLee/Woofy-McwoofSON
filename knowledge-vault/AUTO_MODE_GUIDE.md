# 🚦 Auto-Mode Operations Guide

**Purpose:** Complete guide for operating in Orchestrator Auto-Mode  
**Audience:** Amazon Q, Copilot, and future team members  

## 🎯 WHAT IS AUTO-MODE?

Auto-Mode allows agents to proceed with pre-approved actions when the orchestrator is unavailable, while blocking high-risk actions that require explicit approval.

## ✅ AUTO-APPROVED ACTIONS

**Proceed without orchestrator approval:**
- Documentation updates and improvements
- Code quality refactors (no breaking changes)
- Repository management, file organization
- Monitoring, reporting, and compliance checks
- Adding non-critical tests or workflows
- Standard onboarding and knowledge vault maintenance

## 🚫 CRITICAL APPROVAL REQUIRED

**MUST wait for orchestrator return:**
- Credential changes/rotations
- Production deployments/releases
- Major policy/process changes
- Permanent deletions/destructive actions

## 🔄 ACTIVATION/DEACTIVATION

### Activation Process:
1. Orchestrator updates `AUTO_MODE_STATUS.md` to ACTIVE
2. Agents proceed with auto-approved actions
3. All actions logged in `AUTO_MODE_ACTIVITY_LOG.md`

### Deactivation Process:
1. Orchestrator updates `AUTO_MODE_STATUS.md` to INACTIVE
2. Resume normal approval processes
3. Orchestrator reviews activity log

## 📊 LOGGING REQUIREMENTS

**All actions must be logged using this format:**
```markdown
## [YYYY-MM-DD HH:MM] – [Action Type]
**Agent:** [Amazon Q or Copilot]
**Description:** [Brief summary of activity]
**Status:** [Completed/Blocked]
**Details/Notes:** [Additional context]
```

## 🚨 ESCALATION PROCEDURES

### For Blocked Actions:
1. Log action with status [AUTO-MODE BLOCKED]
2. Continue with other approved work
3. Flag for orchestrator review upon return

### For Critical Issues:
1. Immediately update `ORCHESTRATOR_COMMUNICATION_LOG.md`
2. Mark as CRITICAL priority
3. Consider deactivating auto-mode if necessary

## 🔍 MONITORING AUTO-MODE

**Check these files regularly:**
- `AUTO_MODE_STATUS.md` - Current auto-mode state
- `AUTO_MODE_ACTIVITY_LOG.md` - Real-time activity tracking
- `ORCHESTRATOR_COMMUNICATION_LOG.md` - Critical escalations

---

**🐕 WOOFY's Auto-Mode Rule:** When in doubt, log it out! Maximum transparency for orchestrator review.**