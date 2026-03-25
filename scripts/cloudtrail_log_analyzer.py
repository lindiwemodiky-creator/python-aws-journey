import json
from datetime import datetime

print("=" * 70)
print("CLOUDTRAIL LOG ANALYZER")
print("=" * 70)

# Simulated CloudTrail log entries (in real AWS, these come from S3)
cloudtrail_logs = [
    {
        "eventTime": "2026-03-24T09:15:23Z",
        "eventName": "CreateBucket",
        "userIdentity": {"userName": "alice"},
        "sourceIPAddress": "203.0.113.45",
        "requestParameters": {"bucketName": "production-backups"},
        "responseElements": None,
        "errorCode": None
    },
    {
        "eventTime": "2026-03-24T02:47:12Z",
        "eventName": "TerminateInstances",
        "userIdentity": {"userName": "bob"},
        "sourceIPAddress": "198.51.100.22",
        "requestParameters": {"instancesSet": {"items": [{"instanceId": "i-1234567890abcdef0"}]}},
        "responseElements": None,
        "errorCode": None
    },
    {
        "eventTime": "2026-03-24T03:22:55Z",
        "eventName": "DeleteUser",
        "userIdentity": {"userName": "unknown"},
        "sourceIPAddress": "192.0.2.100",
        "requestParameters": {"userName": "admin"},
        "responseElements": None,
        "errorCode": "AccessDenied"
    },
    {
        "eventTime": "2026-03-24T14:30:10Z",
        "eventName": "PutBucketPolicy",
        "userIdentity": {"userName": "alice"},
        "sourceIPAddress": "203.0.113.45",
        "requestParameters": {"bucketName": "production-backups"},
        "responseElements": None,
        "errorCode": None
    },
    {
        "eventTime": "2026-03-24T03:23:01Z",
        "eventName": "DeleteBucket",
        "userIdentity": {"userName": "unknown"},
        "sourceIPAddress": "192.0.2.100",
        "requestParameters": {"bucketName": "customer-data"},
        "responseElements": None,
        "errorCode": "AccessDenied"
    },
    {
        "eventTime": "2026-03-24T15:45:33Z",
        "eventName": "RunInstances",
        "userIdentity": {"userName": "charlie"},
        "sourceIPAddress": "198.51.100.99",
        "requestParameters": {"instanceType": "m5.xlarge", "minCount": 10},
        "responseElements": None,
        "errorCode": None
    }
]

print(f"\n📋 Analyzing {len(cloudtrail_logs)} CloudTrail events...\n")

# Analysis categories
failed_events = []
suspicious_ips = {}
delete_operations = []
high_risk_actions = []
unusual_times = []

for event in cloudtrail_logs:
    user = event["userIdentity"]["userName"]
    action = event["eventName"]
    ip = event["sourceIPAddress"]
    time = event["eventTime"]
    error = event["errorCode"]

    # Track failed events
    if error:
        failed_events.append({
            "user": user,
            "action": action,
            "error": error,
            "time": time,
            "ip": ip
        })

    # Track IPs with multiple actions
    if ip not in suspicious_ips:
        suspicious_ips[ip] = []
    suspicious_ips[ip].append(action)

    # Track delete operations
    if "Delete" in action or "Terminate" in action:
        delete_operations.append({
            "user": user,
            "action": action,
            "time": time
        })

    # Track high-risk actions
    high_risk = ["DeleteUser", "DeleteBucket",
                 "PutBucketPolicy", "CreateAccessKey"]
    if action in high_risk:
        high_risk_actions.append({
            "user": user,
            "action": action,
            "time": time
        })

    # Track unusual hours (2am-5am)
    hour = int(time.split("T")[1].split(":")[0])
    if 2 <= hour <= 5:
        unusual_times.append({
            "user": user,
            "action": action,
            "time": time
        })

# Print analysis
print("=" * 70)
print("🔍 SECURITY ANALYSIS")
print("=" * 70)

if failed_events:
    print(f"\n⚠️  FAILED EVENTS ({len(failed_events)} found):")
    for event in failed_events:
        print(
            f"   🚨 {event['user']} tried {event['action']} from {event['ip']}")
        print(f"      Error: {event['error']} at {event['time']}")
else:
    print("\n✅ No failed events detected")

if unusual_times:
    print(f"\n🌙 UNUSUAL HOURS ACTIVITY ({len(unusual_times)} found):")
    for event in unusual_times:
        print(
            f"   ⏰ {event['user']} performed {event['action']} at {event['time']}")
else:
    print("\n✅ No unusual hours activity")

if delete_operations:
    print(f"\n🗑️  DELETE OPERATIONS ({len(delete_operations)} found):")
    for event in delete_operations:
        print(
            f"   ❌ {event['user']} performed {event['action']} at {event['time']}")
else:
    print("\n✅ No delete operations")

if high_risk_actions:
    print(f"\n⚡ HIGH-RISK ACTIONS ({len(high_risk_actions)} found):")
    for event in high_risk_actions:
        print(
            f"   🔴 {event['user']} performed {event['action']} at {event['time']}")
else:
    print("\n✅ No high-risk actions")

# IP analysis
suspicious_ip_count = {
    ip: len(actions) for ip, actions in suspicious_ips.items() if len(actions) >= 2}
if suspicious_ip_count:
    print(f"\n🌐 ACTIVE IP ADDRESSES:")
    for ip, count in sorted(suspicious_ip_count.items(), key=lambda x: x[1], reverse=True):
        print(f"   📍 {ip}: {count} actions")

print("\n" + "=" * 70)
print("💡 RECOMMENDATIONS")
print("=" * 70)

if failed_events:
    print("   • Investigate failed access attempts (possible intrusion)")
if unusual_times:
    print("   • Review activity during unusual hours (2am-5am)")
if delete_operations:
    print("   • Verify delete operations were authorized")
print("   • Enable MFA for all IAM users")
print("   • Set up CloudWatch alarms for suspicious CloudTrail events")

print("\n" + "=" * 70)
