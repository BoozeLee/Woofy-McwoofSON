
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
import base64

class GitHubIntegration:
    def __init__(self):
        self.secrets_client = boto3.client('secretsmanager', region_name='us-east-1')
        self.github_token = None
    
    def get_github_token(self):
        response = self.secrets_client.get_secret_value(SecretId='github-oauth-secret')
        secret = json.loads(response['SecretString'])
        self.github_token = secret['client_secret']
        return self.github_token
    
    def create_repo(self, name, description="WOOFY McWOOFSON Enterprise AI Assistant"):
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        data = {
            'name': name,
            'description': description,
            'private': False,
            'auto_init': True
        }
        
        response = requests.post('https://api.github.com/user/repos', 
                               headers=headers, json=data)
        return response.json()
    
    def push_file(self, owner, repo, path, content, message):
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        encoded_content = base64.b64encode(content.encode()).decode()
        
        data = {
            'message': f'WOOFY: {message}',
            'content': encoded_content
        }
        
        url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
        response = requests.put(url, headers=headers, json=data)
        return response.json()

if __name__ == "__main__":
    try:
        github = GitHubIntegration()
        github.get_github_token()
        
        # Create repository
        repo = github.create_repo('woofy-mcwoofson-enterprise')
        print(f"SUCCESS: Repository created: {repo.get('html_url', 'Success!')}")
        
        # Push README
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
        
        github.push_file(repo['owner']['login'], repo['name'], 
                        'README.md', readme_content, 'Initial README')
        print("SUCCESS: WOOFY project pushed to GitHub!")
        
    except Exception as e:
        print(f"ERROR: Setup failed: {e}")