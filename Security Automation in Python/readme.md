# 🔐 Suspicious Login Detector — Security Automation in Python

This project is a simple but powerful Python-based security script I created to simulate a real-world detection tool. It reads system-style log files and looks for signs of suspicious login behavior — like brute-force attempts or logins that might indicate a compromised account.

The goal of this lab was to strengthen my Python scripting skills while applying cybersecurity concepts like log analysis, incident detection, threshold-based alerts, and (optionally) automated email notifications.


📄 [View Python Script](./Python_Automation_lab.py)

---

## 🧠 What the Script Does

When the script runs, it does the following:

1. Reads a system-style log file (`log_sample.txt.txt`) line by line  
2. Tracks how many times each IP address has failed to log in  
3. Flags IPs with multiple failed attempts (default threshold: 3) as potential **brute-force attempts**  
4. If a successful login follows repeated failures, flags it as a **possible compromised system**  
5. Optionally sends an email alert when suspicious behavior is detected

---

## 🖥️ Screenshot: Detection Logic

Here's the core Python logic that reads the log and flags suspicious behavior:

![Automation Script](Automation%20script.png)

---

## 🧪 Screenshot: Brute-force Activity Detected

When an IP triggers the threshold of failed logins, it’s flagged like this:

![IPs Detected](IPs%20detected.png)

---

## ⚠️ Screenshot: Possible Compromised Login

If a successful login follows repeated failures, the script flags it as a possible compromise:

![Compromised Login](Ips%20detected%20with%20brute%20force%20-%20compromised.png)


---
### 🧪 Screenshot: GeoIP Lookup Enabled

This image shows how the script enriches brute-force or compromised logins with location info:

![Code with GeoIP](code%20with%20GeoIP.png)

---

## 🌐 Testing with Public IPs

To simulate real-world behavior, I created a `log_sample_public.txt` file using public IPs (like `8.8.8.8`, `1.1.1.1`, etc.).  
This ensures that GeoIP lookups work correctly and shows how private/internal IPs are excluded from geolocation.

### 📸 Screenshot: Sample Log with Public IPs

![Using Public IPs](using%20public%20IPs%20for%20testing.png)

---

## 🛠️ How to Run It

1. Clone or download this repo  
2. Open it in Visual Studio, VS Code, or any Python IDE  
3. Ensure you're running Python 3.8 or higher  
4. Modify `log_sample.txt.txt` to simulate different login scenarios  
5. Run the script — detection results will print in the terminal

---

## ✉️ Email Alerting (Optional, Simulated)

The script includes email alert logic using `smtplib`. You don’t need to enable it to run the lab — it’s here to show that I know how to securely configure automated alerts.

### 💡 What You’d Configure (if enabled):

```python
SENDER_EMAIL = 'your_email@gmail.com'
RECEIVER_EMAIL = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'  # Use Gmail App Password with 2FA
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
