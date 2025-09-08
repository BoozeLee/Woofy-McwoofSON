#!/bin/bash
# Deploy AWS Hallucination Mitigation System

set -e

STACK_NAME="woofy-hallucination-mitigation"
REGION="us-east-1"

echo "🚀 Deploying WOOFY Hallucination Mitigation System..."

# Deploy CloudFormation stack
aws cloudformation deploy \
  --template-file aws-hallucination-mitigation-system.yml \
  --stack-name $STACK_NAME \
  --region $REGION \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides EnvironmentName=woofy-prod

# Get outputs
API_ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name $STACK_NAME \
  --region $REGION \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' \
  --output text)

TABLE_NAME=$(aws cloudformation describe-stacks \
  --stack-name $STACK_NAME \
  --region $REGION \
  --query 'Stacks[0].Outputs[?OutputKey==`TableName`].OutputValue' \
  --output text)

echo "✅ Deployment complete!"
echo "API Endpoint: $API_ENDPOINT"
echo "DynamoDB Table: $TABLE_NAME"

# Test the system
echo "🧪 Testing hallucination detection..."
curl -X POST $API_ENDPOINT \
  -H "Content-Type: application/json" \
  -d '{
    "text": "I am definitely not sure about this fact",
    "confidence": 0.3
  }'

echo "🎯 System ready for hallucination mitigation!"