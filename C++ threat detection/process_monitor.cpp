#include <iostream>
#include <fstream>
#include <vector>
#include <string>

// Simulated process struct
struct Process {
    std::string pid;
    std::string name;
    std::string parent;
    bool isElevated;
};

// Simulated process list
std::vector<Process> getProcesses() {
    return {
        {"1001", "explorer.exe", "wininit.exe", false},
        {"1002", "cmd.exe", "explorer.exe", false},
        {"1003", "whoami.exe", "cmd.exe", false},
        {"1004", "netcat.exe", "powershell.exe", true},
        {"1005", "powershell.exe", "winword.exe", false}
    };
}

void detectThreats(const std::vector<Process>& processes) {
    std::ofstream log("suspicious_processes.log");

    for (const auto& proc : processes) {
        if ((proc.name == "netcat.exe" || proc.name == "whoami.exe") && proc.isElevated) {
            std::cout << "[!] Suspicious elevated process: " << proc.name << " (PID: " << proc.pid << ")\n";
            log << "[ELEVATED] " << proc.name << " (PID: " << proc.pid << ") launched with elevated privileges\n";
        }

        if ((proc.name == "whoami.exe" && proc.parent == "cmd.exe") ||
            (proc.name == "powershell.exe" && proc.parent == "winword.exe")) {
            std::cout << "[!] Suspicious parent-child behavior: " << proc.parent << " -> " << proc.name << "\n";
            log << "[CHAIN] " << proc.parent << " -> " << proc.name << " flagged for unusual execution path\n";
        }
    }

    log.close();
    std::cout << "Threat scan complete. Log saved to suspicious_processes.log\n";
}

int main() {
    std::vector<Process> processes = getProcesses();
    detectThreats(processes);
    return 0;
}