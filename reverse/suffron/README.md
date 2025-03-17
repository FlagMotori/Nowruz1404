use https://pylingual.io to reverse pyc to py

```py
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ./chall.py
# Bytecode version: 3.13.0rc3 (3571)
# Source timestamp: 2025-03-15 15:42:49 UTC (1742053369)

import random
import time
seed = int(time.time())
flag = list('o1me0T3}h_hTuvar_M4vdCFF3__{l3TY')
random.seed(seed)
random.shuffle(flag)
flag = ''.join(flag)
if 'FMCTF' in flag:
    print(f'flag = {flag!r}')
```

and make this changes

```py
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ./chall.py
# Bytecode version: 3.13.0rc3 (3571)
# Source timestamp: 2025-03-15 15:42:49 UTC (1742053369)

import random
import time
for i in range(int(time.time()) - 1000000, int(time.time())):
    seed = i
    flag = list('o1me0T3}h_hTuvar_M4vdCFF3__{l3TY')
    random.seed(seed)
    random.shuffle(flag)
    flag = ''.join(flag)
    if 'FMCTF' in flag:
        print(f'flag = {flag!r}')
```

Flag: `FMCTF{0h_You_h4v3_Trav3led_T1m3}`