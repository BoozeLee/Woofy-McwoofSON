"""Tests for the autonomous scheduler (ADR 003 / Cogno-style skip-logic)."""
import hashlib
import hmac
import json


from integrations.scheduler import Scheduler, SchedulerConfig
from main import handle_webhook, verify_signature

NOW = 1_700_000_000.0


def make_push(event_id="evt-1", ref="refs/heads/feature/x", repo="acme/app",
              head="abc123", sender_type="User", commits=None):
    return {
        "id": event_id,
        "type": "push",
        "ref": ref,
        "after": head,
        "repository": {"full_name": repo},
        "sender": {"type": sender_type},
        "commits": commits or [{"added": ["src/main.py"], "modified": [], "removed": []}],
    }


def make_pr(event_id="evt-2", draft=False, action="opened", repo="acme/app"):
    return {
        "id": event_id,
        "type": "pull_request",
        "action": action,
        "repository": {"full_name": repo},
        "pull_request": {"draft": draft, "base": {"ref": "develop"}, "head": {"sha": "def456"}},
        "sender": {"type": "User"},
    }


# --------------------------------------------------------------------------- #
# verify_signature
# --------------------------------------------------------------------------- #
def test_signature_valid():
    secret = "s3cret"
    payload = b'{"hello":"world"}'
    sig = "sha256=" + hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    assert verify_signature(secret, payload, sig) is True


def test_signature_invalid():
    assert verify_signature("s3cret", b'{"a":1}', "sha256=" + "0" * 64) is False


def test_signature_missing_or_malformed():
    assert verify_signature("s3cret", b'{"a":1}', None) is False
    assert verify_signature("s3cret", b'{"a":1}', "md5=abc") is False
    assert verify_signature("", b'{"a":1}', "sha256=abc") is False


# --------------------------------------------------------------------------- #
# handle_webhook
# --------------------------------------------------------------------------- #
def test_handle_webhook_bad_signature():
    status, payload = handle_webhook("s3cret", b'{"a":1}', None)
    assert status == 401
    assert payload["status"] == "error"


def test_handle_webhook_bad_json():
    payload = b'{"not json'
    sig = "sha256=" + hmac.new(b"s3cret", payload, hashlib.sha256).hexdigest()
    status, resp = handle_webhook("s3cret", payload, sig)
    assert status == 400
    assert resp["status"] == "error"


def test_handle_webhook_skip_decision():
    event = {"id": "x1", "type": "push", "ref": "refs/heads/main", "repository": {"full_name": "acme/app"}}
    payload = json.dumps(event).encode()
    sig = "sha256=" + hmac.new(b"s3cret", payload, hashlib.sha256).hexdigest()
    status, resp = handle_webhook("s3cret", payload, sig)
    assert status == 200
    assert resp["status"] == "skip"
    assert resp["skip_code"] == "ignored_branch"


def test_handle_webhook_run_decision():
    event = make_push()
    payload = json.dumps(event).encode()
    sig = "sha256=" + hmac.new(b"s3cret", payload, hashlib.sha256).hexdigest()
    status, resp = handle_webhook("s3cret", payload, sig)
    assert status == 200
    assert resp["status"] == "run"
    assert resp["work_order"]["repo"] == "acme/app"
    assert resp["work_order"]["head"] == "abc123"
    assert "review_changes" in resp["work_order"]["actions"]


# --------------------------------------------------------------------------- #
# Scheduler.decide
# --------------------------------------------------------------------------- #
def test_ignored_branch_skipped():
    s = Scheduler()
    d = s.decide(make_push(ref="refs/heads/main"), now=NOW)
    assert d.should_run is False
    assert d.skip_reason.code == "ignored_branch"


def test_unsupported_event_skipped():
    s = Scheduler()
    d = s.decide({"id": "e", "type": "fork", "repository": {"full_name": "a/b"}}, now=NOW)
    assert d.should_run is False
    assert d.skip_reason.code == "unsupported_event"


def test_draft_pr_skipped():
    s = Scheduler()
    d = s.decide(make_pr(draft=True), now=NOW)
    assert d.should_run is False
    assert d.skip_reason.code == "draft_pr"


def test_duplicate_event_skipped():
    s = Scheduler()
    assert s.decide(make_push(event_id="dup"), now=NOW).should_run is True
    d = s.decide(make_push(event_id="dup"), now=NOW + 60)
    assert d.should_run is False
    assert d.skip_reason.code == "duplicate"


def test_cooldown_blocks_rapid_runs():
    cfg = SchedulerConfig(cooldown_seconds=300)
    s = Scheduler(cfg)
    assert s.decide(make_push(event_id="a"), now=NOW).should_run is True
    d = s.decide(make_push(event_id="b"), now=NOW + 60)
    assert d.should_run is False
    assert d.skip_reason.code == "cooldown"
    # After the cooldown elapses the scheduler acts again.
    assert s.decide(make_push(event_id="c"), now=NOW + 301).should_run is True


def test_path_scope_respected():
    cfg = SchedulerConfig(watch_paths=["src/"])
    s = Scheduler(cfg)
    outside = make_push(commits=[{"added": ["docs/readme.md"], "modified": [], "removed": []}])
    d = s.decide(outside, now=NOW)
    assert d.should_run is False
    assert d.skip_reason.code == "path_out_of_scope"

    inside = make_push(commits=[{"added": ["src/main.py"], "modified": [], "removed": []}])
    assert s.decide(inside, now=NOW + 400).should_run is True


def test_min_priority_blocks_bot_noise():
    cfg = SchedulerConfig(min_priority=30)
    s = Scheduler(cfg)
    event = make_push(sender_type="Bot")
    d = s.decide(event, now=NOW)
    assert d.should_run is False
    assert d.skip_reason.code == "low_priority"


def test_human_event_priority_bumped():
    cfg = SchedulerConfig(min_priority=30)
    s = Scheduler(cfg)
    d = s.decide(make_push(sender_type="User"), now=NOW)
    assert d.should_run is True
    assert d.work_order.priority >= 30


def test_malformed_event_skipped():
    s = Scheduler()
    d = s.decide("not-a-dict", now=NOW)
    assert d.should_run is False
    assert d.skip_reason.code == "malformed"


def test_work_order_actions_for_pr():
    s = Scheduler()
    d = s.decide(make_pr(), now=NOW)
    assert d.should_run is True
    assert d.work_order.event_type == "pull_request"
    assert "review_pr" in d.work_order.actions
