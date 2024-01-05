import boto3
import pytest
from unittest.mock import Mock, patch
from Cloud_Resume_Challenge.backend.source.counter import lambda_handler

# Mock the boto3.resource function and DynamoDB operations
@pytest.fixture
def mock_dynamodb_resource(monkeypatch):
    mock_resource = Mock()
    monkeypatch.setattr(boto3, 'resource', mock_resource)
    return mock_resource

@pytest.fixture
def mock_dynamodb_table(mock_dynamodb_resource):
    mock_table = Mock()
    mock_dynamodb_resource().Table = Mock(return_value=mock_table)
    return mock_table

def test_dynamodb_operations_existing_item(mock_dynamodb_table):
    # Mock the response for an existing 'Main' item
    mock_dynamodb_table.get_item.return_value = {'Item': {'Page': 'Main', 'Hits': 5}}

    # Call the lambda_handler function
    event = {}  # Provide any necessary event data
    context = {}  # Provide any necessary context data
    result = lambda_handler(event, context)

    # Assert that update_item was called correctly
    mock_dynamodb_table.update_item.assert_called_once_with(
        Key={'Page': 'Main'},
        UpdateExpression='SET Hits = Hits + :val',
        ExpressionAttributeValues={':val': 1},
        ReturnValues='UPDATED_NEW'
    )

def test_dynamodb_operations_new_item(mock_dynamodb_table):
    # Mock the response for a non-existing 'Main' item
    mock_dynamodb_table.get_item.return_value = {}

    # Call the lambda_handler function
    event = {}  # Provide any necessary event data
    context = {}  # Provide any necessary context data
    result = lambda_handler(event, context)

    # Assert that put_item was called correctly
    mock_dynamodb_table.put_item.assert_called_once_with(
        Item={'Page': 'Main', 'Hits': 0}
    )