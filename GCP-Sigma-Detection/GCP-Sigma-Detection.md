# 🔐 GCP IAM Detection Lab – Sigma Rule for Suspicious Service Account Creation

This project simulates cloud identity threats in GCP and shows how to detect them using portable Sigma rules across SIEM platforms.

We will detect suspicious IAM behavior in **Google Cloud Platform (GCP)** using **Sigma-based Detection-as-Code**. It focuses on identifying **off-hours service account creation** by analyzing Cloud Audit Logs, tuning detection logic, and versioning everything in GitHub.

## 💡 What Is Sigma?

**Sigma** is a generic signature format for writing SIEM detections in a YAML-based structure. It acts as a **translation layer between log data and detection logic** — making your rules portable, tunable, and vendor-neutral.


**These Sigma rules help detect: **
🕵️ Suspicious service account creation  
🔐 Privilege escalation via IAM policy bindings  
🔄 Misuse of GCP APIs for persistence or lateral movement

---

## 🧩 MITRE ATT&CK Mapping

| Rule                        | Tactic               | Technique      | Description                                               |
|----------------------------|----------------------|----------------|-----------------------------------------------------------|
| `iam_suspicious_sa_creation` | Privilege Escalation | T1078.004       | New service accounts used to gain unauthorized access     |
| `iam_set_policy`             | Defense Evasion / Persistence | T1098.003 | Modifying IAM bindings to maintain access or escalate     |

---

---

## 📋 Lab Objectives

✅ Enable Cloud Audit Logs for IAM API  
✅ Simulate suspicious IAM activity using `gcloud`  
✅ Query logs in Logs Explorer  
✅ Write and tune Sigma rule detections  
✅ Validate with real logs and screenshots  
✅ Document findings using Detection-as-Code format

---

## 👨‍💻 Steps Performed

### 1️⃣ Enable Audit Logs for IAM API

- Navigated to **IAM & Admin > Audit Logs**
- Selected: **Identity and Access Management (IAM API)**
- Enabled: ✅ **Admin Read**
- Saved changes to begin logging IAM events

📸 Screenshot:  
![IAM Audit Logging Enabled](./screenshots/IAM-Permission-Setup.png)

---

### 2️⃣ Simulate Suspicious Service Account Creation

- Opened Terminal and ran:

```bash
gcloud iam service-accounts create suspicious-sa \
  --description="Created outside business hours" \
  --display-name="SuspiciousSA"
```
### 3️⃣ Detect the Event in GCP Logs Explorer

- Navigated to **Cloud Logging > Logs Explorer**
- Set resource scope to: `sigma-lab-detection`
- Used the following query:

```sql
protoPayload.methodName="google.iam.admin.v1.CreateServiceAccount"
```
📸 Screenshot:  
![Service Account Detection in Logs Explorer](./screenshots/suspicious-event.png)



## 📁 Sample Log Entry

Captured during the lab:

🔹 [`create_sa_sample_alt.json`](./log_samples/create_sa_sample_alt.json.rtf)

This log includes key fields such as:

- `protoPayload.methodName`
- `protoPayload.authenticationInfo.principalEmail`
- `resource.labels.project_id`
- `timestamp`

---

## 🧠 Sigma Rule: Suspicious SA Creation

📄 [`iam_suspicious_sa_creation.yml`](./detections/iam_suspicious_sa_creation.yml.rtf)

This Sigma rule detects service account creation events that occur outside normal business hours and excludes trusted service accounts.

```yaml
detection:
  selection:
    protoPayload.methodName: "google.iam.admin.v1.CreateServiceAccount"
  filter:
    protoPayload.authenticationInfo.principalEmail|not:
      - "admin@teacup.blog"
  condition: selection and not filter
```
🔗 Additional Detection Rule 
📄 [`iam_set_policy.yml`](./detections/iam_set_policy.yml.rtf)

