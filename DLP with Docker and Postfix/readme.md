# 📧 Email DLP Lab with Docker + Postfix – Privacy-Focused Detection

This lab simulates a **Data Loss Prevention (DLP)** workflow using a containerized Postfix mail server and a custom Bash script to detect outbound messages containing sensitive data such as **Social Security Numbers (SSNs)** and **credit card numbers**. All detections are logged and test cases are containerized for safe experimentation.

🔐 This is a **privacy-focused lab** that demonstrates real-world email content inspection aligned with DLP and compliance controls (e.g., **GDPR Article 32**, **NIST PR.DS-2**, **PCI DSS 3.2.1**).

---

## 🚀 What This Lab Does

✅ Builds a custom Postfix mail server inside a Docker container  
✅ Routes outbound emails through a DLP inspection script  
✅ Scans for:

- Social Security Numbers (SSNs)  
- Credit card numbers (Visa, MasterCard)  
- (Optional) Confidential keywords (e.g., `"internal use only"`)  

✅ Logs alerts to: `/var/log/dlp-log.txt`

---

## 🛠 Technologies Used

| Tool        | Purpose                                   |
|-------------|-------------------------------------------|
| Docker      | Containerize the mail server setup        |
| Postfix     | Simulated outbound SMTP server            |
| Mailutils   | Send test emails from CLI                 |
| Bash Script | DLP logic with regex matching             |
| Regex       | Detect sensitive content patterns         |

---

## 📸 Lab in Action

### 🔍 DLP Test Case

![DLP test case](./DLP%20test%20case.png)

### 🐳 Docker Container View


![Docker container result](./docker%20result.png)
---

## 💡 What I Learned

This lab deepened my practical understanding of **data loss prevention (DLP)** using open-source tools in a controlled, containerized environment. I learned how to:

- 🐳 Containerize a mail server for isolated testing  
- 📬 Intercept and filter SMTP traffic with Postfix  
- 🧠 Apply regex-based logic to scan for privacy violations  
- 📄 Log detections in a format useful for SIEM and alerting workflows

By simulating this DLP pipeline, I explored how **content filtering** integrates with email systems — critical for building **privacy-aware detections** in enterprise and regulated environments.

---

## 🧪 Ethical Note

All testing was performed in a secure lab with synthetic data — no real sensitive information was used.

---

## 🧩 Compliance & Privacy Mappings

| Framework | Relevant Control |
|-----------|------------------|
| **GDPR**  | Article 32 – Data protection by design |
| **NIST CSF** | PR.DS-2 – Data-in-transit is protected |
| **PCI DSS** | Req 3.2.1 – No storage of sensitive auth data in email |

---

