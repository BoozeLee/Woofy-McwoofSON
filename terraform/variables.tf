variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment (staging/production)"
  type        = string
}

variable "perplexity_api_key" {
  description = "Perplexity API key"
  type        = string
  sensitive   = true
}