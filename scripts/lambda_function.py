import json


def lambda_handler(event, context):
    """
    This function gets triggered when a file is uploaded to S3.
    It logs information about the uploaded file.
    """

    # Get information about the uploaded file from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    print(f"🎉 File uploaded!")
    print(f"   Bucket: {bucket}")
    print(f"   File: {file_key}")

    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully processed {file_key}')
    }

