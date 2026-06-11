#!/usr/bin/env python3
# Lists in Python — extremely useful for DevOps

# A list is a collection of items inside []
servers = ["web-server-1", "web-server-2", "db-server", "backup-server"]
ports = [22, 80, 443, 8080, 3306]
log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]

# Access items by position (starts from 0 not 1!)
print("First server:", servers[0])    # web-server-1
print("Second server:", servers[1])   # web-server-2
print("Last server:", servers[-1])    # backup-server (-1 = last item)

# List length — how many items
print(f"Total servers: {len(servers)}")
print(f"Total ports: {len(ports)}")

# Add to list
servers.append("new-server-5")
print(f"After adding: {servers}")

# Remove from list
servers.remove("new-server-5")
print(f"After removing: {servers}")

# Check if something is in a list
if "ERROR" in log_levels:
    print("ERROR level exists in log levels")

if "TRACE" not in log_levels:
    print("TRACE level does not exist")

# Loop through a list — this is where it gets powerful
print("\n--- Checking all servers ---")
for server in servers:
    print(f"Would check: {server}")

# Loop with index number
print("\n--- Servers with numbers ---")
for index, server in enumerate(servers):
    print(f"{index + 1}. {server}")
