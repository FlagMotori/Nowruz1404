# EZ XOR

> Welcome to your first crypto challenge! 🕵️‍♂️    
> This one is all about XOR, one of the simplest yet most widely used operations in cryptography. Can you uncover the hidden flag?

## 📝 writeup

```python
from pwn import *
encryptedFlag = "a850d725cb56b0de4fcb40de72a4df56a72ec06cafa75ecb41f51c95"
s = bytes.fromhex(encryptedFlag)
secret = xor(b'FMCTF{', s[:6]) + xor(b'}', s[-1])
print(xor(s, secret))
```


## 🚩 Flag
> `FMCTF{X0R_1S_L1K3_MAGIC_0x1}`

