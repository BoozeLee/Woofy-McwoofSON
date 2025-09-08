# AWS Credentials Setup for WOOFY Hallucination Mitigation
Write-Host "🔐 Setting up AWS credentials for WOOFY..." -ForegroundColor Green

# Prompt for credentials
$AccessKey = Read-Host "Enter your AWS Access Key ID"
$SecretKey = Read-Host "Enter your AWS Secret Access Key" -AsSecureString
$Region = Read-Host "Enter your AWS Region (default: us-east-1)"

if ([string]::IsNullOrEmpty($Region)) {
    $Region = "us-east-1"
}

# Convert secure string back to plain text for AWS CLI
$SecretKeyPlain = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($SecretKey))

# Configure AWS CLI
Write-Host "Configuring AWS CLI..." -ForegroundColor Yellow
aws configure set aws_access_key_id $AccessKey
aws configure set aws_secret_access_key $SecretKeyPlain
aws configure set default.region $Region
aws configure set default.output json

# Test configuration
Write-Host "Testing AWS configuration..." -ForegroundColor Yellow
aws sts get-caller-identity

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ AWS credentials configured successfully!" -ForegroundColor Green
    Write-Host "🚀 Ready to deploy hallucination mitigation system!" -ForegroundColor Green
} else {
    Write-Host "❌ AWS configuration failed. Please check your credentials." -ForegroundColor Red
}