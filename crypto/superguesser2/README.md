# superguesser v2
> Superguesser is back with a vengeance!  
> ```nc superguesser.fmc.tf 2002```

# 📝 writeup

This solution is based on the techniques described in [Breaking Python's PRNG with a few values and no bruteforce](https://stackered.com/blog/python-random-prediction/).

Used this script to find the seed for superguesser v2: [recover_BytesV2Seed.py](https://github.com/StackeredSAS/python-random-playground/blob/main/recover_BytesV2Seed.py)

```python
from pwn import *
from functions import invertStep, untemper, recover_Kj_from_Ii
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def get(idx):
    p.sendlineafter(b'): ', f'{idx}'.encode())
    return int(p.recvline().split()[-1])

p = remote(*'superguesser.fmc.tf 2002'.split())
p.recvuntil(b'flag: \n')
enc = bytes.fromhex(p.recvline().decode())

I_230_, I_231 = invertStep(untemper(get(3)), untemper(get(230)))
I_231_, I_232 = invertStep(untemper(get(4)), untemper(get(231)))
I_232_, I_233 = invertStep(untemper(get(5)), untemper(get(232)))
I_233_, I_234 = invertStep(untemper(get(6)), untemper(get(233)))
I_231 += I_231_
I_232 += I_232_
I_233 += I_233_
seed_l = recover_Kj_from_Ii(I_233, I_232, I_231, 233) - 16
seed_h1 = recover_Kj_from_Ii(I_234, I_233, I_232, 234) - 17
seed_h2 = recover_Kj_from_Ii(I_234+0x80000000, I_233, I_232, 234) - 17

seed = ((seed_h1 << 32) + seed_l).to_bytes(8)
random.seed(seed)
if random.getrandbits(32) != get(0):
    seed = ((seed_h2 << 32) + seed_l).to_bytes(8)

random.seed(seed)
_ = [random.getrandbits(32) for _ in range(624)]

key = random.getrandbits(128).to_bytes(16, 'big')
cipher = AES.new(key, AES.MODE_CBC, seed*2)
flag = unpad(cipher.decrypt(enc),AES.block_size).decode()
print(f'flag= {flag}')
```

# 🚩 Flag

> `FMCTF{V2_MT19937_S33d_Unc0v3r3d}`

