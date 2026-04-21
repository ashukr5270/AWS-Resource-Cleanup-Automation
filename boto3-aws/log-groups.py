import boto3

# Initialize a session using the "default" profile
aws_management_console = boto3.session.Session(profile_name="default")

# Get the CloudWatch Logs client
logs_client = aws_management_console.client('logs')

# List all CloudWatch log groups
response = logs_client.describe_log_groups()

print("CloudWatch Log Groups Details:\n")
for log_group in response['logGroups']:
    log_group_name = log_group['logGroupName']
    retention_in_days = log_group.get('retentionInDays', 'Never Expire')
    kms_key_id = log_group.get('kmsKeyId', 'No Encryption')
    stored_bytes = log_group.get('storedBytes', 'Unknown')

    # Display log group details
    print(f"Log Group Name: {log_group_name}")
    print(f"  Retention Period: {retention_in_days} days")
    print(f"  KMS Key ID: {kms_key_id}")
    print(f"  Stored Bytes: {stored_bytes}")

    # Fetch anomaly detection configurations for the log group
    anomaly_detection_response = logs_client.describe_metric_filters(logGroupName=log_group_name)
    metric_filters = anomaly_detection_response.get('metricFilters', [])
    if metric_filters:
        print("  Anomaly Detection Configurations:")
        for metric_filter in metric_filters:
            print(f"    Metric Name: {metric_filter['metricTransformations'][0]['metricName']}")
            print(f"    Metric Namespace: {metric_filter['metricTransformations'][0]['metricNamespace']}")
            print(f"    Metric Value: {metric_filter['metricTransformations'][0]['metricValue']}")
    else:
        print("  Anomaly Detection Configurations: None")

    print()