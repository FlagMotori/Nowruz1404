from sage.all import *
from pwn import *

def add(c1, c2): 
    Zn2 = IntegerModRing(n**2)
    while True:
        r = randint(1, n-1)
        if gcd(r, n) == 1:
            break
    return c1 * c2 * Zn2(r)**n

def sub(c1, c2):

    Zn2 = IntegerModRing(n**2)
    while True:
        r = randint(1, n-1)
        if gcd(r, n) == 1:
            break
    inv_c2 = Zn2(c2)**(-1)
    return c1 * inv_c2 * Zn2(r)**n


r=remote('seal-the-deal.fmc.tf 2003',2003)

print(r.recvline())
n,g = r.recvline().decode()[8:-2].split(',')
n=int(n)
g=int(g.strip())
ciphers=[int(r.recvline()[4:-1]) for i in range(4)]

add_c12=add(ciphers[0],ciphers[1])
sub_c34=sub(ciphers[2],ciphers[3])
add_c1234 = str(add(add_c12,sub_c34))

print(r.recv().decode())
r.sendline(add_c1234.encode())
print(r.recv().decode())