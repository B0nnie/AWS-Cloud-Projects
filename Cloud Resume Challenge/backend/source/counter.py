import json
import boto3

def lambda_handler(event, context):

    # Create a DynamoDB client with endpoint-url for local testing
    #dynamodb = boto3.resource('dynamodb', endpoint_url='http://172.16.123.1:8000')

    # Create a DynamoDB client
    dynamodb = boto3.resource('dynamodb')

    # Get the DynamoDB table
    table = dynamodb.Table('Cloud_Resume_Challenge_')

    try:
        # Check if the item with 'Page' attribute set to 'Main' already exists
        response = table.get_item(Key={'Page': 'Main'})

        if 'Item' in response:
            # If 'Main' item exists, update the 'Hits' attribute by 1
            response = table.update_item(
                Key={'Page': 'Main'},
                UpdateExpression='SET Hits = Hits + :val',
                ExpressionAttributeValues={':val': 1},
                ReturnValues='UPDATED_NEW'
            )

            # Get the updated value from the response
            updated_hits = int(response['Attributes']['Hits'])  # Cast to int
            message = 'Item updated successfully.'
        else:
            # If 'Main' item doesn't exist, insert the initial item
            table.put_item(Item={'Page': 'Main', 'Hits': 0})
            updated_hits = 0
            message = 'Initial item inserted successfully.'

        # Get the number of items currently in the table
        response = table.scan(Select='COUNT')
        item_count = response['Count']

        # Construct the response JSON
        response_data = {
            'updated_hits': updated_hits,
            'statusCode': 200,
            'message': message,
            'item_count': item_count
        }

        return {
            'statusCode': 200,
            'body': json.dumps(response_data)
        }
    except Exception as e:
        # Handle the exception and return an error message
        error_message = f'Error inserting/updating item: {str(e)}'
        return {
            'statusCode': 500,
            'error': error_message
        }
