# 🔐 UFW Hardening on Ubuntu

This project demonstrates how to secure a Linux system using **UFW (Uncomplicated Firewall)** by allowing trusted services, denying untrusted traffic, and validating firewall behavior through scanning with **Nmap from Kali Linux**.

---

## 🧰 Tools & Environment

- 🐧 **Ubuntu 20.04 VM** (Firewall target)
- 💥 **Kali Linux VM** (Attacker/simulation for scanning)
- 🔥 **UFW** (Uncomplicated Firewall)
- 🧪 **Nmap** (for port scanning and firewall validation)

---

## ⚙️ Configuration Steps

```bash
# Allow SSH from a specific IP (Kali VM)
sudo ufw allow from 192.168.1.105 to any port 22

# Deny all other inbound traffic
sudo ufw default deny incoming
sudo ufw enable

# Add a custom deny rule
sudo ufw deny 50/tcp

# View active rules
sudo ufw status verbose

# Enable logging
sudo ufw logging on

✅ Key Takeaways
Configured UFW to allow only trusted inbound services (e.g., SSH)

Enforced default-deny posture for all other traffic, including specific port blocks

Validated firewall effectiveness using Nmap scans from an external VM

Applied host-based firewall principles and basic offensive testing techniques

🚀 What I Learned
Practical experience securing Linux systems with UFW

Importance of logging and visibility for incident response

How to simulate and evaluate firewall rules using Nmap

<img width="466" alt="UFW Deny in" src="https://github.com/user-attachments/assets/55910df4-7fdf-49da-940a-e475cfa120ee" />



