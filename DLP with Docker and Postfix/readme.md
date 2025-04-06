# 📧 Email DLP Lab with Docker + Postfix

This project demonstrates a simple but effective **Data Loss Prevention (DLP)** lab using Docker and Postfix. It simulates an email server that filters outbound emails for sensitive data such as **SSNs**, **credit card numbers**, and **keywords** — alerting when violations are detected.

Built entirely in a containerized environment for safe experimentation and reproducibility.

---

## 🚀 What This Lab Does

- ✅ Builds a custom **Postfix-based mail server** inside Docker
- ✅ Pipes outbound emails through a **custom DLP script**
- ✅ Scans content for:
  - Social Security Numbers (SSNs)
  - Credit card numbers (Visa, MasterCard)
  - Confidentiality keywords (optional)
- ✅ Logs DLP alerts to: `/var/log/dlp-log.txt`

---

## 🛠 Technologies Used

| Tool | Purpose |
|------|---------|
| **Docker** | Containerize and isolate the email server |
| **Ubuntu 22.04** | Base OS |
| **Postfix** | Simulated mail transport |
| **Mailutils** | Send test emails via `mail` command |
| **Bash Script** | DLP filtering logic |
| **Regex** | Pattern matching for sensitive data |

---

