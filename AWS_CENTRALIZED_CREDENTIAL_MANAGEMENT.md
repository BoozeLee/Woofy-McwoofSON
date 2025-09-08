# 🔐 AWS Centralized Credential Management for All APIs

**Date:** 2025-01-27  
**Purpose:** Secure, centralized credential management using AWS services  
**Status:** IMPLEMENTATION GUIDE READY  

## 🎯 OVERVIEW

Use AWS Secrets Manager and IAM to securely manage ALL API credentials (Perplexity, watsonx, Gemini, GROQ, etc.) with automatic rotation, encryption, and access control.

## 🛠️ AWS SERVICES FOR CREDENTIAL MANAGEMENT

### 1. AWS Secrets Manager
**Purpose:** Store and automatically rotate API keys  
**Benefits:**
- Automatic encryption at rest and in transit
- Programmatic access with IAM controls
- Automatic rotation capabilities
- Audit logging via CloudTrail

### 2. AWS IAM Roles
**Purpose:** Control access to secrets without hardcoded credentials  
**Benefits:**
- No long-term access keys needed
- Temporary credentials via STS
- Fine-grained permissions
- Cross-service authentication

### 3. AWS Parameter Store (Alternative)
**Purpose:** Hierarchical parameter storage  
**Benefits:**
- Cost-effective for simple secrets
- Integration with CloudFormation
- Versioning and change tracking

## 🚀 IMPLEMENTATION ARCHITECTURE

### Centralized Secret Storage
```yaml
# AWS Secrets Manager Structure
/woofy-mcwoofson/api-keys/
├── perplexity-api-key
├── watsonx-credentials
├── gemini-api-key
├── groq-api-key
├── github-token
├── discord-bot-token
└── stripe-keys
```

### Access Pattern
```python
# Application accesses secrets via AWS SDK
import boto3

def get_api_key(secret_name):
    """Retrieve API key from AWS Secrets Manager"""
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']
```

## 📋 STEP-BY-STEP IMPLEMENTATION

### Step 1: Create AWS Secrets
```bash
# Create secrets in AWS Secrets Manager
aws secretsmanager create-secret \
    --name "woofy-mcwoofson/perplexity-api-key" \
    --description "Perplexity AI API Key" \
    --secret-string "your-perplexity-api-key"

aws secretsmanager create-secret \
    --name "woofy-mcwoofson/watsonx-credentials" \
    --description "IBM watsonx API Credentials" \
    --secret-string '{"api_key":"your-key","project_id":"your-project"}'

aws secretsmanager create-secret \
    --name "woofy-mcwoofson/gemini-api-key" \
    --description "Google Gemini API Key" \
    --secret-string "your-gemini-api-key"

aws secretsmanager create-secret \
    --name "woofy-mcwoofson/groq-api-key" \
    --description "GROQ API Key" \
    --secret-string "your-groq-api-key"
```

### Step 2: Create IAM Role for Application
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": [
        "arn:aws:secretsmanager:*:*:secret:woofy-mcwoofson/*"
      ]
    }
  ]
}
```

### Step 3: Create Secure API Client
```python
# secure_api_client.py
import boto3
import json
from botocore.exceptions import ClientError
import logging

class SecureAPIManager:
    """Centralized API credential management using AWS Secrets Manager"""
    
    def __init__(self, region_name='us-east-1'):
        self.secrets_client = boto3.client('secretsmanager', region_name=region_name)
        self.logger = logging.getLogger(__name__)
    
    def get_secret(self, secret_name):
        """Retrieve secret from AWS Secrets Manager"""
        try:
            response = self.secrets_client.get_secret_value(SecretId=secret_name)
            return response['SecretString']
        except ClientError as e:
            self.logger.error(f"Failed to retrieve secret {secret_name}: {e}")
            raise
    
    def get_json_secret(self, secret_name):
        """Retrieve and parse JSON secret"""
        secret_string = self.get_secret(secret_name)
        return json.loads(secret_string)
    
    def get_perplexity_key(self):
        """Get Perplexity API key"""
        return self.get_secret("woofy-mcwoofson/perplexity-api-key")
    
    def get_watsonx_credentials(self):
        """Get watsonx credentials"""
        return self.get_json_secret("woofy-mcwoofson/watsonx-credentials")
    
    def get_gemini_key(self):
        """Get Gemini API key"""
        return self.get_secret("woofy-mcwoofson/gemini-api-key")
    
    def get_groq_key(self):
        """Get GROQ API key"""
        return self.get_secret("woofy-mcwoofson/groq-api-key")

# Usage example
api_manager = SecureAPIManager()
perplexity_key = api_manager.get_perplexity_key()
watsonx_creds = api_manager.get_watsonx_credentials()
```

### Step 4: Update Integration Clients
```python
# Updated Perplexity client using AWS Secrets Manager
from secure_api_client import SecureAPIManager

class SecurePerplexityClient:
    def __init__(self):
        self.api_manager = SecureAPIManager()
        self.api_key = self.api_manager.get_perplexity_key()
        # Rest of client initialization
    
    def query(self, prompt):
        # Use self.api_key for API calls
        pass

# Updated watsonx client
class SecureWatsonxClient:
    def __init__(self):
        self.api_manager = SecureAPIManager()
        self.credentials = self.api_manager.get_watsonx_credentials()
        self.api_key = self.credentials['api_key']
        self.project_id = self.credentials['project_id']
        # Rest of client initialization
```

## 🔄 AUTOMATIC ROTATION SETUP

### Lambda Function for Rotation
```python
# rotation_lambda.py
import boto3
import json

def lambda_handler(event, context):
    """Lambda function to rotate API keys"""
    
    secrets_client = boto3.client('secretsmanager')
    
    # Get current secret
    secret_name = event['SecretId']
    current_secret = secrets_client.get_secret_value(SecretId=secret_name)
    
    # Generate new API key (service-specific logic)
    new_key = generate_new_api_key(secret_name)
    
    # Update secret
    secrets_client.update_secret(
        SecretId=secret_name,
        SecretString=new_key
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Secret rotated successfully')
    }

def generate_new_api_key(secret_name):
    """Generate new API key based on service"""
    # Service-specific key generation logic
    pass
```

### CloudFormation Template for Rotation
```yaml
# rotation-setup.yaml
Resources:
  RotationLambda:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: woofy-secret-rotation
      Runtime: python3.11
      Handler: rotation_lambda.lambda_handler
      Code:
        ZipFile: |
          # Lambda function code here
      Role: !GetAtt RotationRole.Arn
  
  RotationRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
      Policies:
        - PolicyName: SecretsManagerAccess
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - secretsmanager:*
                Resource: '*'
```

## 🛡️ SECURITY BENEFITS

### Centralized Security
- **Single point of control** for all API credentials
- **Consistent security policies** across all services
- **Centralized audit logging** via CloudTrail
- **Automated compliance** with security standards

### Enhanced Protection
- **Encryption at rest** using AWS KMS
- **Encryption in transit** via HTTPS/TLS
- **Access control** via IAM policies
- **Temporary credentials** via STS assume role

### Operational Benefits
- **No hardcoded secrets** in application code
- **Automatic rotation** capabilities
- **Version control** of secret changes
- **Cross-region replication** for disaster recovery

## 💰 COST CONSIDERATIONS

### AWS Secrets Manager Pricing
- **$0.40 per secret per month**
- **$0.05 per 10,000 API calls**
- **Example:** 10 secrets = $4/month + API call costs

### Cost Optimization
- Use **AWS Parameter Store** for non-sensitive configuration
- **Batch API calls** to reduce request costs
- **Cache secrets** in application memory (with TTL)
- **Monitor usage** via CloudWatch metrics

## 📊 IMPLEMENTATION CHECKLIST

### Setup Phase
- [ ] **Create AWS Secrets Manager secrets** for all API keys
- [ ] **Configure IAM roles** with least privilege access
- [ ] **Deploy Lambda functions** for automatic rotation
- [ ] **Update application code** to use AWS SDK

### Testing Phase
- [ ] **Test secret retrieval** from all environments
- [ ] **Validate IAM permissions** and access controls
- [ ] **Test rotation functionality** (if implemented)
- [ ] **Monitor CloudTrail logs** for access patterns

### Production Phase
- [ ] **Deploy to production** environment
- [ ] **Configure monitoring** and alerting
- [ ] **Document procedures** for team members
- [ ] **Schedule regular reviews** of access and usage

## 🚨 SECURITY BEST PRACTICES

### Access Control
- **Use IAM roles** instead of access keys when possible
- **Implement least privilege** access policies
- **Enable MFA** for sensitive operations
- **Regular access reviews** and cleanup

### Monitoring
- **Enable CloudTrail** for all secret access
- **Set up CloudWatch alarms** for unusual activity
- **Monitor failed access attempts**
- **Regular security audits**

### Rotation
- **Implement automatic rotation** where possible
- **Test rotation procedures** regularly
- **Have rollback procedures** ready
- **Document rotation schedules**

---

**🔐 AWS CENTRALIZED CREDENTIAL MANAGEMENT - Secure, scalable, and compliant solution for all API credentials!**