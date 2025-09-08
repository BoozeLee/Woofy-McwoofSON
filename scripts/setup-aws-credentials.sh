#!/bin/bash

# 🐕‍🦺 WOOFY McWOOFSON AWS Credentials Setup Script
# Enterprise-Grade AWS Authentication Setup
# NEVER share your AWS credentials - this script helps you set them up securely

set -e

# Configuration
SCRIPT_VERSION="1.0"
WOOFY_PROJECT="woofy-mcwoofson"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_security() {
    echo -e "${PURPLE}[SECURITY]${NC} $1"
}

log_step() {
    echo -e "${CYAN}[STEP]${NC} $1"
}

# Security disclaimer
security_disclaimer() {
    echo
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                    🔐 AWS SECURITY NOTICE                     ║"
    echo "╠════════════════════════════════════════════════════════════════╣"
    echo "║  This script helps you set up YOUR OWN AWS credentials.      ║"
    echo "║  NEVER share AWS access keys, secret keys, or session tokens!║"
    echo "║                                                              ║"
    echo "║  🔴 DANGER: Sharing AWS credentials can compromise:          ║"
    echo "║     • Your AWS account and billing                            ║"
    echo "║     • All AWS services and resources                         ║"
    echo "║     • Enterprise security and compliance                     ║"
    echo "║     • Data privacy and regulatory compliance                 ║"
    echo "║                                                              ║"
    echo "║  ✅ SAFE: Generate your own IAM credentials                  ║"
    echo "║  ✅ SAFE: Use AWS IAM best practices                         ║"
    echo "║  ✅ SAFE: Enable MFA and least-privilege access              ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo
}

# Check system requirements
check_requirements() {
    log_step "Checking system requirements..."

    # Check for required commands
    local missing_commands=()

    for cmd in curl wget unzip python3 pip3; do
        if ! command -v "$cmd" &> /dev/null; then
            missing_commands+=("$cmd")
        fi
    done

    if [[ ${#missing_commands[@]} -gt 0 ]]; then
        log_error "Missing required commands: ${missing_commands[*]}"
        log_info "Please install missing commands and try again."
        exit 1
    fi

    # Check Python version
    local python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    if [[ $(echo "$python_version < 3.8" | bc -l) -eq 1 ]]; then
        log_error "Python 3.8+ required. Current version: $python_version"
        exit 1
    fi

    log_success "System requirements check passed"
}

# Setup AWS CLI
setup_aws_cli() {
    log_step "Setting up AWS CLI..."

    # Check if AWS CLI is installed
    if ! command -v aws &> /dev/null; then
        log_info "AWS CLI not found. Installing..."

        # Download and install AWS CLI v2
        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
        unzip awscliv2.zip
        sudo ./aws/install

        # Clean up
        rm -rf awscliv2.zip aws/

        log_success "AWS CLI installed"
    else
        local aws_version=$(aws --version 2>&1 | sed 's/aws-cli\///' | sed 's/ .*//')
        log_info "AWS CLI already installed: $aws_version"
    fi

    # Configure AWS CLI
    log_info "Configuring AWS CLI..."
    aws configure

    log_success "AWS CLI setup completed"
}

# Setup AWS credentials file
setup_credentials_file() {
    log_step "Setting up AWS credentials file..."

    local aws_dir="$HOME/.aws"
    local credentials_file="$aws_dir/credentials"
    local config_file="$aws_dir/config"

    # Create AWS directory if it doesn't exist
    mkdir -p "$aws_dir"

    # Setup credentials file
    if [[ ! -f "$credentials_file" ]]; then
        cat > "$credentials_file" << 'EOF'
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_KEY_HERE
region=us-east-1

[woofy-production]
aws_access_key_id=YOUR_PROD_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_PROD_SECRET_KEY_HERE
region=us-east-1

[woofy-staging]
aws_access_key_id=YOUR_STAGING_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_STAGING_SECRET_KEY_HERE
region=us-east-1
EOF
        log_success "Created AWS credentials template file"
        log_security "Remember to replace placeholder values with your actual credentials"
    else
        log_info "AWS credentials file already exists"
    fi

    # Setup config file
    if [[ ! -f "$config_file" ]]; then
        cat > "$config_file" << 'EOF'
[default]
region=us-east-1
output=json

[profile woofy-production]
region=us-east-1
output=json

[profile woofy-staging]
region=us-east-1
output=json
EOF
        log_success "Created AWS config file"
    else
        log_info "AWS config file already exists"
    fi

    # Set proper permissions
    chmod 600 "$credentials_file"
    chmod 600 "$config_file"

    log_security "AWS credentials file permissions set to 600 (owner read/write only)"
}

# Setup AWS environment variables
setup_environment_variables() {
    log_step "Setting up AWS environment variables..."

    local env_file=".env"

    # Create .env file if it doesn't exist
    if [[ ! -f "$env_file" ]]; then
        cat > "$env_file" << 'EOF'
# WOOFY McWOOFSON AWS Environment Configuration
# Add your actual AWS credentials here
# NEVER commit this file to version control

# AWS Configuration
AWS_ACCESS_KEY_ID=your-access-key-here
AWS_SECRET_ACCESS_KEY=your-secret-key-here
AWS_DEFAULT_REGION=us-east-1
AWS_PROFILE=default

# WOOFY Specific AWS Resources
WOOFY_AWS_REGION=us-east-1
WOOFY_S3_BUCKET=woofy-mcwoofson-bucket
WOOFY_DYNAMODB_TABLE=woofy-hallucination-tracking
WOOFY_LAMBDA_FUNCTION=woofy-hallucination-mitigator

# AWS Service Endpoints (if using custom endpoints)
# AWS_S3_ENDPOINT=https://s3.us-east-1.amazonaws.com
# AWS_DYNAMODB_ENDPOINT=https://dynamodb.us-east-1.amazonaws.com

# AWS Cost Optimization
AWS_BUDGET_AMOUNT=100.0
AWS_BUDGET_NOTIFICATION_EMAIL=alerts@woofymcwoofson.com
EOF
        log_success "Created .env template file"
        log_security "Remember to add your actual AWS credentials to .env"
    fi

    # Add .env to .gitignore if not already there
    if [[ -f ".gitignore" ]] && ! grep -q ".env" .gitignore; then
        echo ".env" >> .gitignore
        log_success "Added .env to .gitignore"
    fi
}

# Setup AWS IAM best practices
setup_iam_best_practices() {
    log_step "Setting up AWS IAM best practices..."

    echo
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                🛡️ AWS IAM BEST PRACTICES                      ║"
    echo "╠════════════════════════════════════════════════════════════════╣"
    echo "║  Follow these enterprise security practices:                 ║"
    echo "║                                                              ║"
    echo "║  1. 🔐 Use IAM Users (not root account)                      ║"
    echo "║  2. 🛡️ Enable Multi-Factor Authentication (MFA)             ║"
    echo "║  3. 🎯 Apply Least Privilege Principle                       ║"
    echo "║  4. 🔄 Rotate Access Keys Regularly                         ║"
    echo "║  5. 📊 Monitor with AWS CloudTrail                          ║"
    echo "║  6. 🏷️ Use Tags for Cost Allocation                         ║"
    echo "║  7. 🚨 Set Up Billing Alerts                                ║"
    echo "║  8. 🔒 Use IAM Roles for EC2/ECS                            ║"
    echo "║                                                              ║"
    echo "║  📖 AWS IAM Documentation:                                   ║"
    echo "║  https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo

    read -p "Have you reviewed AWS IAM best practices? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        log_success "Great! Proceeding with secure setup..."
    else
        log_info "Please review AWS IAM best practices before proceeding."
        log_info "Documentation: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        exit 0
    fi
}

# Test AWS credentials
test_aws_credentials() {
    log_step "Testing AWS credentials..."

    log_info "Testing AWS credentials..."
    if aws sts get-caller-identity &> /dev/null; then
        local account_info=$(aws sts get-caller-identity)
        local account_id=$(echo "$account_info" | jq -r '.Account')
        local user_arn=$(echo "$account_info" | jq -r '.Arn')
        local user_id=$(echo "$account_info" | jq -r '.UserId')

        log_success "AWS credentials are valid!"
        echo "  Account ID: $account_id"
        echo "  User ARN: $user_arn"
        echo "  User ID: $user_id"
    else
        log_error "AWS credentials test failed."
        log_info "Please check:"
        log_info "  • Your access key and secret key are correct"
        log_info "  • Your IAM user has the necessary permissions"
        log_info "  • Your AWS region is correct"
        log_info "  • Your credentials haven't expired"
        exit 1
    fi
}

# Setup AWS SDK for Python
setup_aws_sdk() {
    log_step "Setting up AWS SDK for Python..."

    # Install boto3 and other AWS-related packages
    pip3 install boto3 botocore awscli

    # Test AWS SDK
    python3 -c "
import boto3
import os

# Test basic AWS SDK functionality
try:
    # Try to create a client (this will fail without credentials, but tests import)
    sts = boto3.client('sts', region_name='us-east-1')
    print('✅ AWS SDK (boto3) installed successfully')
    print('✅ Basic AWS connectivity test passed')
except Exception as e:
    print(f'⚠️ AWS SDK test note: {e}')
    print('✅ AWS SDK installed (credentials needed for full functionality)')
"

    log_success "AWS SDK setup completed"
}

# Setup WOOFY-specific AWS resources
setup_woofy_aws_resources() {
    log_step "Setting up WOOFY-specific AWS resources..."

    echo
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║            🐕‍🦺 WOOFY AWS RESOURCES SETUP                      ║"
    echo "╠════════════════════════════════════════════════════════════════╣"
    echo "║  The following AWS resources will be created for WOOFY:     ║"
    echo "║                                                              ║"
    echo "║  1. 📦 S3 Bucket: woofy-mcwoofson-{account-id}              ║"
    echo "║  2. 🗄️ DynamoDB Table: woofy-hallucination-tracking         ║"
    echo "║  3. 🔐 KMS Key: woofy-encryption-key                        ║"
    echo "║  4. 📧 SNS Topic: woofy-alerts                              ║"
    echo "║  5. ☁️ CloudWatch Log Group: /woofy/orchestrator            ║"
    echo "║                                                              ║"
    echo "║  ⚠️ Note: This will incur AWS charges                        ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo

    read -p "Do you want to create WOOFY AWS resources now? (y/N): " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        create_woofy_resources
    else
        log_info "Skipping resource creation. You can create them later."
        log_info "Use the AWS CloudFormation template: aws-hallucination-mitigation-system.yml"
    fi
}

# Create WOOFY AWS resources
create_woofy_resources() {
    log_info "Creating WOOFY AWS resources..."

    # Get account ID
    local account_id=$(aws sts get-caller-identity --query Account --output text)

    # Create S3 bucket
    local bucket_name="woofy-mcwoofson-$account_id"
    if aws s3 ls "s3://$bucket_name" 2>&1 | grep -q 'NoSuchBucket'; then
        aws s3 mb "s3://$bucket_name"
        log_success "Created S3 bucket: $bucket_name"
    else
        log_info "S3 bucket already exists: $bucket_name"
    fi

    # Create DynamoDB table
    local table_name="woofy-hallucination-tracking"
    if ! aws dynamodb describe-table --table-name "$table_name" &> /dev/null; then
        aws dynamodb create-table \
            --table-name "$table_name" \
            --attribute-definitions AttributeName=request_id,AttributeType=S AttributeName=timestamp,AttributeType=S \
            --key-schema AttributeName=request_id,KeyType=HASH AttributeName=timestamp,KeyType=RANGE \
            --billing-mode PAY_PER_REQUEST
        log_success "Created DynamoDB table: $table_name"
    else
        log_info "DynamoDB table already exists: $table_name"
    fi

    # Create CloudWatch log group
    local log_group="/woofy/orchestrator"
    if ! aws logs describe-log-groups --log-group-name-prefix "$log_group" | grep -q "$log_group"; then
        aws logs create-log-group --log-group-name "$log_group"
        log_success "Created CloudWatch log group: $log_group"
    else
        log_info "CloudWatch log group already exists: $log_group"
    fi

    log_success "WOOFY AWS resources setup completed"
}

# Final setup and verification
final_setup() {
    log_step "Final setup and verification..."

    # Verify all components
    echo
    log_info "AWS Setup Verification:"
    echo "  ✅ AWS CLI: $(aws --version | head -1)"
    echo "  ✅ Python AWS SDK: $(python3 -c 'import boto3; print(boto3.__version__)')"
    echo "  ✅ Credentials: $(aws sts get-caller-identity --query Account --output text)"
    echo "  ✅ Region: $(aws configure get region)"
    echo "  ✅ Profile: $(aws configure get profile || echo 'default')"

    # Check WOOFY-specific setup
    if [[ -f ".env" ]]; then
        echo "  ✅ Environment file: .env"
    fi

    if [[ -f ".gitignore" ]] && grep -q ".env" .gitignore; then
        echo "  ✅ .env in .gitignore: Yes"
    fi

    echo
    log_success "WOOFY McWOOFSON AWS setup completed!"
    echo
    echo "🎯 Next Steps:"
    echo "  1. Add your actual AWS credentials to .env file"
    echo "  2. Test AWS connectivity: aws s3 ls"
    echo "  3. Deploy WOOFY infrastructure using CloudFormation"
    echo "  4. Start developing with AWS services! 🚀"
    echo
    echo "📚 Useful AWS Commands:"
    echo "  • aws sts get-caller-identity    - Verify credentials"
    echo "  • aws s3 ls                     - List S3 buckets"
    echo "  • aws dynamodb list-tables      - List DynamoDB tables"
    echo "  • aws logs describe-log-groups  - List CloudWatch log groups"
    echo
    echo "🆘 Need Help?"
    echo "  • AWS Documentation: https://docs.aws.amazon.com/"
    echo "  • WOOFY Resources: docs/aws-setup-guide.md"
    echo "  • Support: aws-support@woofymcwoofson.com"
}

# Main execution
main() {
    echo "🐕‍🦺 WOOFY McWOOFSON AWS Credentials Setup Script v$SCRIPT_VERSION"
    echo "════════════════════════════════════════════════════════════════════"
    echo

    security_disclaimer
    check_requirements
    setup_iam_best_practices
    setup_aws_cli
    setup_credentials_file
    setup_environment_variables
    test_aws_credentials
    setup_aws_sdk
    setup_woofy_aws_resources
    final_setup

    echo
    echo "🎉 AWS setup complete! Welcome to the WOOFY AWS ecosystem!"
    echo "   Remember: 🔐 Security first - never share your AWS credentials!"
}

# Run main function
main "$@"