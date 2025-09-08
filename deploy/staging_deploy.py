import boto3
import json
import sys
from infrastructure.aws_core import WoofyAWSCore

def deploy_staging():
    aws_core = WoofyAWSCore()
    
    try:
        # Deploy Lambda function
        aws_core.deploy_lambda('woofy-staging', 'lambda_function.zip')
        
        # Setup S3 bucket
        aws_core.setup_s3_bucket('woofy-staging-bucket')
        
        # Create DynamoDB table
        aws_core.create_dynamodb_table('woofy-staging-data')
        
        print("Staging deployment successful")
        return True
        
    except Exception as e:
        print(f"Staging deployment failed: {e}")
        return False

if __name__ == "__main__":
    success = deploy_staging()
    sys.exit(0 if success else 1)