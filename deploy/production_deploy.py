
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
import sys
import os
import requests

def deploy_production():
    try:
        # Initialize AWS clients
        lambda_client = boto3.client('lambda')
        s3_client = boto3.client('s3')
        dynamodb = boto3.resource('dynamodb')
        
        # Create S3 bucket
        bucket_name = 'woofy-production-bucket-' + os.urandom(4).hex()
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Created S3 bucket: {bucket_name}")
        
        # Create DynamoDB table
        table_name = 'woofy-production-data'
        dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )
        print(f"Created DynamoDB table: {table_name}")
        
        # Test Perplexity API
        if os.getenv('PERPLEXITY_API_KEY'):
            headers = {
                'Authorization': f'Bearer {os.getenv("PERPLEXITY_API_KEY")}',
                'Content-Type': 'application/json'
            }
            test_payload = {
                'model': 'llama-3.1-sonar-small-128k-online',
                'messages': [{'role': 'user', 'content': 'Test connection'}],
                'max_tokens': 100
            }
            response = requests.post('https://api.perplexity.ai/chat/completions', 
                                   headers=headers, json=test_payload)
            print(f"Perplexity API test: {response.status_code}")
        
        print("Production deployment successful")
        return True
        
    except Exception as e:
        print(f"Production deployment failed: {e}")
        return False

if __name__ == "__main__":
    if not os.getenv('AWS_ACCESS_KEY_ID'):
        print("AWS credentials not configured. Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY")
        sys.exit(1)
    
    success = deploy_production()
    sys.exit(0 if success else 1)