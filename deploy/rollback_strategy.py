import boto3
import json
from datetime import datetime

class RollbackStrategy:
    def __init__(self):
        self.lambda_client = boto3.client('lambda')
        self.s3_client = boto3.client('s3')
        
    def create_snapshot(self, environment: str) -> str:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        snapshot_id = f"{environment}_snapshot_{timestamp}"
        
        # Create Lambda version
        self.lambda_client.publish_version(
            FunctionName=f'woofy-{environment}',
            Description=f'Snapshot {snapshot_id}'
        )
        
        return snapshot_id
    
    def rollback_to_snapshot(self, environment: str, snapshot_id: str) -> bool:
        try:
            # Update Lambda alias to previous version
            self.lambda_client.update_alias(
                FunctionName=f'woofy-{environment}',
                Name='LIVE',
                FunctionVersion=snapshot_id.split('_')[-1]
            )
            
            print(f"Rollback to {snapshot_id} successful")
            return True
            
        except Exception as e:
            print(f"Rollback failed: {e}")
            return False
    
    def health_check(self, environment: str) -> bool:
        try:
            response = self.lambda_client.invoke(
                FunctionName=f'woofy-{environment}',
                Payload=json.dumps({'action': 'health_check'})
            )
            return response['StatusCode'] == 200
        except:
            return False