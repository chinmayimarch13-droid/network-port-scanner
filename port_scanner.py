# network-port-scannerimport socket

target = input("Enter IP address (example: 127.0.0.1): ")

print("Scanning started...\n")

for port in range(20, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()

print("\nScan completed.")
