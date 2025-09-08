#!/bin/bash
# 🐾 WOOFY McWOOFSON Deployment Script

echo "Deploying WOOFY to AWS..."

# Example deployment steps
npm run build
docker build -t woofy-mcwoofson .
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ECR_URL
docker tag woofy-mcwoofson:latest $AWS_ECR_URL/woofy-mcwoofson:latest
docker push $AWS_ECR_URL/woofy-mcwoofson:latest

echo "Deployment complete! 🐕🚀"