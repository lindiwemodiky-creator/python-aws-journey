import json

# This is our Lambda function (same as before)


def lambda_handler(event, context):
    """
    Simulates what happens when a file is uploaded to S3
    """
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    print("=" * 60)
    print("🎉 LAMBDA FUNCTION TRIGGERED!")
    print("=" * 60)
    print(f"   Bucket: {bucket}")
    print(f"   File uploaded: {file_key}")
    print("=" * 60)

    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully processed {file_key}')
    }


# Simulate the S3 event
test_event = {
    "Records": [
        {
            "s3": {
                "bucket": {"name": "lambda-trigger-bucket"},
                "object": {"key": "vacation-photo.jpg"}
            }
        }
    ]
}

# Run the Lambda function locally
if __name__ == "__main__":
    result = lambda_handler(test_event, None)
    print("\n📤 Lambda Response:")
    print(result)
