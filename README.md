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

⚙️ How It Works:-
  * CloudWatch triggers the Lambda function on a schedule.
    
  * Lambda scans AWS resources using Boto3.
    
  * Identifies unused or idle resources.
    
  * Sends alert notification (optional).
    
  * Deletes or stops resources automatically.
    
  * Logs all actions in CloudWatch.



Why It’s Powerful:-

   • Saves cloud cost and automates maintenance.

   • Demonstrates AWS, IAM, and boto3 knowledge.

   • Real-world DevOps use case for cost optimization.
