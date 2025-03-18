# superGuesser

> A little guessing, a little crypto. Can you uncover the hidden message?  
> ```nc superguesser.fmc.tf 2001```

# 📝 writeup

```python
# pip install --upgrade pwntools pycryptodome git+https://github.com/tna0y/Python-random-module-cracker@master
from pwn import *
from randcrack import RandCrack
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def get(idx):
    p.sendlineafter(b'): ', f'{idx}'.encode())
    return int(p.recvline().split()[-1])

p = remote(*'superguesser.fmc.tf 2001'.split())
p.recvuntil(b'flag: \n')
enc = bytes.fromhex(p.recvline().decode())

cracker = RandCrack()
for i in range(624):
    cracker.submit(get(i))

cracker.offset(-624)
cracker.offset(-8)
key = cracker.predict_getrandbits(128).to_bytes(16, 'big')
iv = cracker.predict_getrandbits(128).to_bytes(16, 'big')
cipher = AES.new(key, AES.MODE_CBC, iv)
flag = unpad(cipher.decrypt(enc),AES.block_size).decode()
print(f'flag= {flag}')
```


# 🚩 Flag
> `FMCTF{8a78dcb8e926e99a802261bc282aa3af}`
