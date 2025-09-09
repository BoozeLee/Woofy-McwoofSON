
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

def update_github_token():
    # Get your GitHub token
    github_token = input("Enter your GitHub Personal Access Token: ")
    
    # Update AWS secret
    secrets_client = boto3.client('secretsmanager', region_name='us-east-1')
    
    secret_value = {
        "client_secret": github_token
    }
    
    response = secrets_client.update_secret(
        SecretId='github-oauth-secret',
        SecretString=json.dumps(secret_value)
    )
    
    print("SUCCESS: GitHub token updated in AWS Secrets Manager!")
    print(f"Secret ARN: {response['ARN']}")

if __name__ == "__main__":
    update_github_token()