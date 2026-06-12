from collections import Counter

failed_ips = []

with open("sample.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()

            try:
                ip = parts[-4]
                failed_ips.append(ip)
            except:
                pass

print("\n=== Failed Login Attempts ===\n")

counts = Counter(failed_ips)

for ip, count in counts.items():
    print(f"{ip}: {count} attempts")

print("\n=== Suspicious IPs (>3 attempts) ===\n")

for ip, count in counts.items():
    if count > 3:
        print(f"ALERT: {ip}")
