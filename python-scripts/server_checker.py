#!/usr/bin/env python3
# ================================================
# Server Connectivity Checker
# Author: Arpan Savaliya
# Purpose: Check which servers are up or down
# ================================================

import subprocess
import datetime

# List of servers to check
# In real life this would come from a config file
SERVERS = [
    "google.com",
    "github.com",
    "stackoverflow.com",
    "thiswebsitedoesnotexist12345.com",
    "amazon.com"
]

def ping_server(server):
    # This function pings a server once
    # Returns True if reachable, False if not
    result = subprocess.run(
        f"ping -c 1 -W 2 {server}",
        shell=True,
        capture_output=True,
        text=True
    )
    # -c 1 means ping once
    # -W 2 means wait max 2 seconds for reply
    # returncode 0 means success
    return result.returncode == 0

def check_all_servers(server_list):
    # This function checks all servers
    # Returns a list of results
    results = []
    for server in server_list:
        print(f"Checking {server}...")
        is_up = ping_server(server)
        results.append({
            "server": server,
            "status": "UP" if is_up else "DOWN"
        })
    return results

def print_report(results):
    # This function prints a clean report
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "=" * 50)
    print(f"  SERVER STATUS REPORT")
    print(f"  Generated: {now}")
    print("=" * 50)

    up_count = 0
    down_count = 0

    for result in results:
        server = result["server"]
        status = result["status"]

        if status == "UP":
            up_count += 1
            print(f"  ✓  {server:<35} UP")
        else:
            down_count += 1
            print(f"  ✗  {server:<35} DOWN")
            # :<35 means left align in 35 character space
            # makes the output look neat and aligned

    print("=" * 50)
    print(f"  Total: {len(results)} servers")
    print(f"  Up: {up_count}  |  Down: {down_count}")
    print("=" * 50)

    if down_count > 0:
        print(f"\n  ACTION NEEDED: {down_count} server(s) are down!")
    else:
        print("\n  All servers are healthy.")

# Run everything
print("Starting server checks...")
results = check_all_servers(SERVERS)
print_report(results)
