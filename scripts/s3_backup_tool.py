import boto3
import os

# Connect to S3
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

BACKUP_BUCKET = 'data-backups'

print("=" * 50)
print("S3 BACKUP TOOL")
print("=" * 50)

# Get file from user
file_path = input("Enter full path to backup: ")

# Check if file exists
if not os.path.exists(file_path):
    print(f"❌ File not found: {file_path}")
else:
    filename = os.path.basename(file_path)
    print(f"📤 Uploading {filename}...")
    try:
        s3.upload_file(file_path, BACKUP_BUCKET, filename)
        print(f"✅ BACKED UP to s3://{BACKUP_BUCKET}/{filename}")
    except Exception as e:
        print(f"❌ Failed: {e}")
