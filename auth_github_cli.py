
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
import json
import subprocess
import tempfile
import os

def auth_github_cli():
    # Get token from AWS
    secrets_client = boto3.client('secretsmanager', region_name='us-east-1')
    response = secrets_client.get_secret_value(SecretId='github-oauth-secret')
    secret = json.loads(response['SecretString'])
    github_token = secret['client_secret']
    
    # Create temporary file with token
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write(github_token)
        token_file = f.name
    
    try:
        # Authenticate GitHub CLI
        result = subprocess.run(
            ['gh', 'auth', 'login', '--with-token'],
            input=github_token,
            text=True,
            capture_output=True
        )
        
        if result.returncode == 0:
            print("SUCCESS: GitHub CLI authenticated!")
            
            # Test authentication
            status_result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True)
            print("GitHub CLI Status:")
            print(status_result.stdout)
            
        else:
            print(f"ERROR: GitHub CLI authentication failed")
            print(f"Error: {result.stderr}")
            
    finally:
        # Clean up temp file
        os.unlink(token_file)

if __name__ == "__main__":
    auth_github_cli()