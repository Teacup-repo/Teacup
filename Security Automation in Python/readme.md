# 🔐 Suspicious Login Detector — Security Automation in Python

This project is a simple but powerful Python-based security script I created to simulate a real-world detection tool. It reads system log files and looks for signs of suspicious login behavior, like brute-force attempts or logins that might indicate a compromised account.

The goal of this lab was to strengthen my Python scripting skills while applying core cybersecurity concepts like log analysis, incident detection, and alerting.

---

## 🧠 What the Script Does

When the script runs, it does the following:

1. Reads a system-style log file (`log_sample.txt.txt`) line by line
2. Tracks how many times each IP address has failed to log in
3. Flags IPs that trigger multiple failures (default: 3) as possible **brute-force attempts**
4. If a successful login follows failed attempts, it's flagged as a **possible compromised system**
5. Sends an email alert when suspicious activity is detected

---

## 🧪 Screenshot: Automation Logic

![Automation Script](Automation%20script.png)

This shows the detection engine in Python — simple, readable, and powerful.

---

