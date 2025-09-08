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