🔐 GCP IAM Detection Lab – Sigma Rule for Service Account Monitoring

This lab demonstrates how to detect suspicious IAM behavior in Google Cloud using Sigma-based Detection-as-Code. It focuses on identifying off-hours service account creation by analyzing GCP Cloud Audit Logs and applying a Sigma rule for structured, reusable detection logic. This use case mirrors real-world SOC workflows aligned with cloud security, compliance (NIST/ATT&CK), and continuous monitoring goals.

---

📋 Objectives

✅ Enable Cloud Audit Logs for IAM API  
✅ Simulate a suspicious service account creation using gcloud  
✅ Query logs using Logs Explorer  
✅ Write a Sigma rule for detection  
✅ Tune the rule to reduce false positives  
✅ Add time-based logic to simulate off-hours activity  
✅ Document findings in GitHub using Detection-as-Code structure

---

👨‍💻 Steps Performed

1️⃣ **Enable Audit Logs for IAM**

- Navigated to IAM & Admin > Audit Logs  
- Selected **Identity and Access Management (IAM API)**  
- Enabled: ✅ Admin Read  
- Confirmed logs are sent to Cloud Logging

📸 Screenshot: IAM audit logging enabled

---

2️⃣ **Create Suspicious Service Account**

- Opened terminal and ran:
```bash
gcloud iam service-accounts create suspicious-sa \
  --description="Created outside business hours" \
  --display-name="SuspiciousSA"
