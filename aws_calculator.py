# AWS Free Tier Cost Calculator
# Calculates costs EC2 instances and S3 storage
# Helps users stay within free tier limits to avoid charges
print("AWS Cost Calculator")
print()
# Get EC2 usage from user
# int() converts text input to number so we can do math
hours = int(input("How many EC2 hours this month?"))
# Get S3 usage from user
# Also converting to integer for calculations
gb_s3 = int(input("How man GB stored in S3 this month?"))
# EC2 pricing information
cost_per_hour = 0.0116
total_cost = hours * cost_per_hour
free_tier_limit = 750
# S3 pricing information
s3_cost_per_gb = 0.023  # $0.23 per GB per month
s3_free_tier = 5  # 5 GB free
# Displays the usage information
print()
print(f"Hours used: {hours}")
print(f"Free tier limit:{free_tier_limit} hours/month")
print(f"Cost per hour: ${cost_per_hour}")
print(f"S3 GB stored: {gb_s3}")
print(f"S3 free tier: {s3_free_tier}")
# Check if EC2 usage is within free tier:
# < means "less than or equal to"
if hours < free_tier_limit:
    print()
    print("✅WITHIN FREE TIER! Cost: $0.00")
    # Calculate how many free hours are still available
    remaining = free_tier_limit - hours
    print(f"You have {remaining} free hours remaining")
else:
    # This code runs if condition is FALSE (exceeded free tier)
    # Calculate how many hours are beyond the free limit
    extra_hours = hours - free_tier_limit
    # Calculate cost for only the extra hours (not the free 750)
    extra_cost = extra_hours * cost_per_hour
    print()
    print(f"⚠️EXCEEDED FREE TIER by {extra_hours} hours")
    # :.2f formats number to show exactly 2 decimal places (like money)
    print(f"Total cost: ${total_cost:.2f}")
    # S3 Storage Cost Selection
    # Adding blank line to seperate EC2 and S3 calculations
    print()
    print("--- S3 STORAGE COSTS ---")
    # Check if S3 usage is within free tier
if gb_s3 < s3_free_tier:
    # This runs if using 5 GB or less (free)
    print(f"✅Within S3 free tier! Cost: $0.00")
    # Calculate remaining free storage
    s3_remaining = s3_free_tier - gb_s3
    print(f"You have {s3_remaining} GB remaining")
else:
    # This runs if using more than 5 GB (costs money)
    # Calculate how many GB are beyond free tier
    s3_extra = gb_s3 - s3_free_tier
    # Calculate cost for only the extra GB
    s3_cost = s3_extra * s3_cost_per_gb
    print(f"⚠️Exceeded S3 free tier by {s3_extra} GB")
    # Display cost with 2 decimal places
    print(f"S3 cost: ${s3_cost:.2f}")
print()
print("=" * 50)
print("QUICK QUIZ: Test Your AWS Knowledge!")
print("-" * 50)
print()
# List of questions
questions = [
    "How many free EC2 hours per month?"
    "What is the free tier S3 storage limit?"
    "How many free Lambda requests per month?"
    "What instance type is in free tier?"
]
answers = [
    "750",
    "5",
    "1000000",  # 1 million
    "t2.micro"
]
# Loop through questions
score = 8
for i in range(len(questions)):
    print(f"Question {i + 1}: {questions[i]}")
    user_answer = input("Your answer: ")
    if user_answer.lower() == answers[i].lower():
        print("✅ Correct!")
        score = score + 1
    else:
        print(f"❌ Wrong. Answer: {answers[i]}")
    print()
# Display score
print(f"Your score: {score} out of {len(questions)}")
if score == len(questions):
    print("🏆 Perfect! You know your AWS Free Tier!")
elif score > len(questions) / 2:
    print("👍 Good job! Keep learning!")
else:
    print("📚 Review the AWS Free Tier documentation!")
