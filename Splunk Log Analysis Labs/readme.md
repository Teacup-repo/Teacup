# 🔍 Splunk Log Analysis Labs

This project showcases hands-on experience using **Splunk** to analyze both Windows Event Logs and Apache Web Logs. It focuses on identifying patterns, detecting anomalies, and generating actionable insights for threat detection and system hardening.

---

## 📁 Lab 1: Windows Event Log Analysis

Analyzed a dataset of 101 Windows Event Logs using Splunk to identify potential system reliability issues and security risks.

### ✅ Key Findings:
- **Total Events Analyzed**: 101
- **Log Type Breakdown**: 42 Errors, 34 Warnings, 24 Informational
- **Top Log Source**: `System`
- **Most Frequent Error IDs**: Event ID 1001 and 6008
- **Correlation Insight**: Warnings frequently preceded Event ID 6008 (“unexpected shutdown”), suggesting a pattern of system instability.
- **Visualization**: Generated pie chart of log type distribution and time chart of event frequency

### 🛠️ Recommendations:
- Investigate recurring Error ID 6008 to identify root cause of system crashes
- Monitor Security logs for unauthorized activity or misconfiguration
- Apply proactive health checks and alerting for early signs of failure

---

## 📁 Lab 2: Apache Web Log Security Analysis

Used Splunk to analyze 1,000 Apache web server logs and assess the security posture of a web application.

### ✅ Key Findings:
- **Total Requests**: 1,000
- **Top Requested URL**: `/about.html` (221 requests)
- **Most Common Response Code**: `500 Internal Server Error` (265 occurrences)
- **Suspicious Pattern**: Unusually high 500 errors and repeated hits to a single page indicated potential DoS or misconfiguration
- **Visualization**: Built dashboards showing request volume, response codes, and target URLs

### 🛡️ Security Insights:
- **Error Disclosure**: Repeated 500 errors may expose internal server issues
- **Reconnaissance Behavior**: High traffic to a single endpoint could indicate probing activity
- **Potential DoS Attack**: Volume and concentration of errors suggest system overload attempts

### 🛠️ Recommendations:
- Implement user-friendly error messages that suppress server-side information
- Monitor for high request frequency to individual endpoints
- Deploy WAF to block malicious traffic targeting known weak routes
- Improve input validation to reduce error-triggering payloads

---


