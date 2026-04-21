# AWS-Resource-Cleanup-Automation:-


![image_alt](https://github.com/ashukr5270/AWS-Resource-Cleanup-Automation/blob/main/Pictures_%20Image.png?raw=true)


AWS Resource Cleanup Automation is a serverless cloud solution that automatically identifies and removes unused or idle AWS resources such as EC2 instances and S3 buckets. The system helps reduce operational costs, improve efficiency, and maintain a clean cloud environment using automation.

🚀 Features:-
  🔍 Automatic detection of unused resources
  
  🧹 Cleanup of stopped EC2 instances
  
  🪣 Removal of empty S3 buckets
  
  ⏰ Scheduled execution using CloudWatch
  
  🔔 Optional notifications before deletion (SNS)
  
  📊 Logging and monitoring via CloudWatch Logs
  
  🔐 Secure access using IAM roles

  

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

