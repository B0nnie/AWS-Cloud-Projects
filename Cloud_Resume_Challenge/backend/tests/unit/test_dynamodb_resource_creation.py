import boto3
import pytest
from unittest.mock import Mock
from backend.source.counter import lambda_handler

# Mock the boto3.resource function
@pytest.fixture
def mock_dynamodb_resource(monkeypatch):
    mock_resource = Mock()
    monkeypatch.setattr(boto3, 'resource', mock_resource)
    return mock_resource

def test_dynamodb_resource_creation(mock_dynamodb_resource):
    # Call the lambda_handler function (or any method that triggers the DynamoDB resource creation)
    event = {}  # Provide any necessary event data
    context = {}  # Provide any necessary context data
    lambda_handler(event, context)

    # Assert that boto3.resource was called with the correct parameters
    expected_service = 'dynamodb'
    mock_dynamodb_resource.assert_called_once_with(expected_service)

    # Assert that the correct DynamoDB table was obtained
    expected_table_name = 'Cloud_Resume_Challenge_'
    mock_dynamodb_resource().Table.assert_called_once_with(expected_table_name)