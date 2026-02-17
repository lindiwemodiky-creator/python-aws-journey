# Week 2: EC2 Fundamentals
**Date:** February 4, 2026  
**Focus:** Virtual servers (compute)

## What I Learned
**EC2 is a:** virtual machine that you rent from cloud service providers**
**The reason EC2 matters is because** you get to do your work flexibly without worrying about maintaining the servers. You save the unnecessary costs**

## Key Concepts
**Instance Types:** Different kinds of virtual machines  
**Instance States:**
- **Running:** Means the instances are working
- **Stopped:** The instances are paused or rather they are still on and can work
- **Terminated:** The instances are removed forever

**Stop vs Terminate:** Stop can be seen as someone who still hopes you take them back, so they linger and are there. But Terminate understands that the relationship is over, no take backs. They understand their worth.

## Commands I Used
```bash
awslocal ec2 run-instances --image-id ami-ff0fea8310f3 --instance-type t2.micro --count 1
**Does:** Creates (rents) 1 small robot from factory

### List Instances
awslocal ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId,State.Name]" --output table
```bash
---------------------------------------
|          DescribeInstances          |
+----------------------+--------------+
|  i-b629fbaeea425c636 |  terminated  |
|  i-9017e70c97eaea8d7 |  terminated  |
|  i-a145411d387b21cad |  terminated  |
|  i-dbfc4bfdcddef847e |  terminated  |
|  i-27523f24e591ed66b |  running     |
|  i-820dd6056fd941e4d |  stopped     |
|  i-4f12f325c1bddc6b4 |  running     |
+----------------------+--------------+

## **Finish These 3 Sections** (2 minutes):

```markdown
### Python Tools I Built
1. **ec2_list_instances.py** - Pretty robot list with 🟢🔴🟡 colors
2. **ec2_launcher.py** - Asks "how many?" → launches robots  
3. **ec2_manager.py** - Control panel (list/stop/start/terminate/exit)

## What Worked Well
- Toy factory idea made EC2 click
- Built REAL engineer tools on Day 1

## Things to Remember
- Stop = sleep 😴, Terminate = trash 🗑️
- `run-instances` = create new robots
## Things to Remember
- Stop = sleep 😴 (cheap storage), Terminate = trash 🗑️ (gone forever)
- My robot army IDs: i-27523f24e591ed66b, i-4f12f325c1bddc6b4, i-820dd6056fd941e4d
- Python tools > CLI commands (automation wins)

## Next Steps
**Tomorrow:** Databases (RDS) - store robot instructions
**Practice:** Run ec2_manager.py anytime
