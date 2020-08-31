# -*- coding: UTF-8 -*-
import json
from decimal import Decimal
import boto3
from boto3.dynamodb.types import Binary

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

    response['body'] = json.dumps(res['Items'], default=default)

    return response


def default(obj) -> object:
    if isinstance(obj, Decimal):
        if int(obj) == obj:
            return int(obj)
        else:
            return float(obj)
    elif isinstance(obj, Binary):
        return obj.value
    elif isinstance(obj, bytes):
        return obj.decode()
    elif isinstance(obj, set):
        return list(obj)
    try:
        return str(obj)
    except Exception:
        return None