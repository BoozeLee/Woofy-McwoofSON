terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Lambda Function
resource "aws_lambda_function" "woofy_function" {
  filename         = "lambda_function.zip"
  function_name    = "woofy-${var.environment}"
  role            = aws_iam_role.lambda_role.arn
  handler         = "lambda_function.lambda_handler"
  runtime         = "python3.9"
  timeout         = 30

  environment {
    variables = {
      ENVIRONMENT = var.environment
      PERPLEXITY_API_KEY = var.perplexity_api_key
    }
  }
}

# S3 Bucket
resource "aws_s3_bucket" "woofy_bucket" {
  bucket = "woofy-${var.environment}-${random_id.bucket_suffix.hex}"
}

resource "aws_s3_bucket_versioning" "woofy_bucket_versioning" {
  bucket = aws_s3_bucket.woofy_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

# DynamoDB Table
resource "aws_dynamodb_table" "woofy_table" {
  name           = "woofy-${var.environment}-data"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "woofy-lambda-role-${var.environment}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}