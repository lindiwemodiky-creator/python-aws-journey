import random
import time

print("=" * 60)
print("AUTO SCALING SIMULATOR")
print("=" * 60)

# Configuration
MIN_INSTANCES = 2
MAX_INSTANCES = 10
SCALE_UP_THRESHOLD = 70  # CPU %
SCALE_DOWN_THRESHOLD = 30  # CPU %

# Current state
current_instances = MIN_INSTANCES
current_cpu = 20  # Start low

print(f"\n⚙️  Auto Scaling Configuration:")
print(f"   Min instances: {MIN_INSTANCES}")
print(f"   Max instances: {MAX_INSTANCES}")
print(f"   Scale up threshold: {SCALE_UP_THRESHOLD}% CPU")
print(f"   Scale down threshold: {SCALE_DOWN_THRESHOLD}% CPU")
print(f"\n🚀 Starting with {current_instances} instances\n")

# Simulate 10 time periods
for period in range(1, 11):
    print("=" * 60)
    print(f"⏱️  Period {period}")
    print("=" * 60)

    # Simulate random CPU usage (traffic patterns)
    # Periods 3-6 simulate traffic spike
    if 3 <= period <= 6:
        current_cpu = random.randint(60, 95)  # High traffic
    else:
        current_cpu = random.randint(15, 45)  # Normal traffic

    print(f"📊 Current CPU usage: {current_cpu}%")
    print(f"💻 Current instances: {current_instances}")

    # Scaling logic
    if current_cpu > SCALE_UP_THRESHOLD and current_instances < MAX_INSTANCES:
        instances_to_add = 2
        if current_instances + instances_to_add > MAX_INSTANCES:
            instances_to_add = MAX_INSTANCES - current_instances

        current_instances += instances_to_add
        print(f"🔼 SCALING UP: Adding {instances_to_add} instance(s)")
        print(
            f"   Reason: CPU ({current_cpu}%) > threshold ({SCALE_UP_THRESHOLD}%)")

    elif current_cpu < SCALE_DOWN_THRESHOLD and current_instances > MIN_INSTANCES:
        instances_to_remove = 1
        if current_instances - instances_to_remove < MIN_INSTANCES:
            instances_to_remove = current_instances - MIN_INSTANCES

        current_instances -= instances_to_remove
        print(f"🔽 SCALING DOWN: Removing {instances_to_remove} instance(s)")
        print(
            f"   Reason: CPU ({current_cpu}%) < threshold ({SCALE_DOWN_THRESHOLD}%)")

    else:
        print(f"✅ NO SCALING: CPU within normal range")

    print(f"💻 New instance count: {current_instances}")
    time.sleep(1)  # Pause for readability

print("\n" + "=" * 60)
print("🏁 SIMULATION COMPLETE")
print("=" * 60)
print(f"\n📈 Summary:")
print(f"   Started with: {MIN_INSTANCES} instances")
print(
    f"   Peak instances: {MAX_INSTANCES if period >= 3 else current_instances}")
print(f"   Final instances: {current_instances}")
print(f"\n💰 Cost savings: Auto Scaling only runs instances when needed!")
print("=" * 60)
