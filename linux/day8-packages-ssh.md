# Day 8 — Package Management + SSH | May 21, 2026

## APT Package Manager
| Command | What it does |
|---------|-------------|
| sudo apt update | Refresh package list |
| sudo apt upgrade -y | Upgrade all packages |
| sudo apt install pkg -y | Install package |
| sudo apt remove pkg | Remove package |
| sudo apt purge pkg | Remove + delete configs |
| sudo apt autoremove | Remove unused deps |
| apt search name | Search for package |
| apt show name | Show package details |
| dpkg -l | List installed packages |
| dpkg -L pkg | List package files |

## SSH Key files
| File | Purpose |
|------|---------|
| ~/.ssh/id_ed25519 | YOUR private key (never share) |
| ~/.ssh/id_ed25519.pub | YOUR public key (share with servers) |
| ~/.ssh/authorized_keys | Who can SSH into this server |
| ~/.ssh/known_hosts | Servers you've connected to |
| ~/.ssh/config | SSH shortcuts config |

## SSH Config file shortcut
Host devops-vm
    HostName SERVER_IP
    User USERNAME
    IdentityFile ~/.ssh/id_ed25519

## SCP — copy files over SSH
scp file user@server:/path      # local to remote
scp user@server:/path/file .    # remote to local
scp -r folder user@server:/path # copy entire folder

## systemctl — service management
| Command | What it does |
|---------|-------------|
| systemctl status svc | Check service status |
| systemctl start svc | Start service |
| systemctl stop svc | Stop service |
| systemctl restart svc | Restart service |
| systemctl enable svc | Start on boot |
| systemctl disable svc | Don't start on boot |
| journalctl -u svc -f | Follow service logs |

## Important ports to remember
| Port | Service |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 6379 | Redis |
| 27017 | MongoDB |
| 8080 | Common app port |
