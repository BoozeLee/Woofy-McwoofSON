import json

def lambda_handler(event, context):
    """
    🐶 Woofy Lambda Handler
    Receives API Gateway requests and returns a friendly dog-themed response.
    """
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': "Woofy McWoofson says: Hello, enterprise world! 🐾"
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
