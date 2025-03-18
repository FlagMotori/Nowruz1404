# EZ RSA

> Do you know RSA? Let’s do some basic math and find the flag!

# 📝 writeup

```python
from Crypto.Util.number import *
phi = n-hint+1 # (p-1)*(q-1) = p*q - (p+q) + 1
d = pow(65537, -1, phi)
print(long_to_bytes(pow(c, d, n)))
```


# 🚩 Flag

> `FMCTF{rSA_34SY_P34SY_L3M0N_5QU33ZY}`
