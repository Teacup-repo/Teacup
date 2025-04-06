# 📧 Email DLP Lab with Docker + Postfix

This project showcases a lightweight Data Loss Prevention (DLP) lab built with Docker and Postfix. It simulates an email server that filters outbound messages for sensitive data like SSNs and credit card numbers. Alerts are logged when violations are detected.

Built for reproducibility in a safe containerized environment.

---

## 🚀 What This Lab Does

✅ Builds a custom Postfix mail server inside a Docker container  
✅ Routes outbound emails through a DLP script  
✅ Scans for:
- Social Security Numbers (SSNs)
- Credit card numbers (Visa, MasterCard)
- (Optional) Confidential keywords  
✅ Logs alerts to `/var/log/dlp-log.txt`

---

## 🛠 Technologies Used

| Tool         | Purpose                            |
|--------------|-------------------------------------|
| Docker       | Containerize the mail server setup |
| Postfix      | Simulated outbound mail server     |
| Mailutils    | CLI email sending utility          |
| Bash Script  | DLP logic with regex matching      |
| Regex        | Detect sensitive data patterns     |

---

## 📸 Lab in Action

### 🔍 Test Case Output
![DLP test case](./DLP%20test%20case.png)

### 🐳 Docker Container View
![Docker result](./docker%20result.png)

---

## 💡 What I Learned

This lab deepened my practical understanding of email-based data loss prevention using open-source tools. I learned how to:

- Containerize a mail server using Docker for isolated testing
- Intercept and filter outbound SMTP traffic with Postfix and a custom script
- Apply regex-based content inspection to identify sensitive data patterns like SSNs and credit cards
- Log and verify DLP alerts effectively

By simulating this DLP workflow, I gained insight into how content filtering integrates into mail pipelines—useful for securing enterprise email systems and developing custom compliance controls.

---

> 🧪 All testing was done in a controlled environment with no real sensitive data.

