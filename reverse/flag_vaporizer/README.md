# flag_vaporizer  

This consists of a compiled rust program that checks if the given input is flag or not  
this program works by checking if  it's equations are satisfied or not, which can be extracted by decompiling the program  
Finaly, an automated solver can be used to get the flag  

```python
from z3 import *

l = [BitVec(f'l{i}', 32) for i in range(40)] #xor is not supported for Int class
s = Solver()

s.add(l[0] + 55 == l[39])
s.add(l[0] + 31 == l[38])
s.add(l[2] + 30 == l[35])
s.add(l[4] * 2 == l[20] + 29)
s.add(l[17] - 25 == l[0])
s.add(l[32] + 7 == l[39])
s.add(l[28] / 2 == l[16] - 54)
s.add(l[9] == l[25] - 10)
s.add(l[1] + l[10] - l[20] == l[36] - 31)
s.add(l[2] - l[12] + l[0] == 42)
s.add(l[3] - l[12] + l[22] == 104)
s.add(l[4] - l[12] + l[23] == l[22] - 45)
s.add(l[5] + l[10] + l[4] - l[11] == 184)
s.add(l[5] + l[9] - l[0] == l[3] + 76)
s.add(l[22] - l[12] + l[35] - l[0] == 47)
s.add(l[22] - l[11] + l[2] == l[0] + 2)
s.add(l[23] - l[22] + l[10] == 81)
s.add(l[36] + l[10] + l[11] - l[38] == 208)
s.add(l[7] + l[6] + l[17] - l[0] == 237)
s.add(l[10] + l[38] - l[9] == 95)
s.add(l[20] + l[4] - l[8] == 70)
s.add(l[11] + l[38] - l[22] + l[7] == l[21] + 101)
s.add(l[21] + l[33] + l[0] == 276)
s.add(l[33] + l[32] + l[39] == l[8] + l[10] + 128)
s.add(l[19] + l[12] + l[17] - l[38] == 205)
s.add(l[18] + l[36] + l[0] - l[22] == 150)
s.add(l[16] + l[22] == l[20] + 115)
s.add(l[22] - l[32] + l[13] == l[9] - 5)
s.add(l[22] ^ l[24] == 17)
s.add(l[23] ^ (l[0] + l[24]) == 247)
s.add(((l[25] + l[20]) ^ l[10]) == ((l[22] ^ l[24]) + 112))
s.add((l[26] + l[27]) ^ (l[0] + l[1]) == 64)
s.add(l[26] ^ l[7] == 6)
s.add(l[27] - l[33] + l[16] == 109)
s.add(l[28] + l[22] - l[10] == 128)
s.add(l[29] ^ l[27] == 58)
s.add(l[30] + l[15] - l[20] == 104)
s.add(l[31] ^ l[33] == 14)
s.add(l[34] - l[17] + l[13] == l[8] + 13)
s.add(l[37] + l[29] - (l[9] ^ l[39]) == 187)
s.add(l[15] + l[21] - (l[20] ^ l[10]) == 215)
s.add(l[14] + l[22] - l[38] == 124)

#each variable represents a byte, so we limit all of them to be uint8
for var in l:
    s.add(var >= 0, var < 256)
    
if s.check() == sat:
    m = s.model()
    solution = [m.evaluate(l[i]) for i in range(40)]
    for i in solution:
        print(chr(int(i.__repr__())), end='')
```
