#!/usr/bin/env python3
"""Woofy-McwoofSON webhook server.

Implements the documented project vision: a webhook endpoint protected by
verifying the payload signature using GitHub's WEBHOOK_SECRET, feeding
events into the autonomous scheduler (integrations/scheduler.py) which
decides WHEN to act -- and which tasks NOT to do -- before dispatching a
work order to the agent (integrations/lambda_woofy_handler.py).

Run:
    WEBHOOK_SECRET=<secret> python main.py
Endpoints:
    GET  /health         -> pong (agent health probe)
    GET  /woof           -> hello (agent greeting)
    POST /webhook        -> verified GitHub event, run/skip decision
"""
from __future__ import annotations

import hashlib
import hmac
import json
import logging
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Dict, Optional, Tuple

from integrations.lambda_woofy_handler import lambda_handler
from integrations.scheduler import Scheduler, SchedulerConfig

LOG = logging.getLogger("woofy")
SCHEDULER: Optional[Scheduler] = None


def load_scheduler() -> Scheduler:
    global SCHEDULER
    if SCHEDULER is None:
        SCHEDULER = Scheduler(SchedulerConfig())
    return SCHEDULER


def verify_signature(secret: str, payload: bytes, signature_header: Optional[str]) -> bool:
    """Constant-time verification of the GitHub X-Hub-Signature-256 header.

    Returns False if the header is missing, malformed, or does not match
    an HMAC-SHA256 of ``payload`` keyed with ``secret``.
    """
    if not secret or not signature_header:
        return False
    if not signature_header.startswith("sha256="):
        return False
    expected = hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()
    provided = signature_header[len("sha256="):]
    return hmac.compare_digest(expected, provided)


def handle_webhook(secret: str, body: bytes, signature_header: Optional[str]) -> Tuple[int, Dict[str, Any]]:
    """Verify a webhook delivery, run the scheduler, and produce a response.

    Returns (http_status, json_payload).
    """
    if not verify_signature(secret, body, signature_header):
        return 401, {"status": "error", "error": "Invalid or missing signature"}

    try:
        event = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return 400, {"status": "error", "error": "Invalid JSON payload"}

    event_type = event.get("type") or event.get("event") or "push"
    event["type"] = event_type

    decision = load_scheduler().decide(event)
    if not decision.should_run:
        reason = decision.skip_reason
        return 200, {
            "status": "skip",
            "event_type": decision.event_type,
            "skip_code": reason.code if reason else "unknown",
            "message": reason.message if reason else "Skipped",
        }

    order = decision.work_order
    agent_result = lambda_handler({"action": "ping"}, None)
    return 200, {
        "status": "run",
        "event_type": decision.event_type,
        "work_order": {
            "event_id": order.event_id,
            "repo": order.repo,
            "head": order.head,
            "priority": order.priority,
            "actions": order.actions,
        },
        "agent_probe": agent_result,
    }


class WoofyHandler(BaseHTTPRequestHandler):
    server_version = "WoofyMcWoofson/1.0"

    @property
    def secret(self) -> str:
        return os.environ.get("WEBHOOK_SECRET", "")

    def _send_json(self, status: int, payload: Dict[str, Any]) -> None:
        data = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802 (http.server API)
        if self.path.rstrip("/") == "/health":
            self._send_json(*self._agent_dispatch({"action": "ping"}))
        elif self.path.rstrip("/") == "/woof":
            self._send_json(*self._agent_dispatch({"action": "hello"}))
        else:
            self._send_json(404, {"status": "error", "error": "Not found", "endpoints": ["/health", "/woof", "/webhook"]})

    def do_POST(self) -> None:  # noqa: N802 (http.server API)
        if self.path.rstrip("/") != "/webhook":
            self._send_json(404, {"status": "error", "error": "Not found"})
            return
        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length) if length else b""
        signature = self.headers.get("X-Hub-Signature-256")
        status, payload = handle_webhook(self.secret, body, signature)
        self._send_json(status, payload)

    def _agent_dispatch(self, event: Dict[str, Any]) -> Tuple[int, Dict[str, Any]]:
        result = lambda_handler(event, None)
        return int(result.get("statusCode", 500)), json.loads(result.get("body", "{}"))

    def log_message(self, fmt: str, *args: Any) -> None:
        LOG.info("%s - %s", self.address_string(), fmt % args)


def main() -> None:
    logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))
    port = int(os.environ.get("PORT", "8080"))
    host = os.environ.get("HOST", "127.0.0.1")
    secret = os.environ.get("WEBHOOK_SECRET", "")

    if host == "0.0.0.0":  # nosec B104 -- guarded: only a warning; loopback is the default
        LOG.warning("Binding to all interfaces. Only do this behind a trusted ingress.")

    if not secret:
        LOG.warning("WEBHOOK_SECRET is not set - webhook signature verification is disabled. "
                    "Set it via environment (see .env.example).")

    httpd = ThreadingHTTPServer((host, port), WoofyHandler)
    LOG.info("🐾 Woofy-McwoofSON listening on %s:%s", host, port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        LOG.info("Shutting down.")
        httpd.shutdown()


if __name__ == "__main__":  # pragma: no cover
    main()
