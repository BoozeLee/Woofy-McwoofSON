
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
from integrations.lambda_woofy_handler import lambda_handler


def test_lambda_handler_success(mocker):
    # Mocking the event and context
    event = {
        "httpMethod": "GET",
        "path": "/woof",
        "headers": {"X-API-Key": "test-api-key"},
    }
    context = {}

    # Mocking the response
    mock_response = {
        "statusCode": 200,
        "body": '{"message": "Woof! 🐾 The API is live."}',
    }
    mocker.patch(
        "integrations.lambda_woofy_handler.some_dependency", return_value=mock_response
    )

    # Call the lambda handler
    response = lambda_handler(event, context)

    # Assertions
    assert response["statusCode"] == 200
    assert response["body"] == '{"message": "Woof! 🐾 The API is live."}'


def test_lambda_handler_invalid_method(mocker):
    event = {"httpMethod": "POST", "path": "/woof", "headers": {}}
    context = {}

    response = lambda_handler(event, context)

    assert response["statusCode"] == 405
    assert response["body"] == '{"error": "Method Not Allowed"}'


def test_lambda_handler_missing_api_key(mocker):
    event = {"httpMethod": "GET", "path": "/woof", "headers": {}}
    context = {}

    response = lambda_handler(event, context)

    assert response["statusCode"] == 401
    assert response["body"] == '{"error": "Unauthorized"}'
