# 🔐 Suspicious Login Detector — Security Automation in Python

This project is a simple but powerful Python-based security script I created to simulate a real-world detection tool. It reads system log files and looks for signs of suspicious login behavior, like brute-force attempts or logins that might indicate a compromised account.

The goal of this lab was to strengthen my Python scripting skills while applying core cybersecurity concepts like log analysis, incident detection, and alerting. Plus, I wanted to make something I could extend and build on over time.

---

## 🧠 What the Script Does

When the script runs, it does the following:

1. Reads a system-style log file (`log_sample.txt`) line by line
2. Tracks how many times each IP address has failed to log in
3. If an IP hits the failed login threshold (3 by default), it flags it as **potential brute-force**
4. If a successful login happens *after* multiple failed attempts from the same IP, it flags it as **a possible compromised account**
5. Sends an email alert if suspicious activity is found

It's a simple simulation of what you'd expect in the early stages of a security information and event management (SIEM) system.

---

## 🧪 Example Output

```bash
🔍 Suspicious IPs Detected:

[!] 192.168.1.12 triggered 3 failed logins — possible brute-force
⚠️ 192.168.1.12 had a successful login after multiple failures — possible compromise

📧 Sending alert email...
✅ Alert email sent.
