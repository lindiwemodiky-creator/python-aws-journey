print("=" * 60)
print("AWS COST ESTIMATOR")
print("=" * 60)

# EC2 pricing (simplified - actual prices vary by region)
EC2_PRICES = {
    "t2.micro": 0.0116,    # per hour
    "t2.small": 0.023,
    "t2.medium": 0.0464,
    "m5.large": 0.096,
    "m5.xlarge": 0.192
}

# S3 pricing (per GB per month)
S3_PRICE_PER_GB = 0.023

# RDS pricing (per hour)
RDS_PRICES = {
    "db.t2.micro": 0.017,
    "db.t2.small": 0.034,
    "db.m5.large": 0.17
}

# Lambda pricing (per million requests)
LAMBDA_PRICE_PER_MILLION = 0.20

print("\n📋 What resources do you want to estimate?\n")

# EC2 Instances
ec2_type = input(
    "EC2 instance type (t2.micro/t2.small/t2.medium/m5.large/m5.xlarge) or press Enter to skip: ")
ec2_count = 0
ec2_cost = 0

if ec2_type:
    ec2_count = int(input(f"How many {ec2_type} instances? "))
    hours_per_month = 730  # Average hours in a month
    ec2_cost = EC2_PRICES.get(ec2_type, 0) * ec2_count * hours_per_month

# S3 Storage
s3_gb = input("S3 storage (GB per month) or press Enter to skip: ")
s3_cost = 0

if s3_gb:
    s3_gb = float(s3_gb)
    s3_cost = s3_gb * S3_PRICE_PER_GB

# RDS Database
rds_type = input(
    "RDS instance type (db.t2.micro/db.t2.small/db.m5.large) or press Enter to skip: ")
rds_cost = 0

if rds_type:
    hours_per_month = 730
    rds_cost = RDS_PRICES.get(rds_type, 0) * hours_per_month

# Lambda
lambda_requests = input(
    "Lambda requests per month (in millions) or press Enter to skip: ")
lambda_cost = 0

if lambda_requests:
    lambda_requests = float(lambda_requests)
    lambda_cost = lambda_requests * LAMBDA_PRICE_PER_MILLION

# Calculate total
total_cost = ec2_cost + s3_cost + rds_cost + lambda_cost

# Display results
print("\n" + "=" * 60)
print("💰 ESTIMATED MONTHLY COST")
print("=" * 60)

if ec2_cost > 0:
    print(f"EC2 ({ec2_count}x {ec2_type}): ${ec2_cost:.2f}")
if s3_cost > 0:
    print(f"S3 Storage ({s3_gb} GB): ${s3_cost:.2f}")
if rds_cost > 0:
    print(f"RDS ({rds_type}): ${rds_cost:.2f}")
if lambda_cost > 0:
    print(f"Lambda ({lambda_requests}M requests): ${lambda_cost:.2f}")

print("=" * 60)
print(f"TOTAL ESTIMATED COST: ${total_cost:.2f} / month")
print("=" * 60)
print("\n💡 Tip: These are simplified estimates. Actual costs vary by region and usage patterns.")
