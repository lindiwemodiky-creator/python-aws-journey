import json
import os

print("=" * 60)
print("IAM POLICY VALIDATOR")
print("=" * 60)

# Ask for policy file
policy_file = input(
    "\nEnter policy filename (or press Enter for 'lambda_s3_policy.json'): ") or "lambda_s3_policy.json"

# Check if file exists
if not os.path.exists(policy_file):
    print(f"\n❌ Error: File '{policy_file}' not found!")
    exit()

# Try to load and validate the JSON
try:
    with open(policy_file, 'r') as f:
        policy = json.load(f)

    print(f"\n✅ Valid JSON structure")

    # Check required fields
    errors = []
    warnings = []

    # Must have Version
    if 'Version' not in policy:
        errors.append("Missing required field: 'Version'")
    elif policy['Version'] != '2012-10-17':
        warnings.append(
            f"Version is '{policy['Version']}' - recommended: '2012-10-17'")

    # Must have Statement
    if 'Statement' not in policy:
        errors.append("Missing required field: 'Statement'")
    elif not isinstance(policy['Statement'], list):
        errors.append("'Statement' must be a list")
    else:
        # Validate each statement
        for i, statement in enumerate(policy['Statement']):
            # Must have Effect
            if 'Effect' not in statement:
                errors.append(f"Statement {i}: Missing 'Effect'")
            elif statement['Effect'] not in ['Allow', 'Deny']:
                errors.append(
                    f"Statement {i}: Effect must be 'Allow' or 'Deny', got '{statement['Effect']}'")

            # Must have Action or NotAction
            if 'Action' not in statement and 'NotAction' not in statement:
                errors.append(
                    f"Statement {i}: Missing 'Action' or 'NotAction'")

            # Must have Resource or NotResource (unless Principal is present)
            if 'Resource' not in statement and 'NotResource' not in statement:
                if 'Principal' not in statement:
                    warnings.append(
                        f"Statement {i}: No 'Resource' field - may be invalid for identity-based policies")

    # Display results
    print("\n" + "=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)

    if errors:
        print("\n❌ ERRORS FOUND:")
        for error in errors:
            print(f"   • {error}")

    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"   • {warning}")

    if not errors and not warnings:
        print("\n✅ Policy is valid!")
        print(f"   Version: {policy.get('Version')}")
        print(f"   Statements: {len(policy.get('Statement', []))}")
    elif not errors:
        print("\n✅ No critical errors (warnings can be ignored)")
    else:
        print(
            f"\n❌ Found {len(errors)} error(s) - policy will NOT work in AWS")

    print("=" * 60)

except json.JSONDecodeError as e:
    print(f"\n❌ Invalid JSON format!")
    print(f"   Error: {e}")
    print(f"\n💡 Tip: Check for missing commas, brackets, or quotes")
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")
