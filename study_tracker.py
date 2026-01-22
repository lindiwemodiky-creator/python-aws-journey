# Study Tracker - AWS Certification Journey
# Tracks study progress and motivates user
print("AWS STUDY TRACKER")
print()
# Get user's study goal
total_days = int(input("How many days until your exam?"))
days_studied = int(input("How man days have you studied so far?"))
# Calculate remaining days
days_remaining = total_days - days_studied
# Calculate progress percentage
progress_percent = (days_studied / total_days) * 100
# Display summary
print()
print("---YOUR PROGRESS---")
print(f"Total study period: {total_days} days")
print(f"Days completed: {days_studied}")
print(f"Days remaining: {days_remaining}")
print(f"Progress: {progress_percent:.1f}%")
print()
print("---DAYS COMPLETED---")
# Loop through completed days
for day in range(1, days_studied + 1):
    print(f"✅Day {day}")
print()
print("--- UPCOMING DAYS ---")
# Loop through remaining days
for day in range(days_studied + 1, total_days + 1):
    if day < days_studied + 5:  # Show next 5 days only
        print(f"⏳ Day {day}")
print()
# Motivational message based on progress
if progress_percent < 25:
    print("🌱 Just starting! Every day counts. Keep going!")
elif progress_percent < 50:
    print("🔥 Building momentum! You're doing great!")
elif progress_percent < 75:
    print("💪 Over halfway there! Don't stop now!")
else:
    print("🚀 Final stretch! You've got this!")
