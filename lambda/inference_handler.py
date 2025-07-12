import json
import boto3
import os

runtime = boto3.client("sagemaker-runtime")

ENDPOINT_NAME = os.environ.get("SAGEMAKER_ENDPOINT")

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        input_data = json.dumps(body['input'])

        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType='application/json',
            Body=input_data
        )

        result = json.loads(response['Body'].read().decode())
        return {
            'statusCode': 200,
            'body': json.dumps({'prediction': result})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

