#!/usr/bin/env python3
# Day 15 — For loops in Python

# Example 1 — loop through a list
servers = ["web-server-1", "web-server-2", "db-server", "backup-server"]

print("--- All servers ---")
for server in servers:
    print(f"Server: {server}")

# Example 2 — loop through numbers
print("\n--- Counting ---")
for number in range(1, 6):
    # range(1, 6) generates: 1, 2, 3, 4, 5
    # range starts at first number, stops BEFORE second number
    print(f"Number: {number}")

# Example 3 — loop with index
print("\n--- Servers with numbers ---")
for index, server in enumerate(servers):
    # enumerate gives you both the index AND the item
    print(f"{index + 1}. {server}")

# Example 4 — loop with if inside
print("\n--- Checking server names ---")
for server in servers:
    if "db" in server:
        print(f"{server} — this is a database server")
    elif "backup" in server:
        print(f"{server} — this is a backup server")
    else:
        print(f"{server} — this is a web server")

# Example 5 — loop through a range and do math
print("\n--- Disk usage simulation ---")
disk_readings = [45, 67, 82, 91, 55, 78]
for reading in disk_readings:
    if reading > 90:
        status = "CRITICAL"
    elif reading > 75:
        status = "WARNING"
    else:
        status = "OK"
    print(f"Disk: {reading}%  →  {status}")
