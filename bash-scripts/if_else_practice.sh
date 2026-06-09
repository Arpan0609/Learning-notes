#!/bin/bash

# Basic if/else structure:
# if [ condition ]; then
#     do something
# elif [ other condition ]; then
#     do something else
# else
#     do this if nothing matched
# fi   ← this closes the if block (if backwards!)

# Example 1 — Check a number
NUMBER=75

if [ $NUMBER -gt 90 ]; then
    echo "Excellent score!"
elif [ $NUMBER -gt 70 ]; then
    echo "Good score"
elif [ $NUMBER -gt 50 ]; then
    echo "Average score"
else
    echo "Need improvement"
fi

# Example 2 — Check if a file exists
FILE="/etc/passwd"

if [ -f "$FILE" ]; then
    echo "$FILE exists"
else
    echo "$FILE does not exist"
fi

# Example 3 — Check if a directory exists
DIR="/home"

if [ -d "$DIR" ]; then
    echo "$DIR is a directory"
fi

# Example 4 — Check if a service is running
if systemctl is-active --quiet nginx; then
    echo "Nginx is running"
else
    echo "Nginx is NOT running — starting it now"
    sudo systemctl start nginx
fi
