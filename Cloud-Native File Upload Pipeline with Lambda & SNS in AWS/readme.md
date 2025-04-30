# 📦 Secure File Upload & Notification System (AWS)

This project sets up a serverless, event-driven architecture using multiple AWS services to securely handle file uploads and notifications.

## 🔧 System Components

- **EC2 Instance (Amazon Linux)**  
  Used to upload files to S3 via AWS CLI. Configured with an IAM user (`tanny_intern`) with permission to access S3.

  ![Create EC2 instance](Create%20EC2%20instance.png)

- **S3 Bucket with KMS Encryption**  
  All uploaded files are stored in an S3 bucket (`bucket535kms`) with server-side encryption using AWS Key Management Service (KMS).

  ![KMS Key Generation](KMS%20key%20generation.png)

- **AWS Lambda Function**  
  Triggered by `s3:ObjectCreated:*` events. It processes uploaded files and publishes notifications to SNS.

  ![Lambda Function Code + S3 Trigger](Set%20Lambda%20funtion%20code%20and%20link%20with%20S3%20trigger.png)

- **SNS Topics**
  - **Standard Topic** → sends **email alerts** to subscribed users  
  - **FIFO Topic** → delivers messages to an **SQS FIFO queue** to ensure ordered processing

  ![SNS Setup](Set%20up%20SNS.png)

- **SQS FIFO Queue**  
  Stores messages published by the Lambda function via the FIFO topic for reliable, decoupled downstream processing.

## ✅ Workflow Summary

1. File is uploaded from EC2 to the encrypted S3 bucket
2. Lambda function is triggered automatically
3. Lambda processes the file and sends:
   - an email alert via SNS Standard  
   - a structured message to SQS via SNS FIFO

  ![Upload from EC2](uploaded%20test%20file%20to%20s3.png)
  ![Email Notification](email%20notification%20when%20file%20uploaded%20in%20S3.png)

## 🚀 Technologies Used
- AWS EC2
- AWS S3 + KMS Encryption
- AWS Lambda (Python runtime)
- Amazon SNS (Standard & FIFO)
- Amazon SQS FIFO Queue
- IAM (users, roles, policies)

## 🛡 IAM User
IAM user `tanny_intern` is granted:
- `AmazonS3FullAccess`
- `AWSLambdaExecute`
- `AmazonSNSFullAccess`

This user is used within EC2 to run `aws s3 cp` commands via CLI.

## 🚫 Challenges & Solutions

- **Region mismatch between S3 and Lambda**: Initially, the S3 bucket and Lambda function were in different AWS regions, preventing the S3 trigger from firing. I resolved this by recreating the Lambda in the same region as the bucket (`us-west-1`).

- **SNS FIFO to SQS delivery error**: The Lambda function failed silently when publishing to the FIFO topic due to missing `MessageGroupId` and `MessageDeduplicationId`. Adding those parameters fixed the issue and ensured successful SQS delivery.

---
