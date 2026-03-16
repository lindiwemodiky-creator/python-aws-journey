import json

print("=" * 60)
print("IAM ROLE CONFIGURATION GENERATOR")
print("=" * 60)

# Role templates
ROLE_TEMPLATES = {
    "lambda_s3_read": {
        "RoleName": "LambdaS3ReadRole",
        "Description": "Allows Lambda to read from S3 and write logs",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        },
        "Policies": [{
            "PolicyName": "S3ReadAccess",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": ["s3:GetObject", "s3:ListBucket"],
                        "Resource": ["arn:aws:s3:::YOUR-BUCKET", "arn:aws:s3:::YOUR-BUCKET/*"]
                    },
                    {
                        "Effect": "Allow",
                        "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
                        "Resource": "arn:aws:logs:*:*:*"
                    }
                ]
            }
        }]
    },
    "ec2_s3_full": {
        "RoleName": "EC2S3FullAccessRole",
        "Description": "Allows EC2 to read/write S3 and manage instances",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "ec2.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        },
        "Policies": [{
            "PolicyName": "S3FullAccess",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Action": ["s3:*"],
                    "Resource": "*"
                }]
            }
        }]
    },
    "lambda_dynamodb": {
        "RoleName": "LambdaDynamoDBRole",
        "Description": "Allows Lambda to read/write DynamoDB",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        },
        "Policies": [{
            "PolicyName": "DynamoDBAccess",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": ["dynamodb:GetItem", "dynamodb:PutItem", "dynamodb:UpdateItem", "dynamodb:Query"],
                        "Resource": "arn:aws:dynamodb:*:*:table/YOUR-TABLE"
                    },
                    {
                        "Effect": "Allow",
                        "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
                        "Resource": "arn:aws:logs:*:*:*"
                    }
                ]
            }
        }]
    }
}

print("\nAvailable role templates:")
print("1. lambda_s3_read - Lambda function with S3 read access")
print("2. ec2_s3_full - EC2 instance with full S3 access")
print("3. lambda_dynamodb - Lambda function with DynamoDB access")

choice = input("\nSelect template (1-3): ")

template_map = {
    "1": "lambda_s3_read",
    "2": "ec2_s3_full",
    "3": "lambda_dynamodb"
}

if choice not in template_map:
    print("❌ Invalid choice!")
    exit()

selected = ROLE_TEMPLATES[template_map[choice]]

# Customize
bucket_name = input("Enter S3 bucket name (or press Enter to skip): ")
table_name = input("Enter DynamoDB table name (or press Enter to skip): ")

# Replace placeholders
role_json = json.dumps(selected, indent=2)
if bucket_name:
    role_json = role_json.replace("YOUR-BUCKET", bucket_name)
if table_name:
    role_json = role_json.replace("YOUR-TABLE", table_name)

# Save
filename = f"{selected['RoleName']}.json"
with open(filename, 'w') as f:
    f.write(role_json)

print(f"\n✅ Role configuration saved to: {filename}")
print("=" * 60)