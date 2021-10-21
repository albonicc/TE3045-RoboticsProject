import json
import boto3

table_name = 'myo_data'
DB = boto3.resource('dynamodb')
table = DB.Table(table_name)

def lambda_handler(event, context):
    response = table.put_item(
        Item={
            'id': '2',
            'foo': 'bar',
            'hola': 'mundo'
        })
    response['ResponseMetadata']['HTTPStatusCode']
    print('Im here')
    # TODO implement
    
