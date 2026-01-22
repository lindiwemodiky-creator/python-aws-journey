# Countdown to SAA Exam
# This program calculates and displays time remaining until the AWS certification exam
# Shows countdown in multiple time units: months, weeks, days, hours, minutes and seconds
print("Countdown to success")
print()
# Store exam date as text (Not used in calculations, just display)
exam_date = "May 15, 2026"
# Main calculation: days remaining from today (Jan 21) to exam day (May 15)
days_remaining = 113  # Update for January 21, 2026
# Calculate weeks remaining
# Using // (floor division) to get whole weeks only, ignoring leftover days
week_remaining = days_remaining // 7
# Calculate approximate months remaining
# Using again // because partial months don't make sense in countdown
# 30 is approximate (months vary in length)
months_remaining = days_remaining // 30
# Multiply by 24 because 1 day = 24 hours
hours_remaining = days_remaining * 24
# Multiply hours by 60 because 1 hour = 60 minutes
minutes_remaining = hours_remaining
seconds_remaining = minutes_remaining * 60  # New: Total seconds
# Displays all time units in a clear format
# Using f-strings to insert variable values into text
print(f"Exam date: {exam_date}")
print(f"Days remaining: {days_remaining}")
print(f"Weeks remaining: {week_remaining}")
print(f"Months remaining: (approx): {months_remaining}")
print(f"Hours remaining: {hours_remaining}")
print(f"Minutes remaining: {minutes_remaining}")
print(f"Seconds remaining:{seconds_remaining}")
# Add blank line for spacing
print()
# Motivational messages to keep user focused
print("Every single day counts!")
print("Today is Day 2. Let's go!")
print()
print("--- MILESTONE COUNTDOWN ---")
print("Major milestones ahead:")
print("Major milestones ahead:")
# Create list of milestones
milestones = [
    ("AWS Account Creation", 5),  # Jan 27 (5 days from Jan 21)
    ("First EC2 Deploy", 12),
    ("VPC Project Complete", 19),
    ("Month 1 Complete", 30),
    ("Halfway Point", 57),
    ("Final Month Begins", 83),
    ("Exam Week", 110)
]
# Loop through milestones
for milestone_name, days_until in milestones:
    if days_until < days_remaining:
        days_to_milestone = days_until
        print(f" 🎯 {milestone_name}: {days_to_milestone} days")
