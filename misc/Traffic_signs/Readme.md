To solve this steganography challenge, you need to consider three things about this traffic sign:

1- The first letter of three words refer to LSB, which is a common method in steganography.

2- The UTurn means that the extraction method reverse way. (From the last to the first pixel).

3- The green color of the sign refers to the green channel of the RGB image.

So we need to extract the LSB bits of the green channel of the image in a reverse way.

```py

from PIL import Image

image_path = "stego.png"
img = Image.open(image_path)
img = img.convert("RGB")

width, height = img.size
pixels = img.load()
green_channel = [pixels[x, y][1] for y in range(height) for x in range(width)]
green_channel.reverse() # Reverse green channel values

binary_data = ''.join([str(g & 1) for g in green_channel])  # Extract the LSB of G pixels
chars = []
for i in range(0, len(binary_data), 8):
    byte = binary_data[i:i+8]
    char = chr(int(byte, 2))
    if char == '\x00':  # Null byte signifies end of message
        break
    chars.append(char)
extracted_msg = ''.join(chars)
print('Extracted Message:', extracted_msg)
```

flag: `FMCTF{Tr4ff1c_5i9ns_Gu1de_7h3_5teg0_Hunt3rs}`
