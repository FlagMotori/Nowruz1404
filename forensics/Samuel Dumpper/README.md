Solve:

```bash
secretsdump.py -sam sam -system system LOCAL|grep ss > hash.txt
hashcat hash.txt /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

Flag: `FMCTF{babigurl1}`