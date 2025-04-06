# AWS IAM & EC2 Permissions Project

This project demonstrates how to manage AWS user access and EC2 resource control using Identity and Access Management (IAM) policies.

## 🔐 Key Concepts Learned

- Creating and managing IAM users and groups
- Writing and attaching custom IAM policies
- Using conditions with resource tags to restrict access
- Enabling console access and securing with MFA
- Launching, viewing, and terminating EC2 instances
- Testing permissions with different IAM roles

## ✅ What I Did

- Created an IAM policy to allow EC2 actions only on instances tagged with `Env=development`
- Attached policy to a user group
- Created a user with console access and tested permissions
- Launched and terminated EC2 instances
- Verified access controls through user sign-in and action testing
