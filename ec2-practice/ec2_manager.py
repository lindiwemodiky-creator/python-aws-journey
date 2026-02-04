# EC2 Instance Manager - YOUR FINAL TOOL
import boto3

ec2 = boto3.client('ec2', endpoint_url='http://localhost:4566',
                   aws_access_key_id='test', aws_secret_access_key='test', region_name='us-east-1')


def list_instances():
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] != 'terminated':
                instances.append({
                    'id': instance['InstanceId'],
                    'type': instance['InstanceType'],
                    'state': instance['State']['Name']
                })
    return instances


def show_menu():
    print("\n" + "=" * 60)
    print("EC2 INSTANCE MANAGER")
    print("=" * 60)
    print("1. List instances")
    print("2. Stop instance")
    print("3. Start instance")
    print("4. Terminate instance")
    print("5. Exit")
    print()


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            instances = list_instances()
            if not instances:
                print("\n❌ No instances found")
            else:
                print(f"\n📋 Found {len(instances)} instance(s):")
                for inst in instances:
                    emoji = '🟢' if inst['state'] == 'running' else '🔴' if inst['state'] == 'stopped' else '🟡'
                    print(
                        f"{emoji} {inst['id']} - {inst['type']} ({inst['state']})")

        elif choice == '2':
            instance_id = input("\nInstance ID to stop: ")
            try:
                ec2.stop_instances(InstanceIds=[instance_id])
                print(f"✅ Stopping {instance_id}...")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == '3':
            instance_id = input("\nInstance ID to start: ")
            try:
                ec2.start_instances(InstanceIds=[instance_id])
                print(f"✅ Starting {instance_id}...")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == '4':
            instance_id = input("\nInstance ID to terminate: ")
            confirm = input(
                f"⚠️ Are you sure you want to DELETE {instance_id}? (yes/no): ")
            if confirm.lower() == 'yes':
                try:
                    ec2.terminate_instances(InstanceIds=[instance_id])
                    print(f"✅ Terminating {instance_id}...")
                except Exception as e:
                    print(f"❌ Error: {e}")
            else:
                print("❌ Cancelled")

        elif choice == '5':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice")


if __name__ == "__main__":
    main()
