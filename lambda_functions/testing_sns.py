import json
import boto3

print('Loading function')
table_name = 'myo_data'
DB = boto3.resource('dynamodb')
table = DB.Table(table_name)

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    response = table.put_item(
        Item={
            'id': '3',
            'foo': message,
        })
    print("From SNS: " + message)
    return message
