import json
import os

print("=" * 60)
print("VPC CONFIGURATION EDITOR")
print("=" * 60)

# Ask for config file
config_file = input("\nEnter config filename: ")

# Check if file exists
if not os.path.exists(config_file):
    print(f"\n❌ Error: File '{config_file}' not found!")
else:
    # Read the JSON file
    with open(config_file, 'r') as f:
        config = json.load(f)

    print(f"\n📋 Current VPC: {config['VPCName']}")
    print(f"   Region: {config['Region']}")
    print(f"   Subnets: {len(config['Subnets'])}")
    print(f"   Security Groups: {len(config['SecurityGroups'])}")

    # Menu
    print("\n" + "=" * 60)
    print("What would you like to do?")
    print("1. Add a new subnet")
    print("2. Add a security group rule")
    print("3. Change VPC name")
    print("=" * 60)

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        # Add subnet
        subnet_name = input("New subnet name: ")
        subnet_cidr = input("Subnet CIDR (e.g., 10.0.3.0/24): ")
        is_public = input("Is this subnet public? (yes/no): ").lower() == "yes"
        az = input("Availability Zone (e.g., us-east-1c): ")

        new_subnet = {
            "Name": subnet_name,
            "CIDR": subnet_cidr,
            "AvailabilityZone": az,
            "Public": is_public
        }

        config['Subnets'].append(new_subnet)
        print(f"\n✅ Added subnet: {subnet_name}")

    elif choice == "2":
        # Add security group rule
        # Use first security group
        sg_name = config['SecurityGroups'][0]['Name']
        protocol = input("Protocol (TCP/UDP): ").upper()
        port = int(input("Port number: "))
        source = input("Source (e.g., 0.0.0.0/0 for anywhere): ")

        new_rule = {
            "Protocol": protocol,
            "Port": port,
            "Source": source
        }

        config['SecurityGroups'][0]['InboundRules'].append(new_rule)
        print(f"\n✅ Added rule: Allow {protocol} on port {port} from {source}")

    elif choice == "3":
        # Change VPC name
        new_name = input("New VPC name: ")
        old_name = config['VPCName']
        config['VPCName'] = new_name
        print(f"\n✅ Changed VPC name from '{old_name}' to '{new_name}'")

    else:
        print("\n❌ Invalid choice!")
        exit()

    # Save the modified config
    output_file = config_file.replace(".json", "-modified.json")
    with open(output_file, 'w') as f:
        json.dump(config, f, indent=2)

    print(f"\n💾 Modified config saved to: {output_file}")
    print("=" * 60)
