from collections import Counter
import re

LOG_FILE = "sample.log"
FAILED_LOGIN_THRESHOLD = 3

failed_ips = []
successful_logins = 0
total_failed_logins = 0

ip_pattern = r"from (\d+\.\d+\.\d+\.\d+)"

with open(LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" in line:
            total_failed_logins += 1
            match = re.search(ip_pattern, line)

            if match:
                failed_ips.append(match.group(1))

        elif "Accepted password" in line:
            successful_logins += 1

ip_counts = Counter(failed_ips)

print("=" * 40)
print(" SECURITY LOG ANALYSIS REPORT")
print("=" * 40)

print(f"\nTotal failed login attempts: {total_failed_logins}")
print(f"Total successful logins: {successful_logins}")
print(f"Unique suspicious IPs: {len(ip_counts)}")

print("\nFailed Login Attempts by IP:")
for ip, count in ip_counts.items():
    print(f"- {ip}: {count} failed attempts")

print("\nSuspicious IP Alerts:")
for ip, count in ip_counts.items():
    if count > FAILED_LOGIN_THRESHOLD:
        print(f"[ALERT] {ip} has {count} failed login attempts")

print("\nAnalysis completed.")
