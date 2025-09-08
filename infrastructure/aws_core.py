import boto3
import json
from typing import Dict, Any

class WoofyAWSCore:
    def __init__(self):
        self.lambda_client = boto3.client('lambda')
        self.s3_client = boto3.client('s3')
        self.dynamodb = boto3.resource('dynamodb')
        self.cloudwatch = boto3.client('cloudwatch')
    
    def deploy_lambda(self, function_name: str, code_path: str) -> Dict[str, Any]:
        with open(code_path, 'rb') as f:
            return self.lambda_client.create_function(
                FunctionName=function_name,
                Runtime='python3.9',
                Role='arn:aws:iam::ACCOUNT:role/lambda-execution-role',
                Handler='lambda_function.lambda_handler',
                Code={'ZipFile': f.read()},
                Environment={'Variables': {'STAGE': 'production'}}
            )
    
    def setup_s3_bucket(self, bucket_name: str) -> None:
        self.s3_client.create_bucket(Bucket=bucket_name)
        self.s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={'Status': 'Enabled'}
        )
    
    def create_dynamodb_table(self, table_name: str) -> None:
        self.dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )