output "lambda_function_arn" {
  description = "ARN of the Lambda function"
  value       = aws_lambda_function.inference_function.arn
}

output "api_endpoint" {
  description = "URL of the API Gateway endpoint"
  value       = aws_api_gateway_deployment.deployment.invoke_url
}

