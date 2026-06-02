# Day 9 — Linux Networking | May 22, 2026

## Key concepts
- IP address = home address for computer
- Private IP = works inside network only (192.168.x.x or 10.x.x.x)
- Public IP = works on internet
- DNS = phone book that converts domain to IP
- Port = door on server (each service has its own door)
- Firewall = security guard that allows or blocks traffic

## Important commands
| Command | What it does |
|---------|-------------|
| ip addr show | See your IP addresses |
| ping -c 4 google.com | Test if server reachable |
| nslookup google.com | DNS lookup |
| dig google.com +short | Quick DNS lookup |
| curl http://localhost | Test HTTP response |
| curl -I http://localhost | See HTTP headers |
| wget https://url/file | Download a file |
| sudo ss -tulpn | See all open ports |
| sudo netstat -tulpn | See all open ports (older) |
| traceroute google.com | Trace path of data |
| cat /etc/hosts | See local DNS overrides |
| cat /etc/resolv.conf | See DNS server being used |

## UFW Firewall
| Command | What it does |
|---------|-------------|
| sudo ufw status | Check if firewall is on |
| sudo ufw enable | Turn on firewall |
| sudo ufw allow 22/tcp | Allow SSH |
| sudo ufw allow 80/tcp | Allow HTTP |
| sudo ufw deny 3306/tcp | Block MySQL from outside |
| sudo ufw status verbose | See all rules |

## Important ports to memorize
22=SSH, 80=HTTP, 443=HTTPS, 3306=MySQL,
5432=PostgreSQL, 6379=Redis, 8080=App server

## Troubleshooting order
1. ping server (is it reachable?)
2. ss -tulpn (is port open?)
3. systemctl status (is service running?)
4. ufw status (is firewall blocking?)
5. curl localhost (works locally?)
6. check logs with journalctl
