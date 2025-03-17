Solve:

```bash
binwalk -e a.bin; ls _a*|grep -v zlib|xargs -I{} bash -c "cat _a*/{};echo"|sort|uniq
```

Flag: `FMCTF{8Inw4lK_3x7R4c7_L2m4_4U70m47ic4lLy!!}`