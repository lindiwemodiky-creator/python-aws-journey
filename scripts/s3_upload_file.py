import boto3

# Connect to LocalStack S3
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Upload file
local_file = 'C:\\aws-learning\\index.html'
bucket_name = 'data-backups'
s3_file_name = 'index.html'

print(f"Uploading {local_file} to s3://{bucket_name}/{s3_file_name}...")
try:
    s3.upload_file(local_file, bucket_name, s3_file_name)
    print("✅ Upload successful!")
except Exception as e:
    print(f"❌ Upload failed: {e}")
