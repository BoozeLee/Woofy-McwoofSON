
# WOOFY SECURITY GUARDRAILS - AUTO-APPLIED
import os
import sys
import logging

# Disable AWS credential logging
for logger_name in ['boto3', 'botocore', 'urllib3', 's3transfer']:
    logging.getLogger(logger_name).setLevel(logging.CRITICAL)

# Suppress credential discovery
os.environ['AWS_DEFAULT_OUTPUT'] = 'json'
os.environ['AWS_CLI_FILE_ENCODING'] = 'UTF-8'

# Import security guardrails
try:
    from security_guardrails import SecurityGuardrails
    SecurityGuardrails.secure_log("Security guardrails active")
except ImportError:
    pass

import json
from typing import Any, Dict, Callable

ActionFunc = Callable[[Dict[str, Any]], Dict[str, Any]]


def action_hello(event: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "status": "ok",
        "message": "Woofy McWoofson says: Hello, enterprise world! 🐾",
    }


def action_ping(event: Dict[str, Any]) -> Dict[str, Any]:
    return {"status": "ok", "pong": True}


ACTION_REGISTRY: Dict[str, ActionFunc] = {
    "hello": action_hello,
    "ping": action_ping,
}


def _build_response(status: int, payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "statusCode": status,
    "body": json.dumps(payload, ensure_ascii=False),
        "headers": {"Content-Type": "application/json"},
    }


def some_dependency(*args, **kwargs):  # pragma: no cover - placeholder for tests to patch
    return {"statusCode": 200, "body": json.dumps({"message": "noop"})}


def lambda_handler(event, context):
    """Unified Lambda handler supporting API Gateway and action-dispatch."""
    try:
        if not isinstance(event, dict):
            return _build_response(
                400,
                {
                    "status": "error",
                    "error": "Invalid event type",
                    "expected": "object",
                },
            )

        # API Gateway HTTP path
        if "httpMethod" in event and "path" in event:
            method = (event.get("httpMethod") or "").upper()
            path = event.get("path") or ""
            headers = {k.lower(): v for k, v in (event.get("headers") or {}).items()}

            if path == "/woof":
                if method != "GET":
                    return _build_response(405, {"error": "Method Not Allowed"})
                api_key = headers.get("x-api-key")
                if not api_key:
                    return _build_response(401, {"error": "Unauthorized"})
                _ = some_dependency()
                return {
                    "statusCode": 200,
                    "body": '{"message": "Woof! 🐾 The API is live."}',
                    "headers": {"Content-Type": "application/json"},
                }

        # Action-dispatch path
        action_raw = event.get("action", "hello")
        if not isinstance(action_raw, str):
            return _build_response(400, {"status": "error", "error": "Action must be a string"})
        action = action_raw.lower()
        func = ACTION_REGISTRY.get(action)
        if not func:
            return _build_response(400, {"status": "error", "error": "Unknown action", "supported": sorted(ACTION_REGISTRY.keys())})
        payload = func(event)
        return _build_response(200, payload)
    except Exception as e:
        return _build_response(500, {"status": "error", "error": "Unhandled exception", "detail": str(e)[:200]})
