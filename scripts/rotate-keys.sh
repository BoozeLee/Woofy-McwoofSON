#!/bin/bash
# 🐾 WOOFY Key Rotation Script

echo "Rotating AWS IAM keys..."

aws iam create-access-key --user-name $IAM_USER > new-aws-keys.json
# Update secrets in AWS Secrets Manager or SSM here

echo "Remember to update GitHub Actions secrets and redeploy!"