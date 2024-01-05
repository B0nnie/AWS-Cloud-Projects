import os
import boto3
import pytest
import requests

class TestApiIntegration:

    @pytest.fixture()
    def api_gateway_url(self):
        # Get the API Gateway URL from Cloudformation Stack outputs
        stack_name = os.environ.get("AWS_SAM_STACK_NAME")

        if stack_name is None:
            raise ValueError('Please set the AWS_SAM_STACK_NAME environment variable to the name of your stack')

        client = boto3.client("cloudformation")

        try:
            response = client.describe_stacks(StackName=stack_name)
        except Exception as e:
            raise Exception(
                f"Cannot find stack {stack_name} \n" f'Please make sure a stack with the name "{stack_name}" exists'
            ) from e

        stacks = response["Stacks"]
        stack_outputs = stacks[0]["Outputs"]
        api_outputs = [output for output in stack_outputs if output["OutputKey"] == "HttpEndpoint"]

        if not api_outputs:
            raise KeyError(f"HttpEndpoint not found in stack {stack_name}")

        return api_outputs[0]["OutputValue"]  # Extract url from stack outputs

    def test_api_integration(self, api_gateway_url):
        # Call the API Gateway endpoint and check the response
        response = requests.get(api_gateway_url)

        assert response.status_code == 200

        # Get the actual updated_hits value from the response
        actual_updated_hits = response.json().get('updated_hits')

        # Define the expected response dynamically
        expected_response = {
            "updated_hits": actual_updated_hits,
            "statusCode": 200,
            "message": "Item updated successfully.",
            "item_count": 1
        }

        assert response.json() == expected_response
