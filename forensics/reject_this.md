# reject_this

The point for this challenge was for the participants to realize that data can be hidden by using the TCP initial sequence number, since it's chosen "randomly" by each end of the connection

In this case, a png file was transmitted from `192.168.1.36` to `172.17.0.2`  
It can be extracted with the following script:

```python
from scapy.all import *
dest_port = 80

packets = rdpcap("./reject_this.pcapng")

secret = bytearray()

for packet in packets:
    if TCP not in packet:
        continue
    if packet[TCP].dport != dest_port:
        continue
    if packet[TCP].flags != "S":
        continue
    if packet[TCP].ack != 0:
        continue

    current_payload =  packet[TCP].seq.to_bytes(length = 4)
    secret.extend(current_payload)


open("./file.png", "wb").write(secret)
```
