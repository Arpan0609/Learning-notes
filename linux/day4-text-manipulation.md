# Day 4 — Text Manipulation | May 17, 2026

## Core text tools
| Command | What it does | Example |
|---------|-------------|---------|
| cat file | Print entire file | cat app.log |
| cat -n file | Print with line numbers | cat -n app.log |
| head -5 file | First 5 lines | head -5 app.log |
| tail -10 file | Last 10 lines | tail -10 app.log |
| tail -f file | Follow file live | tail -f /var/log/syslog |
| wc -l file | Count lines | wc -l app.log |

## grep — search
| Command | What it does |
|---------|-------------|
| grep "ERROR" file | Find matching lines |
| grep -i "error" file | Case insensitive |
| grep -n "error" file | Show line numbers |
| grep -c "error" file | Count matches |
| grep -v "INFO" file | Exclude matches |
| grep -r "error" /path | Search recursively |
| grep -E "ERR|WARN" file | Multiple patterns |
| grep -A 2 "ERROR" file | 2 lines after match |

## pipe |
Sends output of one command into another
grep "ERROR" app.log | wc -l

## awk — column processing
| Command | What it does |
|---------|-------------|
| awk '{print $1}' file | Print column 1 |
| awk '{print $1,$9}' file | Print columns 1 and 9 |
| awk '$9 == "403"' file | Filter by column value |
| awk 'END{print NR}' file | Count lines |

## sed — find and replace
| Command | What it does |
|---------|-------------|
| sed 's/old/new/g' file | Replace (screen only) |
| sed -i 's/old/new/g' file | Replace in file |
| sed '/pattern/d' file | Delete matching lines |
| sed -n '1,5p' file | Print lines 1-5 |

## Real world uses
- tail -f = watch live logs
- grep ERROR = find problems
- awk = extract columns from logs
- sed = change config values in scripts
