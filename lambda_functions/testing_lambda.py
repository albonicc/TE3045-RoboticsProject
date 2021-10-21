from decimal import Decimal
import json
import boto3

table_name = 'testing_table'
DB = boto3.resource('dynamodb')
table = DB.Table(table_name)

def lambda_handler(event, context):
    response = table.put_item(
        Item=
        {
            "id": "1",
            "pod0": 80,
            "pod1": 57,
            "pod2": 35,
            "pod3": 29,
            "pod4": 0,
            "pod5": -15,
            "pod6": -27,
            "pod7": 26,
            "gyroscope_x": 500,
            "gyroscope_y": 412,
            "giroscope_z": -99,
            "accelerometer_x": -2,
            "accelerometer_y": 2,
            "accelerometer_z": 4,
            "orientation_x": -1,
            "orientation_y": 0,
            "orientation_z": Decimal('-0.3'),
            "orientation_w": Decimal('0.7')
        }
        )
    response['ResponseMetadata']['HTTPStatusCode']
    print('Data saved in DynamoDB!')


    '''
    '{"id": "1", "pod0": 80, "pod1": 57, "pod2": 35, "pod3": 29, "pod4": 0, "pod5": -15, "pod6": -27, "pod7": 26, "gyroscope_x": 500, "gyroscope_y": 412, "gyroscope_z": -99, "accelerometer_x": -2, "accelerometer_y": 2, "accelerometer_z": 4, "orientation_x": -1,"orientation_y": 0, "orientation_z": "-0.3", "orientation_w": "0.7"}'

{"id": "1", "pod0": 80, "pod1": 57, "pod2": 35, "pod3": 29, "pod4": 0, "pod5": -15, "pod6": -27, "pod7": 26, "gyroscope_x": 500, "gyroscope_y": 412, "gyroscope_z": -99, "accelerometer_x": -2, "accelerometer_y": 2, "accelerometer_z": 4, "orientation_x": -1,"orientation_y": 0, "orientation_z": "-0.3", "orientation_w": "0.7"}
    '''