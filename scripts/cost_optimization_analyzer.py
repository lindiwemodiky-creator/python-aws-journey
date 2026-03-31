print("=" * 70)
print("AWS COST OPTIMIZATION ANALYZER")
print("=" * 70)

# Simulated AWS resource inventory
resources = {
    "ec2_instances": [
        {"id": "i-001", "type": "m5.xlarge", "pricing": "On-Demand",
            "cpu_avg": 15, "hours_per_day": 24},
        {"id": "i-002", "type": "t3.micro", "pricing": "On-Demand",
            "cpu_avg": 65, "hours_per_day": 24},
        {"id": "i-003", "type": "m5.large", "pricing": "Reserved",
            "cpu_avg": 75, "hours_per_day": 24},
        {"id": "i-004", "type": "t3.small", "pricing": "On-Demand",
            "cpu_avg": 20, "hours_per_day": 10},
        {"id": "i-005", "type": "m5.2xlarge", "pricing": "On-Demand",
            "cpu_avg": 12, "hours_per_day": 24}
    ],
    "s3_buckets": [
        {"name": "production-logs", "size_gb": 500,
            "storage_class": "Standard", "access_frequency": "daily"},
        {"name": "old-backups", "size_gb": 2000,
            "storage_class": "Standard", "access_frequency": "yearly"},
        {"name": "media-files", "size_gb": 300,
            "storage_class": "Standard-IA", "access_frequency": "monthly"}
    ],
    "ebs_volumes": [
        {"id": "vol-001", "size_gb": 100, "attached": True, "type": "gp3"},
        {"id": "vol-002", "size_gb": 200, "attached": False, "type": "gp3"},
        {"id": "vol-003", "size_gb": 50, "attached": False, "type": "gp2"}
    ],
    "elastic_ips": [
        {"ip": "52.1.2.3", "attached": True},
        {"ip": "52.1.2.4", "attached": False},
        {"ip": "52.1.2.5", "attached": False}
    ]
}

# Pricing (simplified, per hour/GB)
pricing = {
    "ec2": {
        "t3.micro": 0.0104, "t3.small": 0.0208, "t3.medium": 0.0416,
        "m5.large": 0.096, "m5.xlarge": 0.192, "m5.2xlarge": 0.384
    },
    "s3": {
        "Standard": 0.023, "Standard-IA": 0.0125,
        "Glacier": 0.004, "Deep Archive": 0.00099
    },
    "ebs": {"gp3": 0.08, "gp2": 0.10},  # per GB/month
    "elastic_ip": 0.005  # per hour when not attached
}

recommendations = []
potential_savings = 0

print("\n🔍 ANALYZING RESOURCES...\n")

# EC2 Analysis
print("=" * 70)
print("💻 EC2 INSTANCES")
print("=" * 70)

for instance in resources["ec2_instances"]:
    instance_cost = pricing["ec2"][instance["type"]] * 730  # monthly cost
    print(f"\n📊 {instance['id']} ({instance['type']}) - {instance['pricing']}")
    print(f"   Average CPU: {instance['cpu_avg']}%")
    print(f"   Monthly cost: ${instance_cost:.2f}")

    # Right-sizing recommendation
    if instance["cpu_avg"] < 25 and instance["type"] not in ["t3.micro", "t3.small"]:
        recommendations.append({
            "type": "Right-Size",
            "resource": instance["id"],
            "action": f"Downsize from {instance['type']} to t3.medium",
            "reason": f"CPU only {instance['cpu_avg']}% (underutilized)",
            "savings": instance_cost - (pricing["ec2"]["t3.medium"] * 730)
        })
        potential_savings += instance_cost - \
            (pricing["ec2"]["t3.medium"] * 730)
        print(f"   ⚠️  UNDERUTILIZED - Consider downsizing")

    # Pricing model recommendation
    if instance["pricing"] == "On-Demand" and instance["hours_per_day"] == 24:
        reserved_cost = instance_cost * 0.4  # 60% savings with Reserved
        recommendations.append({
            "type": "Reserved Instance",
            "resource": instance["id"],
            "action": "Switch to Reserved Instance (1-year)",
            "reason": "Runs 24/7, predictable workload",
            "savings": instance_cost - reserved_cost
        })
        potential_savings += instance_cost - reserved_cost
        print(
            f"   💰 OPPORTUNITY: Reserved Instance could save ${instance_cost - reserved_cost:.2f}/month")

# S3 Analysis
print("\n" + "=" * 70)
print("🗄️  S3 STORAGE")
print("=" * 70)

for bucket in resources["s3_buckets"]:
    bucket_cost = bucket["size_gb"] * pricing["s3"][bucket["storage_class"]]
    print(f"\n📦 {bucket['name']}")
    print(f"   Size: {bucket['size_gb']} GB")
    print(f"   Storage class: {bucket['storage_class']}")
    print(f"   Access: {bucket['access_frequency']}")
    print(f"   Monthly cost: ${bucket_cost:.2f}")

    # Storage class optimization
    if bucket["access_frequency"] == "yearly" and bucket["storage_class"] == "Standard":
        glacier_cost = bucket["size_gb"] * pricing["s3"]["Glacier"]
        recommendations.append({
            "type": "S3 Lifecycle",
            "resource": bucket["name"],
            "action": "Move to S3 Glacier",
            "reason": "Accessed yearly, paying for Standard",
            "savings": bucket_cost - glacier_cost
        })
        potential_savings += bucket_cost - glacier_cost
        print(
            f"   ⚠️  Move to Glacier: save ${bucket_cost - glacier_cost:.2f}/month")

# EBS Analysis
print("\n" + "=" * 70)
print("💾 EBS VOLUMES")
print("=" * 70)

for volume in resources["ebs_volumes"]:
    volume_cost = volume["size_gb"] * pricing["ebs"][volume["type"]]
    print(f"\n🔹 {volume['id']} ({volume['size_gb']} GB, {volume['type']})")
    print(f"   Attached: {volume['attached']}")
    print(f"   Monthly cost: ${volume_cost:.2f}")

    if not volume["attached"]:
        recommendations.append({
            "type": "Delete Unused",
            "resource": volume["id"],
            "action": "Delete unattached volume",
            "reason": "Not attached to any instance (waste)",
            "savings": volume_cost
        })
        potential_savings += volume_cost
        print(f"   ❌ UNUSED - Delete to save ${volume_cost:.2f}/month")

# Elastic IP Analysis
print("\n" + "=" * 70)
print("🌐 ELASTIC IPs")
print("=" * 70)

for eip in resources["elastic_ips"]:
    if not eip["attached"]:
        eip_cost = pricing["elastic_ip"] * 730
        print(f"\n📍 {eip['ip']}")
        print(f"   Attached: {eip['attached']}")
        print(f"   Monthly cost: ${eip_cost:.2f}")

        recommendations.append({
            "type": "Delete Unused",
            "resource": eip["ip"],
            "action": "Release unattached Elastic IP",
            "reason": "Unattached IPs incur charges",
            "savings": eip_cost
        })
        potential_savings += eip_cost
        print(f"   ❌ UNUSED - Release to save ${eip_cost:.2f}/month")

# Summary
print("\n" + "=" * 70)
print("💡 COST OPTIMIZATION RECOMMENDATIONS")
print("=" * 70)

if recommendations:
    print(f"\n🎯 Found {len(recommendations)} opportunities to save money:\n")

    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. [{rec['type']}] {rec['resource']}")
        print(f"   Action: {rec['action']}")
        print(f"   Reason: {rec['reason']}")
        print(f"   💰 Potential savings: ${rec['savings']:.2f}/month\n")

    print("=" * 70)
    print(f"💵 TOTAL POTENTIAL SAVINGS: ${potential_savings:.2f}/month")
    print(f"💵 ANNUAL SAVINGS: ${potential_savings * 12:.2f}/year")
    print("=" * 70)
else:
    print("\n✅ No optimization opportunities found - resources are well-optimized!")

print("\n📚 COST OPTIMIZATION BEST PRACTICES:")
print("   • Review CloudWatch metrics weekly to identify underutilized resources")
print("   • Use Reserved Instances for predictable 24/7 workloads")
print("   • Enable S3 Lifecycle policies to auto-archive old data")
print("   • Delete unattached EBS volumes and unused Elastic IPs")
print("   • Use AWS Cost Explorer to track spending trends")
print("   • Set up billing alarms to avoid surprise costs")
print("=" * 70)
