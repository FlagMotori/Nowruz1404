# Robin’s Mystery
> Robin’s friend used an unusual RSA setup, and now he can’t decrypt his own message!  
> Can you step in and use a special technique to recover the plaintext?

# 📝 writeup

```python
import gmpy2
from Crypto.PublicKey import RSA
from Crypto.Util.number import *

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def sqrt(c):
    g ,yp, yq = egcd(p,q)
    mp = pow(c, (p+1)//4, p)
    mq = pow(c, (q+1)//4, q)
    r = (yp*p*mq + yq*q*mp) % n
    mr = n - r
    s = (yp*p*mq - yq*q*mp) % n
    ms = n - s
    return [r,mr,s,ms]

exportKey = """
-----BEGIN PUBLIC KEY-----
MIGcMA0GCSqGSIb3DQEBAQUAA4GKADCBhgKBgGjpRi/Hr5oN5NS219dZrq6nW7AC
Y7fUItXAvbgy0TtagVKO2goQiOssL331b7zRjMvdHkEBR4bTd+hHblmynO+2//fz
4DmVgdgMnrP54+2RSzguEGS1ONX4MpJonBsEGGc1IOiKECiwIbl4DkyTxl6AnFsz
ZI2E+lLDZnX5P44FAgEQ
-----END PUBLIC KEY-----
"""

c = b'\x10\xc4\xbf\xfapg\xee\x00\xe4\xcd\x00\xb4i\xf5\x801\xdd\xafm\xb1\xad\x8dy\x01\xaa\x14\xd1\xa3\x14[\xdf\xc8c\xb1\xf4\xcb\xcf\xf0\xf9\x83\x85%\x19\xd2d>N\x9aR\xa4\xba\xc9\xda\xd8\xe4\xa2\x9cg%.\xac\xd7\xb5\x95\x7f\x87\x04?\xf7\xe4\x06(\xe7l\x1c"c\x95\x90z\xd4\x8b\x9f\x1b\x00\xc67\xe4\x82g\xc4b\x10\x8c\xe7s[\x95-TB+Z;\xe4\x00\x11<\xc51K\xec\x94ZL\xb2\xf9\x7fp<\xe6C\xf8\x7f\x90\x0bG\xcf'
c = bytes_to_long(c)

rsa = RSA.import_key( exportKey.strip() )
n, e = rsa.n, rsa.e

sq,b = gmpy2.iroot(n,2)
while n%sq != 0:
    sq += 1
q = int(sq)
p = n // q
assert(p * q == n)

Found = False
for c1 in sqrt(c):
    for c2 in sqrt(c1):
        for c3 in sqrt(c2):
            for c4 in sqrt(c3):
                if (res := long_to_bytes(c4)).startswith(b'FMCTF'):
                    print(res)
                    Found = True
            if Found:
                break
        if Found:
            break
    if Found:
        break
```

# 🚩 Flag
> `FMCTF{S0lv3d_w1th_R4b1n_fx777}`
