# 🔧 VS Code AWS Setup Instructions

**Date:** 2025-01-27  
**Purpose:** Configure AWS Toolkit in VS Code for WOOFY McWOOFSON  
**Status:** READY FOR CONFIGURATION  

## 🎯 PREREQUISITES

### AWS Account Setup
- **Active AWS subscription:** Confirmed for this month
- **AWS CLI installed:** Required for credential management
- **AWS credentials configured:** Access key and secret key

### VS Code Requirements
- **VS Code installed:** Latest version recommended
- **AWS Toolkit extension:** Will be installed in setup

## 🚀 INSTALLATION STEPS

### Step 1: Install AWS Toolkit Extension
```bash
# Install AWS Toolkit extension
code --install-extension amazonwebservices.aws-toolkit-vscode
```

### Step 2: Configure AWS Credentials
```bash
# Option 1: Using AWS CLI
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter your default region (e.g., us-east-1)
# Enter your default output format (json)

# Option 2: Using environment variables
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_DEFAULT_REGION=us-east-1
```

### Step 3: VS Code Settings Configuration
```json
{
  "aws.profile": "default",
  "aws.region": "us-east-1",
  "aws.samcli.location": "/usr/local/bin/sam",
  "aws.lambda.recentlyUploaded": [],
  "aws.telemetry": false,
  "aws.experiments.jsonResourceModification": true
}
```

### Step 4: Verify AWS Connection
1. **Open VS Code**
2. **Open Command Palette:** `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
3. **Run:** `AWS: Connect to AWS`
4. **Select your AWS profile**
5. **Verify connection** in AWS Explorer panel

## 🛠️ AWS TOOLKIT FEATURES

### Lambda Functions
- **Create new Lambda functions**
- **Deploy existing functions**
- **Invoke functions locally**
- **View CloudWatch logs**

### API Gateway
- **Create and manage APIs**
- **Test API endpoints**
- **Deploy API stages**
- **Monitor API metrics**

### CloudFormation
- **Deploy CloudFormation stacks**
- **View stack resources**
- **Monitor stack events**
- **Update stack parameters**

### S3 Buckets
- **Browse S3 buckets**
- **Upload and download files**
- **Manage bucket permissions**
- **View bucket metrics**

## 🔧 WOOFY-SPECIFIC CONFIGURATION

### Project Settings
Create `.vscode/settings.json` in project root:
```json
{
  "aws.profile": "woofy-mcwoofson",
  "aws.region": "us-east-1",
  "aws.samcli.location": "/usr/local/bin/sam",
  "aws.lambda.recentlyUploaded": [],
  "aws.telemetry": false,
  "files.associations": {
    "*.yaml": "cloudformation"
  },
  "yaml.schemas": {
    "https://raw.githubusercontent.com/awslabs/goformation/master/schema/cloudformation.schema.json": "infrastructure/*.yaml"
  }
}
```

### Launch Configuration
Create `.vscode/launch.json`:
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug WOOFY Lambda",
      "type": "aws-sam",
      "request": "direct-invoke",
      "invokeTarget": {
        "target": "template",
        "templatePath": "infrastructure/woofy-infrastructure.yaml",
        "logicalId": "WoofyLambdaHandler"
      },
      "lambda": {
        "payload": {
          "json": {
            "message": "Hello WOOFY!"
          }
        },
        "environmentVariables": {
          "ENVIRONMENT": "development"
        }
      }
    }
  ]
}
```

## 🧪 TESTING AWS INTEGRATION

### Test 1: Lambda Function Deployment
```bash
# Deploy Lambda function
aws lambda update-function-code \
  --function-name woofy-mcwoofson-handler \
  --zip-file fileb://lambda-deployment-package.zip
```

### Test 2: API Gateway Testing
```bash
# Test API endpoint
curl -X GET https://your-api-id.execute-api.us-east-1.amazonaws.com/production/woofy
```

### Test 3: CloudFormation Stack
```bash
# Validate CloudFormation template
aws cloudformation validate-template \
  --template-body file://infrastructure/woofy-infrastructure.yaml
```

## 📊 MONITORING SETUP

### CloudWatch Integration
- **View Lambda logs** in VS Code
- **Monitor API Gateway metrics**
- **Set up CloudWatch alarms**
- **Create custom dashboards**

### Cost Monitoring
- **AWS Cost Explorer integration**
- **Budget alerts configuration**
- **Resource usage tracking**
- **Cost optimization recommendations**

## 🔒 SECURITY CONFIGURATION

### IAM Best Practices
- **Use least privilege access**
- **Create specific IAM roles**
- **Enable MFA for AWS account**
- **Regular access key rotation**

### Secrets Management
- **Use AWS Secrets Manager**
- **Never commit credentials to code**
- **Use environment variables**
- **Encrypt sensitive data**

## 🚀 NEXT STEPS

### Immediate Actions
1. **Install AWS Toolkit extension**
2. **Configure AWS credentials**
3. **Test connection to AWS**
4. **Deploy WOOFY infrastructure**

### Validation Steps
1. **Verify Lambda function deployment**
2. **Test API Gateway endpoints**
3. **Check CloudWatch logs**
4. **Validate security settings**

---

**🔧 VS Code AWS setup ready - configure toolkit and deploy WOOFY infrastructure!**