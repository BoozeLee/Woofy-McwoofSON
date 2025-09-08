import pytest
import json
from aws_integration import WoofyAWSIntegration

class TestWoofyAWSCompliance:
    """Pytest suite for AWS compliance checks"""
    
    def setup_method(self):
        self.woofy_aws = WoofyAWSIntegration()
    
    def test_iam_policy_structure(self):
        """Test IAM policy has required security elements"""
        policy = self.woofy_aws.setup_security_compliance()
        
        assert "Version" in policy
        assert policy["Version"] == "2012-10-17"
        assert "Statement" in policy
        assert len(policy["Statement"]) >= 2
        
        # Check S3 permissions
        s3_statement = policy["Statement"][0]
        assert "s3:GetObject" in s3_statement["Action"]
        assert "s3:PutObject" in s3_statement["Action"]
    
    def test_lambda_function_config(self):
        """Test Lambda function configuration"""
        config = self.woofy_aws.create_lambda_function()
        
        assert config["Runtime"] == "python3.9"
        assert "woofy" in config["FunctionName"].lower()
        assert config["Handler"] == "lambda_function.lambda_handler"
        assert "Code" in config
    
    def test_cloudwatch_metrics(self):
        """Test CloudWatch monitoring setup"""
        metrics = self.woofy_aws.setup_cloudwatch_monitoring()
        
        assert isinstance(metrics, list)
        assert len(metrics) > 0
        
        metric = metrics[0]
        assert metric["MetricName"] == "WoofyRequests"
        assert metric["Unit"] == "Count"
        assert metric["Value"] == 1.0
    
    def test_s3_bucket_security(self):
        """Test S3 bucket security configuration"""
        bucket_config, encryption_config = self.woofy_aws.create_s3_bucket()
        
        assert "woofy" in bucket_config["Bucket"].lower()
        assert "CreateBucketConfiguration" in bucket_config
        
        # Check encryption
        assert "Rules" in encryption_config
        rule = encryption_config["Rules"][0]
        assert rule["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"] == "AES256"
    
    def test_compliance_report(self):
        """Test compliance report generation"""
        report = self.woofy_aws.generate_compliance_report()
        
        assert report["service"] == "WOOFY McWOOFSON"
        assert report["status"] == "COMPLIANT"
        assert "compliance_checks" in report
        assert "security_score" in report
        
        checks = report["compliance_checks"]
        assert "encryption" in checks
        assert "access_control" in checks
        assert "logging" in checks
        assert "monitoring" in checks
    
    def test_security_score(self):
        """Test security score meets enterprise standards"""
        report = self.woofy_aws.generate_compliance_report()
        score = int(report["security_score"].replace("%", ""))
        
        assert score >= 95, f"Security score {score}% below enterprise threshold"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])