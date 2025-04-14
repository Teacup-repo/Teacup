# 🛡️ C++ Threat Detection Agent

This project simulates a lightweight endpoint detection tool written in C++ — designed to monitor process behavior and flag suspicious patterns like privilege escalation and unusual parent-child process chains.

It mimics how EDR (Endpoint Detection and Response) systems catch post-exploitation behavior using simple heuristics.

---

## 🔧 How to Compile & Run

> 💻 Requires: g++ (MinGW or MSYS2 on Windows)

## 💡 What It Does

- Simulates a process list including PID, parent, name, and privilege status
- Flags:
  - Processes run with elevated privileges (e.g. netcat.exe)
  - Suspicious parent-child combos (e.g. winword.exe spawning powershell.exe)
- Writes all detections to a log file `suspicious_processes.log`

---

## 🧪 Sample Output

```
[!] Suspicious parent-child behavior: cmd.exe -> whoami.exe
[!] Suspicious elevated process: netcat.exe (PID: 1004)
[!] Suspicious parent-child behavior: winword.exe -> powershell.exe
Threat scan complete. Log saved to suspicious_processes.log
```

---

## 📸 Screenshots

### 🔍 Terminal Output

![Terminal Screenshot](terminal%20output.png)

### 📄 Generated Log File

![Log File Screenshot](log%20file.png)

---

## 🛠️ How to Run It (Windows)

1. Open PowerShell and navigate to your file location:
    ```powershell
    cd "C:\Users\YourName\Downloads"
    ```

2. Compile the C++ program:
    ```powershell
    g++ process_monitor_ASCII.cpp -o monitor.exe
    ```

3. Run the program:
    ```powershell
    .\monitor.exe
    ```

4. Check the log output:
    ```powershell
    notepad suspicious_processes.log
    ```

---

