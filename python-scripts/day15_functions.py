#!/usr/bin/env python3
# Day 15 — Functions in Python

# Basic function — no input, no return value
def say_hello():
    # def means define a function
    # say_hello is the function name
    # () holds the inputs — empty means no inputs needed
    print("Hello from a function!")

# Call the function
say_hello()
say_hello()
say_hello()
# Called 3 times — same code runs 3 times

# Function with inputs (arguments)
def greet_user(name, role):
    # name and role are parameters
    # when you call the function you pass actual values
    print(f"Hello {name}!")
    print(f"Your role is: {role}")

greet_user("Arpan", "DevOps Engineer")
greet_user("John", "Developer")

# Function that RETURNS a value
def calculate_percentage(used, total):
    # This function calculates a percentage
    # and RETURNS the result to whoever called it
    percentage = (used / total) * 100
    return round(percentage, 1)
    # round(number, 1) rounds to 1 decimal place
    # return sends the value back

disk_percent = calculate_percentage(45, 100)
memory_percent = calculate_percentage(3.2, 8)
print(f"\nDisk: {disk_percent}%")
print(f"Memory: {memory_percent}%")

# Function that returns a status
def get_status(percentage, warning=75, critical=90):
    # warning=75 means default value is 75
    # if you don't pass warning it uses 75 automatically
    if percentage >= critical:
        return "CRITICAL"
    elif percentage >= warning:
        return "WARNING"
    else:
        return "OK"

# Use the function
readings = [45, 78, 92, 60, 88]
for reading in readings:
    status = get_status(reading)
    print(f"Reading: {reading}%  Status: {status}")

# Using custom thresholds
print(get_status(70, warning=60, critical=80))
