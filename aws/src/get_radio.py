# -*- coding: UTF-8 -*-
import json
import boto3

dynamodb = boto3.resource('dynamodb')
radio_table = dynamodb.Table('radio')


def lambda_handler(event, context):
    # request
    request_body = json.loads(event['body'])

    # response
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': None
    }
    response_body = {}

    weekday = int(request_body['weekday'])

    res = radio_table.scan(
        Limit=10
    )

    response_body.update({
        'items': str(res['Items'])
    })

    response['body'] = json.dumps(response_body)

    return response
