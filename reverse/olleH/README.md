# olleH
> Are you ready to dive into reverse engineering? Let’s start simple!

# 📝 writeup

Decompile `olleH` with any decompiler you have. I use BinaryNinja at [dogbolt](https://dogbolt.org/?id=2c0b57b1-2c12-4fe3-b1ac-33890e00cff4).

```c
int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    int32_t var_9f;
    __builtin_strcpy(&var_9f, "Nowruz");
    int64_t var_98;
    __builtin_memcpy(&var_98, "\x08\x22\x34\x26\x33\x01\x06\x5c\x1b\x1e\x45\x25\x3c\x5c\x01\x41\x07\x09\x7d\x30\x44\x1c\x12\x25\x7e\x17\x42\x45\x16\x07", 0x1e);
    int32_t rax_1 = strlen(&var_9f);
    printf("Enter your flag: ");
    void var_78;
    __isoc99_scanf("%99s", &var_78);
    int32_t rax_4 = strlen(&var_78);
    
    if (rax_4 == 0x1e)
    {
        for (int32_t i = 0; i < rax_4; i += 1)
            *(&var_78 + i) ^= *(&var_9f + i % rax_1);
        
        int32_t var_b4_1 = 1;
        
        for (int32_t i_1 = 0; i_1 < 0x1e; i_1 += 1)
        {
            if (*(&var_78 + i_1) != *(&var_98 + i_1))
            {
                var_b4_1 = 0;
                break;
            }
        }
        
        if (!var_b4_1)
            puts("Try again!");
        else
            puts("Victory! You found the correct f…");
    }
    else
        printf("Try again! (Flag length should b…", 0x1e);
    
    *(fsbase + 0x28);
    
    if (rax == *(fsbase + 0x28))
        return 0;
    
    __stack_chk_fail();
    /* no return */
}
```

As you can see, it XORs our input with the key `"Nowruz"` and checks it against `var_98`. If all 30 bytes match, we have found the flag and solved it.

```py
from pwn import *
expected = b"\x08\x22\x34\x26\x33\x01\x06\x5c\x1b\x1e\x45\x25\x3c\x5c\x01\x41\x07\x09\x7d\x30\x44\x1c\x12\x25\x7e\x17\x42\x45\x16\x07"
xor(expected, b'Nowruz')
```

# 🚩 Flag
> `FMCTF{H3ll0_r3v3rs3_3ng_0x57c}`
