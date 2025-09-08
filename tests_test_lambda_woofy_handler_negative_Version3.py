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