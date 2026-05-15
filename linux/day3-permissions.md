# Day 3 — Linux File Permissions | May 16, 2026

## Permission structure
-rwxr-xr-x = file type + owner + group + others

## Number values
r = 4, w = 2, x = 1, - = 0

## Common permission combos
| Number | Symbol | Meaning |
|--------|--------|---------|
| 777 | rwxrwxrwx | Everyone full access (dangerous!) |
| 755 | rwxr-xr-x | Scripts and executables |
| 644 | rw-r--r-- | Regular files, web files |
| 600 | rw------- | SSH keys, secret files |
| 400 | r-------- | Read-only (AWS .pem keys) |
| 000 | ---------- | No access at all |

## Commands
| Command | What it does |
|---------|-------------|
| ls -la | See permissions of all files |
| chmod 755 file | Set numeric permissions |
| chmod +x file | Add execute permission |
| chmod u+x,go-w file | Symbolic permissions |
| chown user file | Change owner |
| chown user:group file | Change owner and group |
| chown -R user folder | Change recursively |

## Real world scenarios
- SSH .pem keys: chmod 400 (AWS/GCP requirement)
- Bash scripts: chmod 755 or chmod +x
- Config files: chmod 644
- Secret files: chmod 600

## Special permissions
- s (setuid) = runs as file owner (e.g. sudo)
- t (sticky bit) = only owner can delete (e.g. /tmp)
