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

### 📊 Visualizations:

#### 🔹 Error Message Distribution
![Windows Log - Error Message](Window%20log%20error%20msg.png)

#### 🔹 Log Grouping by Type
![Windows Log - Grouping](Window%20log%20grouping%20.png)

#### 🔹 Source Event Types
![Windows Log - Source Event](Window%20log%20source%20event.png)

#### 🔹 Identified Event IDs
![Windows Log - Identified Event ID](Window%20log-%20identified%20event%20id.png)

#### 🔹 Pie Chart: Log Breakdown
![Windows Log - Pie Chart](Window%20log-%20pie%20chart.png)

#### 🔹 Correlation: Warnings Followed by Errors
![Windows Log - Warning Before Error](Window%20log-%20warning%20follow%20by%20error%20finding.png)

---

## 📁 Lab 2: Apache Web Log Security Analysis

Used Splunk to analyze 1,000 Apache web server logs and assess the security posture of a web application.

### ✅ Key Findings:
- **Total Requests**: 1,000  
- **Top Requested URL**: `/about.html` (221 requests)  
- **Most Common Response Code**: `500 Internal Server Error` (265 occurrences)  
- **Suspicious Pattern**: Unusually high 500 errors and repeated hits to a single page indicated potential DoS or misconfiguration

### 📊 Visualizations:

#### 🔹 Apache Log Sample
![Apache Log](Apache%20log.png)

#### 🔹 Most Requested URL
![Apache Top URL](Apache%20Top%20URL%20.png)

#### 🔹 Most Common Response Code
![Apache Most Response Code](Apache%20most%20response%20code.png)
