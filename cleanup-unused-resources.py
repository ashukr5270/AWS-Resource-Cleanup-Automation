import boto3
import datetime
from dateutil import tz

# Initialize AWS clients
ec2_client = boto3.client("ec2")
cloudwatch_logs_client = boto3.client("logs")
iam_client = boto3.client("iam")

def delete_old_ebs_snapshots():
    print("Checking for old EBS snapshots...")
    three_months_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=90)
    snapshots = ec2_client.describe_snapshots(OwnerIds=["self"])['Snapshots']

    for snapshot in snapshots:
        if snapshot['StartTime'] < three_months_ago:
            print(f"Deleting snapshot: {snapshot['SnapshotId']} created on {snapshot['StartTime']}")
            ec2_client.delete_snapshot(SnapshotId=snapshot['SnapshotId'])

def delete_old_cloudwatch_log_groups():
    print("Checking for old CloudWatch log groups...")
    three_years_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3 * 365)
    paginator = cloudwatch_logs_client.get_paginator("describe_log_groups")

    for page in paginator.paginate():
        for log_group in page.get("logGroups", []):
            last_ingestion_time = log_group.get("lastIngestionTime")
            if last_ingestion_time:
                last_ingestion_date = datetime.datetime.fromtimestamp(last_ingestion_time / 1000, tz=tz.UTC)
                if last_ingestion_date < three_years_ago:
                    print(f"Deleting log group: {log_group['logGroupName']} last used on {last_ingestion_date}")
                    cloudwatch_logs_client.delete_log_group(logGroupName=log_group['logGroupName'])

def delete_old_ec2_instances():
    print("Checking for old EC2 instances...")
    three_years_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3 * 365)
    instances = ec2_client.describe_instances(Filters=[{"Name": "instance-state-name", "Values": ["stopped"]}])['Reservations']

    for reservation in instances:
        for instance in reservation['Instances']:
            launch_time = instance['LaunchTime']
            if launch_time < three_years_ago:
                instance_id = instance['InstanceId']
                print(f"Terminating instance: {instance_id} launched on {launch_time}")
                ec2_client.terminate_instances(InstanceIds=[instance_id])

def delete_unused_security_groups():
    print("Checking for unused security groups...")
    security_groups = ec2_client.describe_security_groups()['SecurityGroups']

    for sg in security_groups:
        if sg['GroupName'] == 'default':
            continue

        sg_id = sg['GroupId']
        network_interfaces = ec2_client.describe_network_interfaces(Filters=[{"Name": "group-id", "Values": [sg_id]}])['NetworkInterfaces']

        if not network_interfaces:
            print(f"Deleting security group: {sg_id} ({sg['GroupName']})")
            try:
                ec2_client.delete_security_group(GroupId=sg_id)
            except Exception as e:
                print(f"Error deleting security group {sg_id}: {e}")

def delete_old_key_pairs():
    print("Checking for old key pairs...")
    three_months_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=90)
    key_pairs = ec2_client.describe_key_pairs()['KeyPairs']

    for key_pair in key_pairs:
        key_name = key_pair['KeyName']
        key_creation_time = key_pair.get('CreateTime', None)  # Replace with the actual method to fetch creation time, if available
        if key_creation_time and key_creation_time < three_months_ago:
            print(f"Deleting key pair: {key_name} created on {key_creation_time}")
            try:
                ec2_client.delete_key_pair(KeyName=key_name)
            except Exception as e:
                print(f"Error deleting key pair {key_name}: {e}")

def delete_unused_iam_users():
    print("Checking for unused IAM users...")
    six_months_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=6 * 30)
    users = iam_client.list_users()['Users']

    for user in users:
        user_name = user['UserName']
        last_used = iam_client.get_user(UserName=user_name)['User'].get('PasswordLastUsed')

        if last_used and last_used < six_months_ago:
            print(f"Deleting IAM user: {user_name}, last used on {last_used}")
            try:
                iam_client.delete_user(UserName=user_name)
            except Exception as e:
                print(f"Error deleting IAM user {user_name}: {e}")

if __name__ == "__main__":
    delete_old_ebs_snapshots()
    delete_old_cloudwatch_log_groups()
    delete_old_ec2_instances()
    delete_unused_security_groups()
    delete_old_key_pairs()
    delete_unused_iam_users()
