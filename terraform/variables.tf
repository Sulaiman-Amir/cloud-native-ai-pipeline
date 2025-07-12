variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
}

variable "s3_bucket_name" {
  description = "S3 bucket for storing models or data"
  type        = string
}

variable "api_gateway_name" {
  description = "Name of the API Gateway"
  type        = string
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

