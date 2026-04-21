import boto3

# Initialize a session using the "default" profile
aws_management_console = boto3.session.Session(profile_name="default")

# Get the S3 resource
s3_console = aws_management_console.resource('s3')

# List all S3 buckets
for bucket in s3_console.buckets.all():
    print(bucket.name)