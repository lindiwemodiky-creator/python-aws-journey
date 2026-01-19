# AWS Free Tier Cost Calculator
print("AWS Cost Calculator")
print()
hours = int(input("How many EC2 hours this month?"))
cost_per_hour = 0.0116
total_cost = hours * cost_per_hour
free_tier_limit = 750
print()
print(f"Hours used: {hours}")
print(f"Free tier limit:{free_tier_limit} hours/month")
print(f"Cost per hour: ${cost_per_hour}")
if hours < free_tier_limit:
    print()
    print("✅WITHIN FREE TIER! Cost: $0.00")
    remaining = free_tier_limit - hours
    print(f"You have {remaining} free hours remaining")
else:
    extra_hours = hours - free_tier_limit
    extra_cost = extra_hours * cost_per_hour
    print()
    print(f"⚠️EXCEEDED FREE TIER by {extra_hours} hours")
    print(f"Total cost: ${total_cost:.2f}")
