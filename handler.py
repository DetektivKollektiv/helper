import json
import os
import boto3
import time

def create_invalidation(event, context):
    client = boto3.client('cloudfront')
    
    distributionId = event['CodePipeline.job']['data']['actionConfiguration']['configuration']['UserParameters']

    invalidation = client.create_invalidation(
        DistributionId=distributionId,
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