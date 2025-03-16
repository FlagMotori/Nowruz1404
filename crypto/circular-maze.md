# circular-maze

Participants are given a encrypt script it's output for the flag  
The encrypt script replaces each byte of the input with: `input[i-1] + input[i] + input[i+1]`  

Since the flag format is `FMCTF{}`, the participant can safely assume `flag[0-5]` and `flag[len - 1]`  
Knowing this information, 6th byte of the flag can be extracted by `input[6] - input [5] - input[4]`  
And same for the following bytes

A thanks to [n1k4](https://github.com/mheidari98) for helping me with this challenge  
```python
flag = list(b"FM")
enc = open("./flag.enc", "rb").read()

for i in range(1, len(enc)-1):
    flag.append((enc[i]-flag[-1]-flag[-2])%256)
print(''.join(map(chr, flag)))
```
