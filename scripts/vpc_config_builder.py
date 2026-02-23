import json

print("=" * 60)
print("VPC CONFIGURATION BUILDER")
print("=" * 60)

# Get user input
vpc_name = input("VPC Name: ")
vpc_cidr = input("VPC CIDR Block (default: 10.0.0.0/16): ") or "10.0.0.0/16"
region = input("AWS Region (default: us-east-1): ") or "us-east-1"

# Build the configuration
vpc_config = {
    "VPCName": vpc_name,
    "Region": region,
    "CIDR": vpc_cidr,
    "Subnets": [
        {
            "Name": f"{vpc_name}-public-subnet-1",
            "CIDR": "10.0.1.0/24",
            "AvailabilityZone": f"{region}a",
            "Public": True
        },
        {
            "Name": f"{vpc_name}-private-subnet-1",
            "CIDR": "10.0.2.0/24",
            "AvailabilityZone": f"{region}b",
            "Public": False
        }
    ],
    "SecurityGroups": [
        {
            "Name": f"{vpc_name}-web-sg",
            "Description": "Allow HTTP and HTTPS traffic",
            "InboundRules": [
                {"Protocol": "TCP", "Port": 80, "Source": "0.0.0.0/0"},
                {"Protocol": "TCP", "Port": 443, "Source": "0.0.0.0/0"}
            ]
        }
    ]
}

# Save to file
filename = f"{vpc_name.replace(' ', '-').lower()}-vpc-config.json"
with open(filename, 'w') as f:
    json.dump(vpc_config, f, indent=2)

print(f"\n✅ VPC configuration saved to: {filename}")
print("=" * 60)