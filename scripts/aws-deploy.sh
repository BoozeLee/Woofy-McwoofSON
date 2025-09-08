#!/bin/bash
# AWS Infrastructure Deployment Script for WOOFY McWOOFSON

set -e

echo "🚀 Deploying WOOFY McWOOFSON AWS Infrastructure"

# Check AWS CLI
if ! command -v aws &> /dev/null; then
    echo "❌ AWS CLI not found. Please install AWS CLI first."
    exit 1
fi

# Check credentials
if ! aws sts get-caller-identity &> /dev/null; then
    echo "❌ AWS credentials not configured. Please run 'aws configure' first."
    exit 1
fi

# Deploy CloudFormation stack
echo "📦 Deploying CloudFormation stack..."
aws cloudformation deploy \
    --template-file infrastructure/woofy-infrastructure.yaml \
    --stack-name woofy-mcwoofson-stack \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameter-overrides \
        Environment=production \
        ProjectName=woofy-mcwoofson

# Get stack outputs
echo "📊 Getting stack outputs..."
API_URL=$(aws cloudformation describe-stacks \
    --stack-name woofy-mcwoofson-stack \
    --query 'Stacks[0].Outputs[?OutputKey==`APIGatewayURL`].OutputValue' \
    --output text)

LAMBDA_ARN=$(aws cloudformation describe-stacks \
    --stack-name woofy-mcwoofson-stack \
    --query 'Stacks[0].Outputs[?OutputKey==`LambdaFunctionArn`].OutputValue' \
    --output text)

# Test API endpoint
echo "🧪 Testing API endpoint..."
if curl -s "$API_URL" | grep -q "WOOFY"; then
    echo "✅ API endpoint is working!"
else
    echo "⚠️ API endpoint test failed"
fi

# Setup monitoring
echo "📊 Setting up monitoring..."
aws logs create-log-group --log-group-name /aws/lambda/woofy-mcwoofson-handler || true

# Create cost alert
echo "💰 Setting up cost alerts..."
aws budgets create-budget \
    --account-id $(aws sts get-caller-identity --query Account --output text) \
    --budget '{
        "BudgetName": "WoofyMcWoofsonBudget",
        "BudgetLimit": {
            "Amount": "50.00",
            "Unit": "USD"
        },
        "TimeUnit": "MONTHLY",
        "BudgetType": "COST"
    }' || echo "Budget may already exist"

echo "✅ AWS Infrastructure deployed successfully!"
echo "🌐 API URL: $API_URL"
echo "⚡ Lambda ARN: $LAMBDA_ARN"
echo "📊 Monitor at: https://console.aws.amazon.com/cloudformation/home"