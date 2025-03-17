import bitarray
from bitarray.util import int2ba, ba2int
from PIL import Image
from itertools import product

def bytes2list_of_ba(byte_list):
    result = [] 
    for byte in byte_list:
        result.append(int2ba(byte, length=8))

    return result

secret_str = "FMCTF{haha_ypu_unlocked_bitmap}"
key_str = "Im_THE_kyE"

secret_ba = bytes2list_of_ba(secret_str.encode())
key_ba = bytes2list_of_ba(key_str.encode())

carrier_filename = "./img_1739540471044.jpeg"
carrier = Image.open(carrier_filename)

encoded_steg_filename = "./steg.png" #to avoid corruption of flag

def encode_to_image(key, carrier, secret):
    current_secret_offset = 0
    current_key_byte_index = 0
    for j,i in product(range(carrier.size[1]), range(carrier.size[0])):
        current_carrier_pixel= carrier.getpixel((i,j))
        current_carrier_bitarray = int2ba(current_carrier_pixel[0], length=8)

        print(f"{current_carrier_bitarray} ->", end='')
        for key_bit_index,bit_val in enumerate(key[current_key_byte_index]):
            if bit_val == 1:

                encode_bit = 0
                if current_secret_offset < len(secret) * 8:
                    encode_bit = secret[current_secret_offset // 8][current_secret_offset % 8]

                current_carrier_bitarray[key_bit_index] = encode_bit

                #print(f"encoded {encode_bit} to carrier pixel {i},{j} and bit pos of {key_bit_index}, used {current_key_byte_index}th key byte")
                current_secret_offset += 1
            #end of loop inside key

        print(f"{current_carrier_bitarray} pixel pos {i},{j}")
        pixel_to_encode = (
                ba2int(current_carrier_bitarray),
                current_carrier_pixel[1],
                current_carrier_pixel[2]
                )
        carrier.putpixel((i,j), pixel_to_encode)
        current_key_byte_index = (current_key_byte_index + 1) % len(key)

    #end of loop inside carrier

    return carrier


def bit_list2_int(bl):
    tmp_ba = bitarray.bitarray('0' * 8)
    for i,bit in enumerate(bl):
        if bit:
            tmp_ba[i] = 1

    return ba2int(tmp_ba)


def decode_from_image(key, carrier):
    secret_bit_list = []
    current_key_byte_index = 0
    for j,i in product(range(carrier.size[1]), range(carrier.size[0])):
        current_carrier_pixel= carrier.getpixel((i,j))
        current_carrier_bitarray = int2ba(current_carrier_pixel[0], length=8)

        for key_bit_index,bit_val in enumerate(key[current_key_byte_index]):
            if bit_val == 1:
                secret_bit_list.append(current_carrier_bitarray[key_bit_index])

        current_key_byte_index = (current_key_byte_index + 1) % len(key)

    result = []
    i = 0
    while i < (len(secret_bit_list) // 8):
        current_byte = (secret_bit_list[i:i+8])
        current_int = bit_list2_int(current_byte) 
        result.append(current_int)

        i += 8

    return result


encoded_carrier = encode_to_image(key_ba, carrier, secret_ba)
carrier.save(encoded_steg_filename)
