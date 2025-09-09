
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

"""Test: Ensure documented actions & registry stay in sync.

Parses ADR 002 and registry to validate actions listed in code vs ADR narrative.
Lightweight guard to prevent drift (see ADR 002 Section 3 Risks & Mitigations).
"""

import os
import re
import importlib.util

ADR_002_PATH = os.path.join(
    "docs", "architecture", "adr", "002-modular-lambda-action-dispatch.md"
)
HANDLER_PATH = os.path.join("integrations", "lambda_woofy_handler.py")
MODULE_PATH = HANDLER_PATH  # single module holding ACTION_REGISTRY


def load_registry_actions():
    spec = importlib.util.spec_from_file_location("lambda_woofy_handler", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore
    registry = getattr(module, "ACTION_REGISTRY", None)
    assert isinstance(registry, dict) and registry, "ACTION_REGISTRY missing or empty"
    return set(registry.keys())


def parse_adr_actions():
    assert os.path.exists(ADR_002_PATH), "ADR 002 file missing"
    with open(ADR_002_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    # Simple heuristic: look for backticked action names in Context section listing (`hello`, `ping`)
    mentioned = set(re.findall(r"`([a-zA-Z0-9_-]+)`", text))
    # Filter out generic words not meant as actions if needed later
    return mentioned


def test_registry_and_adr_alignment():
    registry = load_registry_actions()
    adr_actions = parse_adr_actions()
    # Intersection check: all registry actions must appear somewhere in ADR (documented)
    missing_in_adr = registry - adr_actions
    assert not missing_in_adr, f"Actions not documented in ADR 002: {missing_in_adr}"
    # Optionally ensure we don't have stale documented actions; allow ADR to mention future ones gracefully
    # For now we only enforce registry -> ADR coverage.
