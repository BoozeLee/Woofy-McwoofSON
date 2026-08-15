"""Autonomous task scheduler for Woofy-McwoofSON.

A Cogno-style decision layer above the coding agent: it decides WHEN to
act and -- more importantly -- WHICH TASKS NOT TO DO.

Instead of firing on every event (cron, hooks, a rule somewhere), the
scheduler watches an event stream, applies skip-logic, and only hands a
work order to the agent when a task is actually worth doing.

Design notes (ADR 003):
  - Deterministic and pure where possible (injectable clock) -> unit tested.
  - Skip-logic is additive: add a rule, do not weaken existing ones.
  - No side effects inside :func:`Scheduler.decide` -- dispatching is the
    caller's job, so scheduling stays auditable and testable.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set


@dataclass(frozen=True)
class SkipReason:
    """Why the scheduler decided NOT to act on an event."""

    code: str
    message: str


@dataclass
class WorkOrder:
    """The task handed to the agent when the scheduler decides to act."""

    event_id: str
    event_type: str
    repo: str
    ref: str
    head: str
    priority: int  # 0..100, higher = more important
    actions: List[str]
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Decision:
    """Outcome of evaluating a single event."""

    should_run: bool
    work_order: Optional[WorkOrder]
    skip_reason: Optional[SkipReason]
    event_type: str


@dataclass
class SchedulerConfig:
    """Tunables for the scheduler. Values are deliberately conservative."""

    #: Ignore events whose id/head we have already seen (dedupe).
    dedupe: bool = True
    #: Minimum seconds between two runs for the same repository.
    cooldown_seconds: float = 300.0
    #: Only run when the change touches at least one of these paths.
    #: Empty list = watch everything.
    watch_paths: List[str] = field(default_factory=list)
    #: Never act on these branches (e.g. release branches handled by humans).
    ignored_branches: List[str] = field(default_factory=lambda: ["main", "master"])
    #: Treat draft PRs as not-ready -- do not hand them to the agent.
    skip_drafts: bool = True
    #: Minimum priority an event must reach before we act (0..100).
    min_priority: int = 30
    #: Priority added when the event was triggered by a human (vs. a bot).
    human_bump: int = 20
    #: Events we know how to act on. Anything else is skipped as "noise".
    supported_events: Set[str] = field(
        default_factory=lambda: {"push", "pull_request", "issue_comment", "pull_request_review"}
    )


class Scheduler:
    """Event-driven decision engine. Stateless per call apart from memory."""

    def __init__(self, config: Optional[SchedulerConfig] = None) -> None:
        self.config = config or SchedulerConfig()
        self._processed: Set[str] = set()
        self._last_run_at: Dict[str, float] = {}

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #
    def decide(self, event: Dict[str, Any], now: Optional[float] = None) -> Decision:
        """Evaluate one event and produce a run/skip decision.

        ``now`` is injectable for deterministic tests; defaults to wall clock.
        """
        ts = now if now is not None else time.time()

        # 0. Shape / noise guards -------------------------------------------------
        if not isinstance(event, dict):
            return self._skip("unknown", "malformed", "Event is not an object")

        event_type = self._event_type(event)

        event_id = self._event_id(event)
        repo = self._repo_name(event)
        head = self._head_sha(event)

        if event_type not in self.config.supported_events:
            return self._skip(
                event_type,
                "unsupported_event",
                f"Event type '{event_type}' is not supported for agent dispatch",
            )

        # 1. Dedupe: already handled this exact event/head.
        if self.config.dedupe and event_id in self._processed:
            return self._skip(event_type, "duplicate", "Event was already processed")

        # 2. Repo / branch guards.
        if not repo:
            return self._skip(event_type, "no_repo", "Event has no repository context")

        branch = self._branch(event)
        if branch and branch in self.config.ignored_branches:
            return self._skip(
                event_type,
                "ignored_branch",
                f"Branch '{branch}' is excluded from autonomous dispatch",
            )

        # 3. Draft pull requests are not ready for the agent.
        if self.config.skip_drafts and self._is_draft(event):
            return self._skip(event_type, "draft_pr", "Pull request is still a draft")

        # 4. Path scoping: only act if the change is on a watched path.
        if self.config.watch_paths and not self._touches_watched_path(event):
            return self._skip(
                event_type,
                "path_out_of_scope",
                "Change does not touch any watched path",
            )

        # 5. Priority gate.
        priority = self._priority(event)
        if priority < self.config.min_priority:
            return self._skip(
                event_type,
                "low_priority",
                f"Priority {priority} below threshold {self.config.min_priority}",
            )

        # 6. Cooldown: don't nag the same repository within cooldown_seconds.
        if repo in self._last_run_at:
            elapsed = ts - self._last_run_at[repo]
            if elapsed < self.config.cooldown_seconds:
                return self._skip(
                    event_type,
                    "cooldown",
                    f"Cooldown active for '{repo}' ({elapsed:.0f}s/{self.config.cooldown_seconds:.0f}s)",
                )

        # 7. Run.
        self._processed.add(event_id)
        self._last_run_at[repo] = ts

        actions = self._plan_actions(event_type, event)
        order = WorkOrder(
            event_id=event_id,
            event_type=event_type,
            repo=repo,
            ref=self._ref(event),
            head=head or "",
            priority=priority,
            actions=actions,
            payload=event,
        )
        return Decision(should_run=True, work_order=order, skip_reason=None, event_type=event_type)

    # ------------------------------------------------------------------ #
    # Introspection helpers
    # ------------------------------------------------------------------ #
    def processed_count(self) -> int:
        return len(self._processed)

    # ------------------------------------------------------------------ #
    # Skip / scoring internals
    # ------------------------------------------------------------------ #
    def _skip(self, event_type: str, code: str, message: str) -> Decision:
        return Decision(
            should_run=False,
            work_order=None,
            skip_reason=SkipReason(code=code, message=message),
            event_type=event_type,
        )

    def _event_type(self, event: Dict[str, Any]) -> str:
        return str(event.get("type") or event.get("event") or "unknown")

    def _event_id(self, event: Dict[str, Any]) -> str:
        return str(event.get("id") or event.get("delivery") or self._head_sha(event) or "")

    def _repo_name(self, event: Dict[str, Any]) -> str:
        repo = event.get("repository") or {}
        return str(repo.get("full_name") or repo.get("name") or "")

    def _ref(self, event: Dict[str, Any]) -> str:
        return str(event.get("ref") or event.get("pull_request", {}).get("base", {}).get("ref") or "main")

    def _head_sha(self, event: Dict[str, Any]) -> str:
        head = event.get("after") or event.get("head")
        if not head:
            pr = event.get("pull_request") or {}
            head = pr.get("head", {}).get("sha")
        return str(head or "")

    def _branch(self, event: Dict[str, Any]) -> str:
        ref = self._ref(event)
        return ref.split("/")[-1] if ref.startswith("refs/") else ref

    def _is_draft(self, event: Dict[str, Any]) -> bool:
        pr = event.get("pull_request") or {}
        if isinstance(pr, dict) and pr.get("draft"):
            return True
        return bool(event.get("draft"))

    def _touches_watched_path(self, event: Dict[str, Any]) -> bool:
        commits = event.get("commits") or []
        for commit in commits:
            for kind in ("added", "modified", "removed"):
                for path in commit.get(kind) or []:
                    if any(path.startswith(prefix) for prefix in self.config.watch_paths):
                        return True
        return False

    def _priority(self, event: Dict[str, Any]) -> int:
        """Score how much this event is worth acting on (0..100)."""
        score = 10  # baseline
        if self._is_draft(event):
            score -= 20
        pr = event.get("pull_request") or {}
        if isinstance(pr, dict) and pr.get("draft"):
            score -= 20
        sender = event.get("sender") or {}
        if not isinstance(sender, dict) or str(sender.get("type", "")).lower() in ("bot", "automation"):
            pass  # bots do not add value on their own
        else:
            score += self.config.human_bump
        if event.get("action") == "opened":
            score += 10
        if event.get("action") == "labeled":
            score += 5
        return max(0, min(100, score))

    def _plan_actions(self, event_type: str, event: Dict[str, Any]) -> List[str]:
        """Translate an event into a concrete, bounded task for the agent."""
        if event_type == "push":
            return ["review_changes", "check_build", "update_changelog"]
        if event_type == "pull_request":
            return ["review_pr", "check_ci", "comment_summary"]
        if event_type == "pull_request_review":
            return ["respond_to_review"]
        if event_type == "issue_comment":
            return ["triage_comment"]
        return ["assess"]
