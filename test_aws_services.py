from aws_services_integration import WoofyAWSServices

def main():
    woofy_aws = WoofyAWSServices()
    
    print("WOOFY McWOOFSON AWS Services Integration")
    print("=" * 50)
    
    # Generate configurations
    lambda_config = woofy_aws.deploy_lambda_function()
    print(f"SUCCESS: Lambda function configured: {lambda_config['FunctionName']}")
    
    s3_config, lifecycle = woofy_aws.setup_s3_art_storage()
    print(f"SUCCESS: S3 bucket configured: {s3_config['Bucket']}")
    
    tables = woofy_aws.setup_dynamodb_tables()
    print(f"SUCCESS: DynamoDB tables: {list(tables.keys())}")
    
    bedrock_config = woofy_aws.setup_bedrock_integration()
    print(f"SUCCESS: Bedrock AI configured: {bedrock_config['model_id']}")
    
    # Generate compliance report
    report = woofy_aws.generate_compliance_report()
    print(f"SUCCESS: Compliance status: {report['security_score']} - Enterprise Ready: {report['enterprise_ready']}")
    
    print("\nWOOFY McWOOFSON is AWS-powered and enterprise-ready!")
    
    return report

if __name__ == "__main__":
    main()