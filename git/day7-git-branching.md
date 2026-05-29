# Day 7 — Git Branching | May 20, 2026

## What is a branch?
A branch is an independent line of development.
Main branch = production (always stable)
Feature branches = where work happens

## Core branch commands
| Command | What it does |
|---------|-------------|
| git branch | List all branches |
| git branch name | Create new branch |
| git checkout name | Switch to branch |
| git checkout -b name | Create AND switch |
| git merge name | Merge branch into current |
| git branch -d name | Delete branch |
| git push origin name | Push branch to GitHub |

## The professional Git workflow
1. git checkout main
2. git pull origin main
3. git checkout -b feature/my-feature
4. make changes + git add + git commit
5. git push origin feature/my-feature
6. Open Pull Request on GitHub
7. Review + merge to main
8. git checkout main + git pull
9. git branch -d feature/my-feature

## Merge vs Rebase
- Merge: combines branches, keeps history
- Rebase: rewrites history, cleaner log
- For beginners: always use merge
