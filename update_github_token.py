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