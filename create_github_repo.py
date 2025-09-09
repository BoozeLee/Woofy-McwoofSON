
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

def create_github_repo():
    # Get GitHub token
    secrets_client = boto3.client('secretsmanager', region_name='us-east-1')
    response = secrets_client.get_secret_value(SecretId='github-oauth-secret')
    secret = json.loads(response['SecretString'])
    github_token = secret['client_secret']
    
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Create repository
    data = {
        'name': 'woofy-mcwoofson-enterprise',
        'description': 'WOOFY McWOOFSON: Enterprise AI Assistant - Unleashing Revenue Through Atomic Innovation',
        'private': False,
        'auto_init': True
    }
    
    response = requests.post('https://api.github.com/user/repos', headers=headers, json=data)
    
    if response.status_code == 201:
        repo = response.json()
        print(f"SUCCESS: Repository created!")
        print(f"URL: {repo['html_url']}")
        print(f"Clone URL: {repo['clone_url']}")
        return repo
    elif response.status_code == 422:
        print("Repository already exists! Checking existing repo...")
        # Get existing repo
        response = requests.get('https://api.github.com/user/repos', headers=headers)
        repos = response.json()
        for repo in repos:
            if repo['name'] == 'woofy-mcwoofson-enterprise':
                print(f"Found existing repo: {repo['html_url']}")
                return repo
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    create_github_repo()