import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

with open("a.png", "wb") as f:
    while message := server_socket.recv(516):
        part = int.from_bytes(message[:4])-1
        f.seek(part*512)
        f.write(message[4:])