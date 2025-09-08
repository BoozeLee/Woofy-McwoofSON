import pytest
from integrations.lambda_woofy_handler import lambda_handler

def test_lambda_handler_success(mocker):
    # Mocking the event and context
    event = {
        "httpMethod": "GET",
        "path": "/woof",
        "headers": {
            "X-API-Key": "test-api-key"
        }
    }
    context = {}

    # Mocking the response
    mock_response = {
        "statusCode": 200,
        "body": '{"message": "Woof! 🐾 The API is live."}'
    }
    mocker.patch('integrations.lambda_woofy_handler.some_dependency', return_value=mock_response)

    # Call the lambda handler
    response = lambda_handler(event, context)

    # Assertions
    assert response['statusCode'] == 200
    assert response['body'] == '{"message": "Woof! 🐾 The API is live."}'

def test_lambda_handler_invalid_method(mocker):
    event = {
        "httpMethod": "POST",
        "path": "/woof",
        "headers": {}
    }
    context = {}

    response = lambda_handler(event, context)

    assert response['statusCode'] == 405
    assert response['body'] == '{"error": "Method Not Allowed"}'

def test_lambda_handler_missing_api_key(mocker):
    event = {
        "httpMethod": "GET",
        "path": "/woof",
        "headers": {}
    }
    context = {}

    response = lambda_handler(event, context)

    assert response['statusCode'] == 401
    assert response['body'] == '{"error": "Unauthorized"}'