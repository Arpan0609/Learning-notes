# Day 10 — Vim Text Editor | May 23, 2026

## Why Vim?
Vim is on every Linux server. When nano is not available
on a production server — Vim will be there.

## The 3 modes
Normal mode → press ESC (default, navigate here)
Insert mode → press i (type text here)
Command mode → press : (save, quit, search here)

## Most important rule
When in doubt → press ESC first. Always.

## Opening and closing
vim filename     open a file
:w               save
:q               quit
:wq              save and quit
:q!              quit WITHOUT saving

## Navigation (Normal mode)
h j k l          left down up right
w / b            next / previous word
gg / G           first / last line
0 / $            start / end of line

## Editing (Normal mode)
dd               delete line
yy               copy line
p                paste
u                undo
Ctrl+r           redo
i                insert before cursor
o                new line below

## Search and replace
/word            search forward
n                next match
:%s/old/new/g    replace all in file
:set number      show line numbers
