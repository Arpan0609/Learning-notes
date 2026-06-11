#!/usr/bin/env python3
# Day 14 — Python basics
# Author: Arpan Savaliya

# ---- VARIABLES ----
# In Python variables are simple — no $, no quotes around names
name = "Arpan"
goal = "DevOps Engineer in USA"
target_year = 2026
days_completed = 14
days_remaining = 200 - days_completed

# ---- PRINT ----
# print() shows output on screen
print("My name is:", name)
print("My goal:", goal)
print("Target year:", target_year)

# f-string — the cleanest way to combine variables and text
# Put f before the quote, then use {} around variable names
print(f"I have completed {days_completed} days")
print(f"I have {days_remaining} days remaining")
print(f"Progress: {days_completed / 200 * 100:.1f}%")
# :.1f means show 1 decimal place

# ---- DATA TYPES ----
# Python has different types of data
my_string = "Hello"          # text — called a string
my_number = 42               # whole number — called integer
my_decimal = 3.14            # decimal number — called float
my_bool = True               # true or false — called boolean
my_list = ["web1", "web2", "web3"]  # list of items

print("\n--- Data Types ---")
print(f"String: {my_string}")
print(f"Integer: {my_number}")
print(f"Float: {my_decimal}")
print(f"Boolean: {my_bool}")
print(f"List: {my_list}")

# ---- MATH ----
print("\n--- Math ---")
print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3:.2f}")   # division
print(f"10 // 3 = {10 // 3}")      # whole number division
print(f"10 % 3 = {10 % 3}")        # remainder
print(f"2 ** 10 = {2 ** 10}")      # power of
