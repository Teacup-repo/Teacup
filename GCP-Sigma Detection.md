Sigma Rule: Suspicious Service Account Creation in Google Cloud (GCP)

## Summary
This Sigma rule is part of the **Hafez GCP Sigma Detection Lab**, inspired by a recommendation from Hafez. It detects the creation of new Google Cloud service accounts (`google.iam.admin.v1.CreateServiceAccount`) occurring **outside of standard working hours** (12am–4am PST). 

The rule is designed for **GCP Cloud Audit Logs** and can help identify suspicious IAM activity such as:
- Privilege escalation
- Unauthorized automation
- Persistence via newly created service accounts

> 💡 Written in [Sigma](https://sigmahq.io/) format and mapped to the GCP Audit log schema. Ideal for Detection-as-Code workflows in SOCs and cloud-native security teams.

---

🔍 Sigma Rule Metadata
- **File**: `iam_suspicious_sa_creation.yml`
- **Platform**: Google Cloud Platform
- **Log Source**: `product: gcp`, `service: audit`
- **ATT&CK Tags**: 
  - T1078.004 (Valid Accounts: Cloud Accounts)
  - T1087 (Account Discovery)

---

🧪 Sample Detection Query (Logs Explorer)
```sql
resource.type="project"
protoPayload.methodName="google.iam.admin.v1.CreateServiceAccount"
protoPayload.authenticationInfo.principalEmail!="admin@teacup.blog"
timestamp >= "2025-06-10T08:00:00Z"
timestamp <= "2025-06-10T12:00:00Z"
