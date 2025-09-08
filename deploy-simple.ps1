Write-Host "🚀 Deploying WOOFY Hallucination Mitigation System..." -ForegroundColor Green

# Test AWS credentials first
Write-Host "Testing AWS credentials..." -ForegroundColor Yellow
aws sts get-caller-identity

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ AWS credentials valid!" -ForegroundColor Green
    
    # Deploy the stack
    Write-Host "Deploying CloudFormation stack..." -ForegroundColor Yellow
    aws cloudformation deploy `
        --template-file aws-hallucination-mitigation-system.yml `
        --stack-name woofy-hallucination-mitigation `
        --region us-east-1 `
        --capabilities CAPABILITY_IAM `
        --parameter-overrides EnvironmentName=woofy-prod
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Deployment successful!" -ForegroundColor Green
        
        # Get outputs
        $ApiEndpoint = aws cloudformation describe-stacks --stack-name woofy-hallucination-mitigation --region us-east-1 --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' --output text
        $TableName = aws cloudformation describe-stacks --stack-name woofy-hallucination-mitigation --region us-east-1 --query 'Stacks[0].Outputs[?OutputKey==`TableName`].OutputValue' --output text
        
        Write-Host "API Endpoint: $ApiEndpoint" -ForegroundColor Cyan
        Write-Host "DynamoDB Table: $TableName" -ForegroundColor Cyan
    } else {
        Write-Host "❌ Deployment failed!" -ForegroundColor Red
    }
} else {
    Write-Host "❌ AWS credentials invalid. Run 'aws configure' first." -ForegroundColor Red
}