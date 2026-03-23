import random
import time

print("=" * 70)
print("CLOUDWATCH ALARM SIMULATOR")
print("=" * 70)

# Alarm configuration
ALARM_NAME = "HighCPUAlarm"
METRIC_NAME = "CPUUtilization"
THRESHOLD = 80  # Percent
EVALUATION_PERIODS = 2  # Must exceed threshold for 2 periods to trigger

print(f"\n⚙️  Alarm Configuration:")
print(f"   Name: {ALARM_NAME}")
print(f"   Metric: {METRIC_NAME}")
print(f"   Threshold: {THRESHOLD}%")
print(f"   Evaluation Periods: {EVALUATION_PERIODS}")
print(f"   Action: Send notification + trigger Auto Scaling\n")

# Alarm state
alarm_state = "OK"
periods_above_threshold = 0

# Simulate 12 monitoring periods (like 12 minutes)
for period in range(1, 13):
    print("=" * 70)
    print(f"⏱️  Period {period}")
    print("=" * 70)

    # Simulate CPU usage (random realistic values)
    if 4 <= period <= 8:
        # Simulate traffic spike (high CPU)
        cpu_usage = random.randint(75, 95)
    else:
        # Normal traffic
        cpu_usage = random.randint(30, 65)

    print(f"📊 Current {METRIC_NAME}: {cpu_usage}%")
    print(f"🎯 Alarm Threshold: {THRESHOLD}%")

    # Check if threshold exceeded
    if cpu_usage > THRESHOLD:
        periods_above_threshold += 1
        print(
            f"⚠️  THRESHOLD EXCEEDED ({periods_above_threshold}/{EVALUATION_PERIODS} periods)")

        # Trigger alarm after consecutive periods
        if periods_above_threshold >= EVALUATION_PERIODS:
            if alarm_state != "ALARM":
                alarm_state = "ALARM"
                print(f"\n🚨 ALARM TRIGGERED: {ALARM_NAME}")
                print(f"   📧 Sending notification to admin@company.com")
                print(f"   🔼 Triggering Auto Scaling to add instances")
                print(f"   📱 SNS notification sent to operations team\n")
            else:
                print(f"🔴 Alarm State: {alarm_state} (still active)")
        else:
            print(
                f"🟡 Alarm State: {alarm_state} (monitoring, not triggered yet)")

    else:
        # CPU back to normal
        if periods_above_threshold > 0:
            print(f"✅ CPU returned to normal")

        periods_above_threshold = 0

        if alarm_state == "ALARM":
            alarm_state = "OK"
            print(f"\n✅ ALARM RESOLVED: {ALARM_NAME}")
            print(f"   📧 Sending recovery notification")
            print(f"   🔽 Auto Scaling may scale down if traffic remains low\n")
        else:
            print(f"✅ Alarm State: {alarm_state}")

    print(f"📈 Current Alarm State: {alarm_state}")
    time.sleep(0.5)  # Pause for readability

print("\n" + "=" * 70)
print("🏁 SIMULATION COMPLETE")
print("=" * 70)
print(f"\n📊 Summary:")
print(f"   Alarm Name: {ALARM_NAME}")
print(f"   Final State: {alarm_state}")
print(f"   Threshold: {THRESHOLD}%")
print(f"\n💡 CloudWatch alarms help you detect issues before customers notice!")
print("=" * 70)
