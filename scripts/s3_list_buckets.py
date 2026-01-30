import boto3

# Connect to LocalStack S3 (your local AWS)
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test', 
    region_name='us-east-1'
)

# Get all your S3 buckets
response = s3.list_buckets()

print("=" * 50)
print("MY S3 BUCKETS")
print("=" * 50)
for bucket in response['Buckets']:
    print(f"📦 {bucket['Name']}")
print(f"Total: {len(response['Buckets'])} buckets")
print("=" * 50)
