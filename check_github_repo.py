
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

def check_github_repos():
    # Get GitHub token from AWS
    secrets_client = boto3.client('secretsmanager', region_name='us-east-1')
    response = secrets_client.get_secret_value(SecretId='github-oauth-secret')
    secret = json.loads(response['SecretString'])
    github_token = secret['client_secret']
    
    # List your repositories
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    response = requests.get('https://api.github.com/user/repos', headers=headers)
    repos = response.json()
    
    print("Your GitHub repositories:")
    for repo in repos:
        if 'woofy' in repo['name'].lower():
            print(f"SUCCESS: Found WOOFY repo: {repo['html_url']}")
            print(f"  - Name: {repo['name']}")
            print(f"  - Description: {repo.get('description', 'No description')}")
            print(f"  - Private: {repo['private']}")
            return repo['html_url']
    
    print("No WOOFY repository found yet.")
    return None

if __name__ == "__main__":
    repo_url = check_github_repos()
    if repo_url:
        print(f"\nYour WOOFY repository is ready at: {repo_url}")
    else:
        print("Repository creation may still be in progress.")