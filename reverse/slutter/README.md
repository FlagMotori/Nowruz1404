`strings data/flutter_assets/kernel_blob.bin|grep "flag = \[" -A 40`

```py
flag = [
    70,
    77,
    67,
    84,
    70,
    123,
    100,
    49,
    68,
    95,
    121,
    48,
    117,
    95,
    117,
    53,
    51,
    95,
    56,
    108,
    117,
    55,
    55,
    51,
    82,
    95,
    48,
    82,
    95,
    119,
    104,
    52,
    55,
    63,
    125
]
print("".join([chr(i) for i in flag]))
```

Flag: `FMCTF{d1D_y0u_u53_8lu773R_0R_wh47?}`