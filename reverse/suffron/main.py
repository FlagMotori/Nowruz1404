import random
import time

seed = int(time.time())
flag = list("FMCTF{0h_You_h4v3_Trav3led_T1m3}")
mapp = [chr(i) for i in range(len(flag))]
random.seed(seed)
random.shuffle(mapp)
mapp = list(map(ord, mapp))
result = flag.copy()
for i in range(len(mapp)):
    result[mapp[i]] = flag[i]
print(f"{seed = }")
print(f"{flag = }")
print(f"{result = }")