# AWS-Resource-Cleanup-Automation:-


![image_alt](https://github.com/ashukr5270/AWS-Resource-Cleanup-Automation/blob/main/Pictures_%20Image.png?raw=true)


AWS Resource Cleanup Automation is a serverless cloud solution that automatically identifies and removes unused or idle AWS resources such as EC2 instances and S3 buckets. The system helps reduce operational costs, improve efficiency, and maintain a clean cloud environment using automation.

🛠️ Technologies Used:-

   Amazon Web Services (AWS),
   AWS Lambda,
   Amazon CloudWatch,
   Amazon SNS,
   Python (Boto3 SDK),
   IAM (Identity and Access Management),
  

🚀Flowchart:-

  User → CloudWatch Trigger → Lambda Function → Resource Scan → 
Identify Idle Resources → Send Notification → Cleanup → Logs

How It Works:-

  • Run script via cron job or Lambda function periodically.

  • List all AWS resources using boto3 or AWS CLI.

  • Check usage metrics (e.g., EC2 stopped > 7 days).

  • Send alerts via Slack/Email before deletion.

  • Delete or tag unused resources automatically.



Why It’s Powerful:-

   • Saves cloud cost and automates maintenance.

   • Demonstrates AWS, IAM, and boto3 knowledge.

   • Real-world DevOps use case for cost optimization.
