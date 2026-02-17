import boto3

ec2 = boto3.client('ec2', endpoint_url='http://localhost:4566',
                   aws_access_key_id='test', aws_secret_access_key='test', region_name='us-east-1')

print("=" * 60)
print("EC2 INSTANCE LAUNCHER")
print("=" * 60)

instance_type = input("Instance type (default: t2.micro): ") or "t2.micro"
count = int(input("How many instances? (default: 1): ") or "1")

print(f"Launching {count} x {instance_type} instance(s)...")

try:
    response = ec2.run_instances(
        ImageId='ami-ff0fea8310f3', InstanceType=instance_type, MinCount=count, MaxCount=count)
    print("✅ Success!")
    for instance in response['Instances']:
        print(f"   🟢 {instance['InstanceId']} ({instance_type})")
except Exception as e:
    print(f"❌ Error: {e}")

