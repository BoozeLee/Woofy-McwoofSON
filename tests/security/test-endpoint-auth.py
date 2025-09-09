
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

# 🦴 Test: Endpoint Authentication

import pytest
import requests


@pytest.mark.skip(
    reason="External endpoint placeholder - skip in local/CI to avoid network dependency"
)
def test_requires_auth():
    r = requests.post(
        "https://api.woofy.example.com/api/v1/documents/fetch",
        json={"document_id": "doc-123"},
    )
    assert r.status_code == 401


@pytest.mark.skip(
    reason="External endpoint placeholder - skip in local/CI to avoid network dependency"
)
def test_valid_token():
    headers = {"Authorization": "Bearer test_valid_token"}
    r = requests.post(
        "https://api.woofy.example.com/api/v1/documents/fetch",
        headers=headers,
        json={"document_id": "doc-123"},
    )
    assert r.status_code in (200, 404)  # 404 if doc doesn't exist, 200 if it does
