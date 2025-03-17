flag = "FMCTF{broken_circle_is_not_fun_at_all}"


def enc(data : str):
    result = []
    for i in range(len(data)):
        result.append(
                    (
                        (
                            ord(data[i - 1]) +
                            ord(data[i]) + 
                        ord(data[(i + 1) % len(data)])
                     ) % 256)
                        .to_bytes() 
                )
                
    return b''.join(result)
print(enc(flag))
open("./flag.enc", "wb").write(enc(flag))
