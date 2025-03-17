import random
import time

seed = int(time.time())
flag = list("o1me0T3}h_hTuvar_M4vdCFF3__{l3TY")
random.seed(seed)
random.shuffle(flag)
flag = "".join(flag)
if "FMCTF" in flag:
    print(f"{flag = }")
else:
    print("Time lost can not be won again.")