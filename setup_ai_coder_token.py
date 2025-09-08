import boto3
import json
import os

def setup_ai_coder_token():
    # Get token from AWS Secrets Manager
    secrets_client = boto3.client('secretsmanager', region_name='us-east-1')
    response = secrets_client.get_secret_value(SecretId='github-oauth-secret')
    secret = json.loads(response['SecretString'])
    github_token = secret['client_secret']
    
    print(f"Retrieved token: {github_token[:20]}...")
    
    # 1. Update .env file
    env_content = f"""# GitHub Token for AI Coder
GITHUB_TOKEN={github_token}
GITHUB_USERNAME=BoozeLee
GITHUB_REPO=woofy-mcwoofson-enterprise
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    print("SUCCESS: Updated .env file")
    
    # 2. Set environment variable for current session
    os.environ['GITHUB_TOKEN'] = github_token
    print("SUCCESS: Set environment variable")
    
    # 3. Create PowerShell command to set permanently
    ps_command = f'[Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "{github_token}", "User")'
    
    with open('set_github_token.ps1', 'w') as f:
        f.write(f"""# Set GitHub token permanently
{ps_command}
Write-Host "GitHub token set permanently for user"
""")
    print("SUCCESS: Created PowerShell script: set_github_token.ps1")
    
    # 4. Test the token
    import requests
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get('https://api.github.com/user', headers=headers)
    
    if response.status_code == 200:
        user = response.json()
        print(f"SUCCESS: Token verified - User: {user['login']}")
    else:
        print(f"ERROR: Token verification failed: {response.status_code}")
    
    return github_token

if __name__ == "__main__":
    setup_ai_coder_token()