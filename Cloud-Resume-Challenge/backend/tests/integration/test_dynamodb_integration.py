import json
import boto3
import moto
import pytest
from backend.source.counter import  lambda_handler

@pytest.fixture
def dynamodb_mock():
    with moto.mock_dynamodb():
        yield boto3.client("dynamodb")

def test_integration(dynamodb_mock):
    dynamodb_mock.create_table(
        TableName="Cloud_Resume_Challenge_",
        KeySchema=[{"AttributeName": "Page", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "Page", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )

    # Call the lambda_handler function
    event = {}  # Provide any necessary event data
    context = {}  # Provide any necessary context data
    result = lambda_handler(event, context)

    # Verify the response
    expected_response = {
        'updated_hits': 0,
        'statusCode': 200,
        'message': 'Initial item inserted successfully.',
        'item_count': 1
    }

    assert result['statusCode'] == expected_response['statusCode']
    assert json.loads(result['body']) == expected_response
