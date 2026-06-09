#!/bin/bash

#!/bin/bash

# Creating variables — NO spaces around the = sign
NAME="Arpan"
GOAL="DevOps Engineer in USA"
YEAR=2026
SERVER_IP="34.121.55.245"

# Using variables — always put $ before the name
echo "My name is $NAME"
echo "My goal is: $GOAL"
echo "Target year: $YEAR"
echo "My server IP: $SERVER_IP"

# Variables from commands — use $() to capture output
CURRENT_DATE=$(date)
CURRENT_USER=$(whoami)
DISK_USAGE=$(df / | awk 'NR==2 {print $5}')
FREE_MEMORY=$(free -h | awk 'NR==2 {print $4}')

echo ""
echo "--- System Info ---"
echo "Date: $CURRENT_DATE"
echo "Logged in as: $CURRENT_USER"
echo "Disk usage: $DISK_USAGE"
echo "Free memory: $FREE_MEMORY"

# Math with variables
TOTAL=100
USED=65
FREE=$((TOTAL - USED))
echo ""
echo "Storage: $USED used out of $TOTAL — $FREE remaining"
