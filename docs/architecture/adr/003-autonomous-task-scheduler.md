# 003: Autonomous Task Scheduler (Cogno-style skip-logic) 🐾

**Status:** Accepted  
**Date:** 2026-08-15  
**Authors:** Kiliaan Vanvoorden

## 1. Context
Woofy-McwoofSON received events on a schedule or on any webhook trigger, and would act on all of them. In practice this produces "junk tasks" and constant nagging: draft PRs, bot-generated noise, main-branch pushes, duplicate deliveries, and out-of-scope path changes all fire the agent even though none of them need work.

Inspired by the design notes in Cogno's pitch (a layer above the coding agent that decides its own timing and, crucially, which tasks *not* to do), Woofy needs a decision layer between the event stream and the agent. It must be deterministic, auditable, and testable.

## 2. Decision
Introduce `integrations/scheduler.py`, an event-driven decision engine:

1. `Scheduler.decide(event)` returns a `Decision` — either a run decision with a `WorkOrder` (task handed to the agent) or a skip decision with a structured `SkipReason`.
2. Skip-logic is applied in order: malformed events → unsupported event types → dedupe (already-processed) → ignored branches → draft PRs → path scope → priority threshold → cooldown.
3. Timing is self-determined via per-repository cooldown (no fixed cron; the scheduler acts only when an event is worth acting on).
4. Priority scoring is additive and configurable (`SchedulerConfig`): humans bump priority, bots do not, drafts are penalized.
5. `decide()` has no side effects — dispatching is the caller's job. This keeps scheduling auditable and unit-testable (injectable clock via the `now` parameter).
6. `main.py` exposes a verified webhook endpoint (`X-Hub-Signature-256` via `WEBHOOK_SECRET`) that feeds events into the scheduler before dispatching.

## 3. Consequences
### Positive
- Fewer junk tasks: draft PRs, bot noise, duplicates, and out-of-scope changes never reach the agent.
- Self-timing: cooldown prevents nagging the same repository repeatedly.
- Testable: 15+ unit tests cover every skip path (`tests/test_scheduler.py`).
- Secure: webhook signature verification is constant-time (`hmac.compare_digest`).

### Negative / Trade-offs
- Conservative defaults (ignored `main`/`master`, 5-minute cooldown) must be tuned per deployment.
- Rule order matters; adding rules requires care not to weaken earlier guards.

### Risks & Mitigations
- Rule drift → every skip reason has a machine-readable code used in tests.
- Misconfigured thresholds → all thresholds live in `SchedulerConfig` with documented defaults.

## 4. Implementation Notes
- New: `integrations/scheduler.py`, `main.py`, `tests/test_scheduler.py`, ADR 003.
- `main.py` binds `127.0.0.1` by default; bind `0.0.0.0` only behind a trusted ingress.
- Future: pluggable rule providers and persistent dedupe state (Redis) for multi-instance deployments.

## 5. Alternatives Considered
- Cron-based triggering: rejected — fires regardless of value, generates junk tasks.
- Act on every event: rejected — the exact problem this ADR solves.
- External scheduler service: rejected — Woofy stays self-contained; the module is framework-agnostic.

## 6. References
- Cogno pitch (Genaxis, 2026-08) — "decides which tasks not to do".
- ADR 002 Modular Lambda Action Dispatch (agent entry point).
- Tests: `tests/test_scheduler.py`, `tests/test_api.py`.

---
🐕 Revisit when multi-instance deployment requires shared dedupe/cooldown state.
