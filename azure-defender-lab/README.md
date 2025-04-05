# 🛡️ Microsoft Defender for Cloud – Security Posture Lab

A hands-on lab simulating insecure configurations in a cloud environment and validating Microsoft Defender for Cloud's detection and recommendation capabilities.

## 🧠 Objective

Gain real-world experience using Azure’s Microsoft Defender for Cloud to:

- Monitor cloud security posture
- Detect open ports, misconfigurations, and risky users
- Review and respond to Defender recommendations
- Document and remediate issues in line with CIS/NIST standards

---

## 🛠️ Tools & Services Used

- 🧩 **Microsoft Defender for Cloud (Free Tier)**
- ☁️ **Azure Virtual Machines (Ubuntu 20.04 LTS)**
- 🐧 SSH & UFW firewall
- 🔓 Simulated risky configurations (weak user + disabled firewall)
- 📊 Secure Score & Recommendations dashboard

---

## ⚙️ Lab Actions

| Action | Purpose |
|--------|---------|
| Created Azure VM (Standard B1s, Ubuntu 20.04) | Free-tier eligible |
| Enabled Microsoft Defender for Cloud (Free Plan) | Monitor security posture |
| SSH into VM | Secure remote access |
| Created weak sudo user `testuser:test` | Simulate credential risk |
| Disabled UFW | Exposed host to network traffic |
| Opened SSH to the public internet (0.0.0.0/0) | Trigger risk detection |
| (Optional) Ran Nmap scan from Kali VM | Simulate external probing |

---

## 📸 Screenshots

| Screenshot | Description |
|------------|-------------|
| ![VM Config](./images/vm-config.png) | VM settings and open ports |
| ![Terminal Output](./images/testuser-ufw-disabled.png) | Risky user + disabled firewall |
| ![Secure Score](./images/secure-score.png) | Defender posture and recommendations |
| ![Alerts](./images/alerts.png) | Generated security alerts |

> 📷 Replace with your actual screenshots or terminal captures

---

## ✅ Defender Alerts Triggered

- 🔓 SSH accessible to the internet (0.0.0.0/0)
- ⚠️ Privileged user with weak password
- 🛑 Host firewall disabled (UFW off)
- ❌ No endpoint protection agent installed
- 🧠 Recommendations generated based on CIS best practices

---

## ✍️ Key Takeaways

- Defender for Cloud provides visibility into basic and advanced misconfigurations
- Secure Score reflects how posture changes based on exposed attack surfaces
- Alerts and remediation steps align with real-world compliance standards

---

## 💡 Next Steps (For Future Labs)

- Add Defender for Endpoint integration
- Explore Just-In-Time (JIT) VM access
- Apply Defender recommendations and re-measure Secure Score impact

---

## 📚 Related Skills

- ✅ NIST/CIS compliance awareness  
- ✅ Network hardening & monitoring  
- ✅ Azure security configuration  
- ✅ Incident response basics in cloud environment  
- ✅ CV-ready security documentation

---

## 📎 License

For educational purposes only. Do not expose real-world environments intentionally.
