# 🦠 WannaCry Ransomware Case Study

This project simulates a real-world incident response workflow by investigating potential WannaCry ransomware activity on a Windows system. Using Windows-native tools and process monitoring, the goal was to detect behavioral indicators, registry modifications, and malicious persistence.

---

## 🔧 Tools Used

- 🗂️ **Windows Registry Editor** – to search for persistence keys
- 🧠 **Process Monitor (ProcMon)** – to trace real-time file, registry, and process activity
- 📊 **Task Manager** – to observe process behavior and resource usage

---

## 🧪 Analysis Workflow

### 📝 1. Registry Analysis
- Reviewed keys under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
- **Findings:** No indicators of persistence or ransomware-related keys present in this instance

### 🔎 2. Process Monitoring
- Used ProcMon to capture real-time events during execution of suspect `.exe`
- Looked for common ransomware patterns:
  - Suspicious file creation
  - Encryption behavior
  - Registry tampering
- **Findings:** The executable was active but did **not exhibit encryption behavior**. No mutex or shadow copy deletions observed. Possibly a dormant sample or sandbox-aware malware.

### 👀 3. Task Manager Observation
- Verified that the sample was running
- Monitored CPU and disk usage
- **Findings:** No resource spike detected. Executable remained idle, supporting non-triggered behavior.

---

## 🧠 Conclusion

While no ransomware actions were triggered during this test, the investigation simulated key steps in responding to suspected ransomware activity:

- Registry hunting for persistence
- Process behavior analysis with ProcMon
- Execution trace and environmental indicators

This lab reflects best practices in **incident response and ransomware triage**, and reinforces the value of layered detection techniques, even in low-activity scenarios.

---

## 📁 Project Goal

> Demonstrate real-world investigative techniques used by SOC analysts and IR teams in detecting and understanding ransomware behavior on Windows systems.


