import json
import os
import boto3

def create_invalidation(event, context):
    client = boto3.client('cloudfront')
    
    invalidation = client.create_invalidation(
        DistributionId=os.environ['DISTRIBUTION_ID'],
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': ['/*']
        },
        'CallerReference': str(time.time())
    })
    
    pipeline = boto3.client('codepipeline')
    
    response = pipeline.put_job_success_result(
        jobId=event['CodePipeline.job']['id']
    )
    
    return response
