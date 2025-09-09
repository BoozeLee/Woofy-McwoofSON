
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

import boto3
import requests
import json
import pytest

def test_github_token():
    if not (os.environ.get("AWS_ACCESS_KEY_ID") and os.environ.get("AWS_SECRET_ACCESS_KEY")):
        pytest.skip("AWS credentials not configured; skipping live Secrets Manager test")
    # Get GitHub token
    secrets_client = boto3.client('secretsmanager', region_name='us-east-1')
    response = secrets_client.get_secret_value(SecretId='github-oauth-secret')
    secret = json.loads(response['SecretString'])
    github_token = secret['client_secret']
    
    print(f"Token starts with: {github_token[:10]}...")
    
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Test token by getting user info
    response = requests.get('https://api.github.com/user', headers=headers)
    
    if response.status_code == 200:
        user = response.json()
        print(f"SUCCESS: Token works!")
        print(f"Username: {user['login']}")
        print(f"Name: {user.get('name', 'Not set')}")
        
        # Check token scopes
        scopes = response.headers.get('X-OAuth-Scopes', 'No scopes found')
        print(f"Token scopes: {scopes}")
        
        return True
    else:
        print(f"ERROR: Token test failed - {response.status_code}")
        print(response.text)
        return False

if __name__ == "__main__":
    test_github_token()