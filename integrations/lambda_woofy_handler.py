import json
from typing import Any, Dict, Callable

"""Lambda handler module for Woofy McWoofson.

Refactored to modular action dispatch per ADR 002 (Modular Lambda Action Dispatch 🐾):
 - Registry driven mapping action->callable
 - Pure functions for each action (facilitates isolation tests)
 - Central validation & error wrapping (prevents scattered insecure patterns)
 - Backward compatible JSON envelope contract (statusCode/body/headers)

Security Notes:
 - No secrets logged or echoed.
 - Future enhancement: structured logging with redaction & correlation IDs.
"""

ActionFunc = Callable[[Dict[str, Any]], Dict[str, Any]]


def action_hello(event: Dict[str, Any]) -> Dict[str, Any]:  # 🐶 Friendly greeting
    return {
        "status": "ok",
        "message": "Woofy McWoofson says: Hello, enterprise world! 🐾",
    }


def action_ping(event: Dict[str, Any]) -> Dict[str, Any]:  # Health probe
    return {"status": "ok", "pong": True}


ACTION_REGISTRY: Dict[str, ActionFunc] = {
    "hello": action_hello,
    "ping": action_ping,
}


def _build_response(status: int, payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "statusCode": status,
        "body": json.dumps(payload),
        "headers": {"Content-Type": "application/json"},
    }


def lambda_handler(
    event, context
):  # pragma: no cover (context aspects not covered fully)
    """Primary Lambda entrypoint (dispatch).

    Contract:
      Input: event dict with optional 'action' (defaults to 'hello')
      Output: HTTP style dict {statusCode, body(json), headers}

    Error paths return json payload with status=error & explanatory fields.
    See ADR 002 for evolution rationale & extension guidelines.
    """
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

        action_raw = event.get("action", "hello")
        if not isinstance(action_raw, str):
            return _build_response(
                400,
                {
                    "status": "error",
                    "error": "Action must be a string",
                },
            )

        action = action_raw.lower()
        func = ACTION_REGISTRY.get(action)
        if not func:
            return _build_response(
                400,
                {
                    "status": "error",
                    "error": "Unknown action",
                    "supported": sorted(ACTION_REGISTRY.keys()),
                },
            )

        payload = func(event)
        return _build_response(200, payload)
    except Exception as e:  # Catch-all to ensure JSON response contract
        return _build_response(
            500,
            {
                "status": "error",
                "error": "Unhandled exception",
                "detail": str(e)[:200],
            },
        )
