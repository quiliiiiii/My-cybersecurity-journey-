import socket

target = input("Enter IP address: ")

print(f"\nScanning {target}...\n")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    s.close()

print("\nScan completed.")
