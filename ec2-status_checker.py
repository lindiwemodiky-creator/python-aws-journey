import boto3

# Connect to LocalStack EC2
ec2 = boto3.client(
    'ec2',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

print("=" * 60)
print("EC2 INSTANCE STATUS CHECKER")
print("=" * 60)

# Get all instances
response = ec2.describe_instances()

# Count instances
instance_count = 0

# Loop through reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_count += 1
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        state = instance['State']['Name']

        # Color-code the state
        if state == 'running':
            emoji = '🟢'
        elif state == 'stopped':
            emoji = '🔴'
        else:
            emoji = '🟡'

        print(f"{emoji} {instance_id} | Type: {instance_type} | State: {state}")

print("=" * 60)
print(f"Total instances: {instance_count}")
print("=" * 60)
