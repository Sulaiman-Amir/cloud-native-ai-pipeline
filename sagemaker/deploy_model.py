import boto3

sm = boto3.client('sagemaker')

response = sm.create_model(
    ModelName='topg-rf-model',
    PrimaryContainer={
        'Image': '683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:0.23-1-cpu-py3',
        'ModelDataUrl': 's3://your-bucket-name/path-to/model.tar.gz'
    },
    ExecutionRoleArn='arn:aws:iam::your-account-id:role/SageMakerExecutionRole'
)

print("Model Deployed:", response['ModelArn'])

