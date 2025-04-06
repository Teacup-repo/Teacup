# 🔍 Network Traffic Analysis with Security Onion

This project shows how I used **Security Onion** in a virtual environment to analyze network traffic, detect threats, and respond to security incidents — all while improving my hands-on skills in network defense.

---

## 🛠 What I Did

- Installed **Security Onion** on a virtual machine.
- Uploaded and analyzed a **PCAP file** using:
  - **Zeek** for network metadata.
  - **Suricata** for intrusion detection.
  - **Wireshark** (CLI-based) for packet inspection.
  - **Kibana** for log visualization.
- Monitored multiple network interfaces to simulate real-world traffic flow.
- Investigated signs of malicious activity, insecure connections, and anomalies.

---

## 🧠 Key Findings

- ✅ **Detected known malicious domains** (e.g., `colorsuckbeh.com`).
- 🔁 **Spotted DNS flood behavior** from one host (possible DoS or botnet).
- 📦 **Unencrypted file transfers** over HTTP.
- ❗ **SSL/TLS issues**, including deprecated protocols (TLSv1.0).
- ⚠️ **WPAD spoofing attempts** and suspicious DHCP hostnames.
- 🧪 Used **Wireshark** to verify findings at the packet level.

---

## 🧰 Tools Used

- **Security Onion** (Zeek, Suricata, Kibana, Wireshark CLI)
- **VirtualBox / VMware**
- **PCAP Traffic Samples**

---

## 🛡️ Incident Response Approach

I followed the NIST process:
1. **Detect** unusual traffic via Zeek & Suricata.
2. **Analyze** logs and PCAPs to confirm.
3. **Contain** (hypothetical lab response).
4. **Eradicate** root cause (malicious domains, deprecated protocols).
5. **Recover** and **document** findings.

---

## 💡 What I Learned

- How to deploy and configure Security Onion in a VM.
- How to identify real threats using logs and packet data.
- The importance of monitoring, alert triage, and incident handling.
- Gained confidence in both detection and response workflows.
