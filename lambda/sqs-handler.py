import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserData')

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            message_body = json.loads(record['body'])
            user_id = message_body.get('userId')
            data = message_body.get('data')
            
            table.put_item(Item={
                'userId': user_id,
                'data': data,
                'processed': True
            })
        
        return {
            'statusCode': 200,
            'body': json.dumps('Messages processed successfully')
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
