# 🦴 Test: Endpoint Authentication

import pytest
import requests

@pytest.mark.skip(reason="External endpoint placeholder - skip in local/CI to avoid network dependency")
def test_requires_auth():
    r = requests.post("https://api.woofy.example.com/api/v1/documents/fetch", json={"document_id": "doc-123"})
    assert r.status_code == 401

@pytest.mark.skip(reason="External endpoint placeholder - skip in local/CI to avoid network dependency")
def test_valid_token():
    headers = {"Authorization": "Bearer test_valid_token"}
    r = requests.post("https://api.woofy.example.com/api/v1/documents/fetch", headers=headers, json={"document_id": "doc-123"})
    assert r.status_code in (200, 404)  # 404 if doc doesn't exist, 200 if it does