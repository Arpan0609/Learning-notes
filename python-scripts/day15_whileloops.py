#!/usr/bin/env python3
# Day 15 — While loops in Python

# While loop keeps running as long as condition is True
# Exactly like bash but cleaner syntax

# Example 1 — basic counter
print("--- Basic counter ---")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
    # count += 1 is same as count = count + 1
    # ALWAYS increment or loop runs forever!

# Example 2 — wait for correct input
print("\n--- Input validation ---")
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    answer = input("Type 'yes' to continue: ")
    if answer == "yes":
        print("Correct! Moving on.")
        break
        # break immediately exits the loop
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Wrong. {remaining} attempts remaining.")

if attempts == max_attempts:
    print("Too many wrong attempts.")

# Example 3 — retry logic
# This is VERY common in real DevOps scripts
# Keep trying to connect until it works or max retries reached
print("\n--- Retry logic ---")
import time

max_retries = 3
retry_count = 0
connected = False

while retry_count < max_retries and not connected:
    print(f"Attempt {retry_count + 1} of {max_retries}...")
    # In real script you would try to connect here
    # We simulate with a fake connection check
    if retry_count == 2:
        connected = True
        print("Connected successfully!")
    else:
        print("Connection failed. Retrying in 1 second...")
        time.sleep(1)
        retry_count += 1

if not connected:
    print("Could not connect after all retries")
