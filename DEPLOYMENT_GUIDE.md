# WOOFY McWOOFSON Deployment Guide

## Quick Deploy Commands

### Staging Deployment
```bash
# Deploy to staging
git push origin develop
# Or manual deploy
python deploy/staging_deploy.py
```

### Production Deployment
```bash
# Deploy to production
git push origin main
# Or manual deploy
python deploy/production_deploy.py
```

## Infrastructure Setup

### Terraform Deployment
```bash
cd terraform
terraform init
terraform plan -var="environment=production"
terraform apply -var="environment=production"
```

### AWS Services
- **Lambda**: Serverless compute for AI processing
- **S3**: Storage for generated content and assets
- **DynamoDB**: NoSQL database for user data and analytics
- **CloudWatch**: Monitoring and logging

### Perplexity Integration
- API key configured in environment variables
- Real-time market analysis and AI insights
- Enhanced search capabilities for content generation

## Rollback Strategy
```bash
# Create snapshot before deployment
python -c "from deploy.rollback_strategy import RollbackStrategy; RollbackStrategy().create_snapshot('production')"

# Rollback if needed
python -c "from deploy.rollback_strategy import RollbackStrategy; RollbackStrategy().rollback_to_snapshot('production', 'SNAPSHOT_ID')"
```

## Environment Variables
```
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
PERPLEXITY_API_KEY=your_perplexity_key
ENVIRONMENT=production
```

## Health Checks
- Automated health checks in CI/CD pipeline
- Manual health check: `python -c "from woofy_orchestrator import WoofyOrchestrator; print(WoofyOrchestrator().health_check())"`

## Revenue Monitoring
- Real-time analytics via Perplexity market insights
- DynamoDB stores user interaction data
- CloudWatch dashboards for revenue tracking