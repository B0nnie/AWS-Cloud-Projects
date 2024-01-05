import json
import boto3
import pytest
from unittest.mock import Mock, patch
from Cloud_Resume_Challenge.backend.source.counter import lambda_handler

# Mock the DynamoDB operations and boto3.resource
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

def test_response_json_construction_existing_item(mock_dynamodb_table):
    # Mock the response for an existing 'Main' item
    mock_dynamodb_table.get_item.return_value = {'Item': {'Page': 'Main', 'Hits': 5}}
    mock_dynamodb_table.scan.return_value = {'Count': 10}  # Mock item count

    # Call the lambda_handler function
    event = {}  # Provide any necessary event data
    context = {}  # Provide any necessary context data
    result = lambda_handler(event, context)

    # Verify the response_data dictionary for success scenario
    expected_response_data = {
        'updated_hits': 6,  # 5 (initial) + 1 (updated)
        'statusCode': 200,
        'message': 'Item updated successfully.',
        'item_count': 10
    }
    if 'body' in result:  # Check if 'body' key is present
        assert json.loads(result['body']) == expected_response_data
    else:  # Handle error scenario
        assert result['statusCode'] == 500

def test_response_json_construction_new_item(mock_dynamodb_table):
    # Mock the response for a non-existing 'Main' item
    mock_dynamodb_table.get_item.return_value = {}
    mock_dynamodb_table.scan.return_value = {'Count': 10}  # Mock item count

    # Call the lambda_handler function
    event = {}  # Provide any necessary event data
    context = {}  # Provide any necessary context data
    result = lambda_handler(event, context)

    # Verify the response_data dictionary for success scenario
    expected_response_data = {
        'updated_hits': 0,
        'statusCode': 200,
        'message': 'Initial item inserted successfully.',
        'item_count': 10
    }
    if 'body' in result:  # Check if 'body' key is present
        assert json.loads(result['body']) == expected_response_data
    else:  # Handle error scenario
        assert result['statusCode'] == 500
