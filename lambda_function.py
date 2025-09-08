import json
import boto3
import os

def lambda_handler(event, context):
    """WOOFY McWOOFSON Production Handler"""
    
    prompt = event.get('prompt', 'atomic psychedelic dog')
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'WOOFY McWOOFSON is live!',
            'prompt': prompt,
            'status': 'production'
        })
    }
