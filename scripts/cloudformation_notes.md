# CloudFormation Quick Reference

## Key Concepts

**Template**: JSON or YAML file defining infrastructure  
**Stack**: Collection of AWS resources created from template  
**Parameters**: User inputs (like instance type, environment)  
**Resources**: AWS resources to create (EC2, S3, RDS, etc.)  
**Outputs**: Values returned after stack creation (IDs, URLs, ARNs)  

## Common Intrinsic Functions

- `!Ref` - Reference a resource or parameter  
- `!GetAtt` - Get attribute of a resource (e.g., PublicIp, Arn)  
- `!Sub` - Substitute variables in strings  
- `!Join` - Join strings with delimiter  

## Benefits of CloudFormation

1. **Repeatable**: Same template creates identical environments  
2. **Version Control**: Track changes in Git  
3. **Rollback**: Auto-rollback on failure  
4. **Delete Everything**: One command deletes entire stack  
5. **Cost Tracking**: Resources tagged by stack  

## When to Use CloudFormation

✅ Creating dev/test/prod environments (identical setup)  
✅ Disaster recovery (rebuild infrastructure fast)  
✅ Compliance (ensure resources meet standards)  
✅ Multi-region deployment (same template, different Regions)  

## Exam Tips

- CloudFormation is FREE (you only pay for resources it creates)  
- Templates can be stored in S3 and versioned  
- If stack creation fails, CloudFormation auto-deletes everything (rollback)  
- Drift detection = check if resources were manually changed outside CloudFormation  