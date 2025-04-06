# 🧅 Network Traffic Analysis with Security Onion

This project demonstrates my ability to deploy and operate **Security Onion** in a virtual lab for analyzing network traffic, detecting anomalies, and strengthening security posture. I used real PCAP files and a layered approach for threat detection, validation, and response.

---

## 📌 What I Did

- Installed **Security Onion 2.4** on a virtual machine.
- Imported PCAP files for analysis using Zeek, Suricata, Wireshark (CLI), and Kibana.
- Monitored multiple network segments using separate interfaces.
- Investigated **malicious domains**, **HTTP traffic**, **TLS issues**, and **DNS exploits**.

> 📷 ![Imported PCAP to Security Onion](./screenshots/imported%20pcap%20to%20security%20onion.png)

---

## 🔍 Key Findings

### 🟠 Insecure File Transfers
Observed file types such as `.txt`, `.gif`, and `.html` being transferred via **unencrypted HTTP**, which exposes data in plaintext and increases the risk of MITM attacks.

> 📷 ![Unencrypted file transfer](./screenshots/Files%20transfer%20in%20the%20clear.png)

---

### 🌐 Suspicious HTTP Activity
Domains like `tabletcaptiveportal.com` and `nrgbreakdancing.com` were accessed using `GET` and `POST` methods, which may suggest **phishing** or **redirection attempts**.

> 📷 ![HTTP activity](./screenshots/HTTP%20attemp%20for%20insecure%20connection.png)

---

### 🧅 Malicious Domains Detected
`colorsuckbeh.com` flagged during SSL inspection. This domain has been linked with **botnet traffic** and **malware delivery**.

> 📷 ![Malicious domains](./screenshots/Malicious%20domains%20.png)

---

### 🛑 WPAD Spoofing Behavior
Multiple systems attempted to query `wpad.mountaintech.org`, a potential **WPAD spoofing vector** where attackers can hijack proxy configurations.

> 📷 ![WPAD activity](./screenshots/wpad.png)

---

### 📉 SSL Certificate Failures
Multiple invalid certificates were flagged:
- **Self-signed certs**
- **Unable to get local issuer cert**
- **Deprecated TLS versions (TLSv1.0)**

> 📷 ![SSL issues](./screenshots/SSL%20invalid.png)

---

### 📊 TLS Usage Analysis
Most encrypted traffic used **TLSv1.2**, but some **TLSv1.0** traffic was seen — this outdated protocol poses a security risk.

> 📷 ![Zeek SSL anomalies](./screenshots/Zeek%20TSL%20anomalies%20.png)

---

### 📈 Host Log Investigation via Kibana
Using ElasticSearch + Kibana, I tracked traffic flow, source IPs, and organization metadata. A host (Intel device) was making repeated connection attempts without responses.

> 📷 ![Kibana logs](./screenshots/Kibana%20log%20analysis.png)

---

### 🧰 Tool Usage Summary
Security Onion combines Zeek, Suricata, and Elastic Stack to provide layered insights.

> 📷 ![SO Module Breakdown](./screenshots/Zeek%20and%20Suricata%20detection.png)

---

## 🛡️ Incident Response Approach

1. **Detect** anomalies using Zeek logs and dashboards.
2. **Investigate** traffic with Wireshark and Kibana queries.
3. **Validate** domain/IP reputation and certificate issues.
4. **Respond** by identifying root causes, isolating risky hosts, and proposing fixes.

---

## 💡 What I Learned

This project deepened my understanding of **network defense and incident response workflows** using open-source tools in a simulated real-world environment.

I learned how to go beyond just capturing traffic — by importing PCAPs into Security Onion, I gained experience in **analyzing network behavior at both the packet and protocol level** using Zeek, Suricata, Wireshark, and Kibana. 

Working through different dashboards helped me correlate multiple indicators of compromise (IOCs) such as:
- **Unusual HTTP requests** to suspicious domains.
- **TLS misconfigurations**, including deprecated protocols like TLSv1.0 and invalid SSL cert chains.
- **DNS anomalies**, including repeated unresolved WPAD lookups — a common vector for man-in-the-middle attacks.
- **Unencrypted file transfers**, which could easily leak sensitive data.

By visualizing and validating these findings across tools, I strengthened my ability to think like a **blue team analyst** — identifying patterns, prioritizing alerts, and asking deeper investigative questions (e.g., "Why is this host contacting `colorsuckbeh.com`?", or "Why is this device generating repeated certificate validation errors?").

Ultimately, this lab sharpened my technical skills in traffic analysis **and** improved my mindset around **defending security posture proactively**. It emphasized how visibility, validation, and structured investigation are key in detecting and responding to threats effectively.


---


> 🔐 *All data used is simulated and intended strictly for cybersecurity training purposes.*

