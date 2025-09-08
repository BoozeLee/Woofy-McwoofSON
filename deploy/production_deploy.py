import boto3
import json
import sys
from infrastructure.aws_core import WoofyAWSCore
from integrations.perplexity_ai import PerplexityAI

def deploy_production():
    aws_core = WoofyAWSCore()
    perplexity = PerplexityAI()
    
    try:
        # Deploy production Lambda
        aws_core.deploy_lambda('woofy-production', 'lambda_function.zip')
        
        # Setup production S3
        aws_core.setup_s3_bucket('woofy-production-bucket')
        
        # Create production DynamoDB
        aws_core.create_dynamodb_table('woofy-production-data')
        
        # Test Perplexity integration
        test_result = perplexity.search_and_analyze("AI market trends 2024")
        
        print("Production deployment successful")
        return True
        
    except Exception as e:
        print(f"Production deployment failed: {e}")
        return False

if __name__ == "__main__":
    success = deploy_production()
    sys.exit(0 if success else 1)