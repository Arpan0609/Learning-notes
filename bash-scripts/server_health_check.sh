#!/bin/bash

# ================================================
# Server Health Check Script
# Author: Arpan Savaliya
# Purpose: Check server health and report status
# ================================================

# Colors for output (makes it easier to read)
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color — resets color back to normal

# Thresholds
DISK_THRESHOLD=80
MEMORY_THRESHOLD=80
CPU_THRESHOLD=80

echo "================================================"
echo "   SERVER HEALTH CHECK — $(date)"
echo "   Server: $(hostname)"
echo "================================================"
echo ""

# CHECK 1 — Disk Space
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | tr -d '%')
echo "Checking disk space..."
if [ $DISK_USAGE -gt $DISK_THRESHOLD ]; then
    echo -e "${RED}ALERT: Disk usage is at ${DISK_USAGE}% — above ${DISK_THRESHOLD}% threshold!${NC}"
else
    echo -e "${GREEN}OK: Disk usage is at ${DISK_USAGE}%${NC}"
fi

echo ""

# CHECK 2 — Memory
MEMORY_USAGE=$(free | awk 'NR==2 {printf "%.0f", $3/$2*100}')
echo "Checking memory..."
if [ $MEMORY_USAGE -gt $MEMORY_THRESHOLD ]; then
    echo -e "${RED}ALERT: Memory usage is at ${MEMORY_USAGE}% — above ${MEMORY_THRESHOLD}% threshold!${NC}"
else
    echo -e "${GREEN}OK: Memory usage is at ${MEMORY_USAGE}%${NC}"
fi

echo ""

# CHECK 3 — Nginx service
echo "Checking nginx service..."
if systemctl is-active --quiet nginx; then
    echo -e "${GREEN}OK: Nginx is running${NC}"
else
    echo -e "${RED}ALERT: Nginx is NOT running!${NC}"
fi

echo ""

# CHECK 4 — SSH service
echo "Checking SSH service..."
if systemctl is-active --quiet ssh; then
    echo -e "${GREEN}OK: SSH is running${NC}"
else
    echo -e "${RED}ALERT: SSH is NOT running!${NC}"
fi

echo ""

# CHECK 5 — Internet connectivity
echo "Checking internet connectivity..."
if ping -c 1 google.com &>/dev/null; then
    echo -e "${GREEN}OK: Internet is reachable${NC}"
else
    echo -e "${RED}ALERT: Cannot reach internet!${NC}"
fi

echo ""
echo "================================================"
echo "   Health check complete"
echo "================================================"
