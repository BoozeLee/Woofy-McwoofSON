# 🚀 AWS Hallucination Mitigation System Setup

## Prerequisites

1. **Install AWS CLI**:
   ```powershell
   # Download from: https://aws.amazon.com/cli/
   # Or use chocolatey:
   choco install awscli
   ```

2. **Configure AWS Credentials**:
   ```powershell
   aws configure
   ```
   Enter:
   - AWS Access Key ID
   - AWS Secret Access Key  
   - Default region: `us-east-1`
   - Default output format: `json`

3. **Deploy the System**:
   ```powershell
   aws cloudformation deploy `
     --template-file aws-hallucination-mitigation-system.yml `
     --stack-name woofy-hallucination-mitigation `
     --region us-east-1 `
     --capabilities CAPABILITY_IAM `
     --parameter-overrides EnvironmentName=woofy-prod
   ```

## System Components

✅ **DynamoDB Table**: Tracks hallucination events  
✅ **Lambda Function**: Real-time detection algorithm  
✅ **SNS Topic**: Alert notifications  
✅ **API Gateway**: REST endpoint for integration  
✅ **IAM Roles**: Secure permissions  

## Usage

```python
from integrations.hallucination_detector import HallucinationDetector

detector = HallucinationDetector("https://your-api-endpoint/prod/detect")
result = detector.detect("Sample text", confidence=0.8)
print(f"Safe: {detector.is_safe('Sample text', 0.8)}")
```

## Next Steps

1. Configure AWS credentials
2. Run deployment command
3. Update API endpoint in code
4. Test the system