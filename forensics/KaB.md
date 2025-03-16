# KaB

This challenge is implementation of a custom made steganography algorithm  
For the first step you need to extract the needed files from the given pcap file, wireshark has a builtin feature to export transmitted file with http protocol  

The pcap file contains a document for the steganography algorithm, a `steg.png` file and a text file `key`  
You need to implement the algorithm for give it the key and `steg.png` to get the flag  

```python
import bitarray
from bitarray.util import int2ba, ba2int
from PIL import Image
from itertools import product
key_str = "Im_THE_kyE"

key_ba = bytes2list_of_ba(key_str.encode())
encoded_steg_filename = "./steg.png" 

def decode_from_image(key, carrier):
    secret_bit_list = []
    current_key_byte_index = 0
    
    #data extraction from image, will fill secret_bit_list
    for j,i in product(range(carrier.size[1]), range(carrier.size[0])):
        current_carrier_pixel= carrier.getpixel((i,j))
        current_carrier_bitarray = int2ba(current_carrier_pixel[0], length=8)

        for key_bit_index,bit_val in enumerate(key[current_key_byte_index]):
            if bit_val == 1:
                secret_bit_list.append(current_carrier_bitarray[key_bit_index])

        current_key_byte_index = (current_key_byte_index + 1) % len(key)

    result = []
    i = 0
    #turn secret_bit_list to a list of bytes so the caller can use the data without any headaches
    while i < (len(secret_bit_list) // 8):
        current_byte = (secret_bit_list[i:i+8])
        current_int = bit_list2_int(current_byte) 
        result.append(current_int)

        i += 8

    return result

secret_byte_list=decode_from_image(key_ba, Image.open(encoded_steg_filename))
for ch in secret_byte_list:
    if ch == 0:
        break
    print(chr(ch), end='')
```
