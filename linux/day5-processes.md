# Day 5 — Process Management | May 18, 2026

## What is a process?
Every running program = a process
Each has: PID, PPID, USER, CPU%, MEM%, STATUS

## ps commands
| Command | What it does |
|---------|-------------|
| ps | Your processes only |
| ps aux | ALL processes |
| ps aux --sort=-%cpu | Sort by CPU |
| ps aux --sort=-%mem | Sort by memory |
| ps aux | grep nginx | Find specific process |

## top / htop
| Tool | Use for |
|------|---------|
| top | Built-in live monitor |
| htop | Better colored version |
| top shortcut M | Sort by memory |
| top shortcut P | Sort by CPU |
| top shortcut q | Quit |

## kill signals
| Signal | Command | Meaning |
|--------|---------|---------|
| SIGTERM | kill -15 PID | Polite stop |
| SIGKILL | kill -9 PID | Force stop |
| SIGHUP | kill -1 PID | Reload config |

## Background jobs
| Command | What it does |
|---------|-------------|
| command & | Run in background |
| jobs | List background jobs |
| fg 1 | Bring job 1 to foreground |
| bg 1 | Send job 1 to background |
| Ctrl+Z | Suspend current process |
| Ctrl+C | Kill current process |
| nohup cmd & | Keep running after SSH disconnect |

## Resource monitoring
| Command | What it shows |
|---------|--------------|
| free -h | Memory usage |
| df -h | Disk usage |
| du -sh folder | Folder size |
| uptime | Load average |
| lscpu | CPU info |
| who / w | Logged in users |

## Real world rules
- Load average should be < number of CPU cores
- Always try kill -15 before kill -9
- Use nohup for long running processes over SSH
- ps aux | grep name = first step when app is down
