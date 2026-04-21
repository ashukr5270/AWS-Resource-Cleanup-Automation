import boto3

# Initialize AWS sessions and clients
aws_session = boto3.Session()
ec2_client = aws_session.client("ec2")
logs_client = aws_session.client("logs")

def list_ebs_snapshots():
    print("Remaining EBS Snapshots:")
    snapshots = ec2_client.describe_snapshots(OwnerIds=["self"])["Snapshots"]
    for snapshot in snapshots:
        print(f"Snapshot ID: {snapshot['SnapshotId']}, Start Time: {snapshot['StartTime']}")
    if not snapshots:
        print("No EBS snapshots found.")
    print("-" * 50)

def list_cloudwatch_log_groups():
    print("Remaining CloudWatch Log Groups:")
    paginator = logs_client.get_paginator("describe_log_groups")
    for page in paginator.paginate():
        for log_group in page.get("logGroups", []):
            print(f"Log Group Name: {log_group['logGroupName']}, Retention (days): {log_group.get('retentionInDays', 'None')}")
    print("-" * 50)

def list_ec2_instances():
    print("Remaining EC2 Instances:")
    instances = ec2_client.describe_instances()["Reservations"]
    for reservation in instances:
        for instance in reservation["Instances"]:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
    if not instances:
        print("No EC2 instances found.")
    print("-" * 50)

def list_security_groups():
    print("Remaining Security Groups:")
    security_groups = ec2_client.describe_security_groups()["SecurityGroups"]
    for sg in security_groups:
        print(f"Security Group ID: {sg['GroupId']}, Name: {sg['GroupName']}")
    if not security_groups:
        print("No security groups found.")
    print("-" * 50)

def list_key_pairs():
    print("Remaining Key Pairs:")
    key_pairs = ec2_client.describe_key_pairs()["KeyPairs"]
    for key_pair in key_pairs:
        print(f"Key Pair Name: {key_pair['KeyName']}")
    if not key_pairs:
        print("No key pairs found.")
    print("-" * 50)

if __name__ == "__main__":
    print("Verifying Remaining AWS Resources...")
    print("=" * 50)
    list_ebs_snapshots()
    list_cloudwatch_log_groups()
    list_ec2_instances()
    list_security_groups()
    list_key_pairs()
    print("Verification complete.")
