from collections import defaultdict

THRESHOLD = 3
failed_logins = defaultdict(int)
success_after_fail = {}

with open('log_sample.txt.txt', 'r') as log_file:
    for line in log_file:
        if "Failed password" in line:
            parts = line.strip().split()
            ip = parts[parts.index("from") + 1]
            failed_logins[ip] += 1

        elif "Accepted password" in line:
            parts = line.strip().split()
            ip = parts[parts.index("from") + 1]
            if failed_logins[ip] >= THRESHOLD:
                success_after_fail[ip] = True

# Display suspicious IPs
print("\n🔍 Suspicious IPs Detected:\n")
for ip in success_after_fail:
    print(f"⚠️  {ip} had {failed_logins[ip]} failed attempts before a successful login.")
