# 002: Modular Lambda Action Dispatch 🐾

**Status:** Accepted  
**Date:** 2025-09-08  
**Authors:** Automation Layer

## 1. Context
The initial `lambda_woofy_handler.py` implemented inline conditional logic for each supported action (`hello`, `ping`). As actions grow (health checks, enrichment, audit export, supervised AI orchestration), inline branching becomes brittle, harder to test, and risks insecure patterns (e.g., forgotten validation). A unified, declarative dispatch model reduces complexity, centralizes validation, and enables safe extension.

## 2. Decision
Refactor the handler to:
1. Introduce a registry (`ACTION_REGISTRY`) mapping action names to pure functions.
2. Isolate each action in its own small function returning a serializable dict.
3. Centralize input validation & error handling in the main handler.
4. Preserve existing response envelope (statusCode/body/headers) for backward compatibility.
5. Add guard for non-string action and unknown action returning structured error with supported list.

## 3. Consequences
### Positive
- Extensible: Adding actions = O(1) new function + registry entry.
- Testable: Each action testable in isolation (unit scope) + integration via dispatcher.
- Secure: Single choke point for validation & error wrapping.
- Maintainable: Reduces conditional sprawl.

### Negative / Trade-offs
- Slight indirection vs simple if/else.
- Requires contributor discipline to register actions.

### Risks & Mitigations
- Drift between documented and actual actions → add automated test asserting registry names appear in docs/OpenAPI (future).
- Action name collisions → fail fast on duplicate keys at import time.

## 4. Implementation Notes
- Keep `_build_response` helper for envelope consistency.
- Future: move actions into `integrations/actions/` package when count > ~6.
- Logging (future) must redact sensitive event keys—NOT implemented yet (avoid premature complexity).

## 5. Alternatives Considered
- Continue inline branching: rejected (scalability & security hotspots).
- Class-based strategy objects: overkill for current scale.
- Dynamic import per action: premature optimization with cold start risk.

## 6. References
- ADR 001 Serverless Baseline
- CHANGELOG Unreleased entry (modular dispatch)
- Tests: `tests/test_api.py`, `tests/test_lambda_woofy_handler_negative.py`

---
🐕 This ADR will be revisited once action count > 8 or cross-cutting concerns (auth, rate limiting) require middleware abstraction.
