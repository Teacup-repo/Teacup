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

---

## 🖥️ Screenshot: Detection Logic

Here's the core of the script — it reads the log, tracks IPs, and flags suspicious behavior:

![Automation Script](Automation%20script.png)

---

## 🧪 Screenshot: Brute-force Detected

This is what happens when an IP crosses the failed login threshold:

![IPs Detected](IPs%20detected.png)

---

## ⚠️ Screenshot: Possible Compromise Detected

A successful login **after multiple failures** is flagged as a potential account compromise:

![Compromised Login](Ips%20detected%20with%20brute%20force%20-%20compromised.png)

---

## 🛠️ How to Run It

1. Clone or download the repo  
2. Open it in Visual Studio, VS Code, or any Python IDE  
3. Make sure you have Python 3.8+  
4. Modify `log_sample.txt.txt` to test different login scenarios  
5. Run the script and view flagged IPs in your terminal

---

## ✉️ (Optional) Email Alerting — Simulated Setup

I included optional logic to send email alerts for detected events. It's turned off by default, but here's what you'd configure if you wanted to use it:

```python
# Email Config
SENDER_EMAIL = 'your_email@gmail.com'
RECEIVER_EMAIL = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'  # Use Gmail App Password (2FA enabled)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

