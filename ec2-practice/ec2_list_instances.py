# EC2 Instance Lister
import boto3

ec2 = boto3.client(
    'ec2',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

response = ec2.describe_instances()
print("=" * 60)
print("MY EC2 INSTANCES")
print("=" * 60)

instance_count = 0
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_count += 1
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        state = instance['State']['Name']

        if state == 'running':
            emoji = '🟢'
        elif state == 'stopped':
            emoji = '🔴'
        else:
            emoji = '🟡'

        print(f"{emoji} Instance ID: {instance_id}")
        print(f"   Type: {instance_type}")
        print(f"   State: {state}")
        print()

print(f"Total instances: {instance_count}")
