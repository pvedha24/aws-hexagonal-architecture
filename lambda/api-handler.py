import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserData')

def lambda_handler(event, context):
    try:
        http_method = event['httpMethod']
        
        if http_method == 'POST':
            body = json.loads(event['body'])
            user_id = body.get('userId')
            data = body.get('data')
            
            table.put_item(Item={
                'userId': user_id,
                'data': data
            })
            
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Data saved successfully'})
            }
        
        elif http_method == 'GET':
            user_id = event['queryStringParameters'].get('userId')
            response = table.get_item(Key={'userId': user_id})
            
            if 'Item' in response:
                return {
                    'statusCode': 200,
                    'body': json.dumps(response['Item'], default=str)
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'User not found'})
                }
                
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
