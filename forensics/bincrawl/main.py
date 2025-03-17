import zlib
import random
flags = ["FMCTF{Not_ThiS}", "FMCTF{ArE_y0U_Sur3?}", "FMCTF{I_Dont_thINk_s0}"]
flag = "FMCTF{8Inw4lK_3x7R4c7_L2m4_4U70m47ic4lLy!!}"
with open("a.bin", "wb") as f:
    for i in range(0x100):
        text = random.choice(flags)
        if i == 0x77:
            text = flag
        f.write(zlib.compress(text.encode()))