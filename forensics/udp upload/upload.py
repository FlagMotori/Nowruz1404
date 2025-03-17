import socket
import random

def send(file, socket: socket.socket):
    part_number = 0
    CHUNK = 512
    packets = []
    with open(file, "rb") as f:
        while c := f.read(CHUNK):
            part_number += 1
            packets.append(part_number.to_bytes(4) + c)
    random.shuffle(packets)
    for packet in packets:
        socket.send(packet)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
addr = ("127.0.0.1", 12000)
client_socket.connect(addr)
send("flag.png", client_socket)
