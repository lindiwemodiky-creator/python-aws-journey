import json
import os

print("=" * 60)
print("VPC CONFIGURATION READER")
print("=" * 60)

# Ask user for config file
config_file = input(
    "\nEnter config filename (or press Enter for default): ") or "my-test-vpc-vpc-config.json"

# Check if file exists
if not os.path.exists(config_file):
    print(f"\n❌ Error: File '{config_file}' not found!")
else:
    # Read the JSON file
    with open(config_file, 'r') as f:
        config = json.load(f)

    # Print it nicely
    print(f"\n📋 VPC Configuration Summary")
    print("=" * 60)
    print(f"VPC Name: {config['VPCName']}")
    print(f"Region: {config['Region']}")
    print(f"CIDR Block: {config['CIDR']}")

    print(f"\n📌 Subnets ({len(config['Subnets'])} total):")
    for subnet in config['Subnets']:
        subnet_type = "Public" if subnet['Public'] else "Private"
        print(f"   • {subnet['Name']}")
        print(f"     Type: {subnet_type}")
        print(f"     CIDR: {subnet['CIDR']}")
        print(f"     AZ: {subnet['AvailabilityZone']}")

    print(f"\n🔒 Security Groups ({len(config['SecurityGroups'])} total):")
    for sg in config['SecurityGroups']:
        print(f"   • {sg['Name']}")
        print(f"     {sg['Description']}")
        print(f"     Rules:")
        for rule in sg['InboundRules']:
            print(
                f"       - Allow {rule['Protocol']} on port {rule['Port']} from {rule['Source']}")

    print("\n" + "=" * 60)
