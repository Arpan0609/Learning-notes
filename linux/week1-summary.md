# Week 1 Summary — Linux Foundations
**Dates:** May 14–19, 2026
**Phase:** 1 — Foundations

## What I covered this week
- Day 1: GitHub account + Git setup + SSH keys
- Day 2: GCP VM setup + first 15 Linux commands
- Day 3: File permissions — chmod, chown, rwx numbers
- Day 4: Text manipulation — grep, awk, sed, pipes
- Day 5: Process management — ps, top, kill, nohup, jobs

## Most important commands I learned
\`\`\`bash
# Navigation
pwd, ls -la, cd, mkdir, touch, rm -r, cp, mv

# Permissions  
chmod 755 script.sh
chmod 600 secret.key
chown user:group file

# Text tools
grep -c "ERROR" app.log
tail -f /var/log/syslog
awk '{print $1}' file | sort | uniq -c
sed -i 's/old/new/g' file

# Processes
ps aux | grep processname
kill -9 PID
killall processname
nohup command &
jobs, fg, bg
\`\`\`

## Things that were tricky
- killall ping to stop background ping (learned from real mistake!)
- kill %1 only works for shell jobs, kill PID for all processes
- Ctrl+C doesn't work on background processes

## Interview questions I can now answer
1. chmod 755 = owner rwx, group rx, others rx
2. > overwrites, >> appends
3. grep -c "ERROR" file counts errors
4. ps aux shows all processes from all users
5. kill -15 is polite, kill -9 is force
6. tail -f watches live log updates
7. sudo = run as administrator
8. pipe | chains command output to next command
9. nohup keeps process running after SSH disconnect
10. grep -v excludes matching lines

## Weak areas to improve
(write your honest weak spots here)

## Score this week
Navigation: /10
Permissions: /6
Text tools: /7
Processes: /8
