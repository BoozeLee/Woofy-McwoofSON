
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

import pytest

from lambda_woofy_handler import lambda_handler


def test_invalid_event_shape():
    # Event missing required keys
    event = {}
    context = None
    with pytest.raises(KeyError):
        lambda_handler(event, context)


def test_event_with_wrong_type():
    # Event with wrong type for a field
    event = {"action": 123}
    context = None
    with pytest.raises(TypeError):
        lambda_handler(event, context)


def test_event_with_unexpected_action():
    # Event with an unsupported action string
    event = {"action": "unknown_action"}
    context = None
    response = lambda_handler(event, context)
    assert response.get("status") == "error"
