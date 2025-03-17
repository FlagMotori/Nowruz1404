from scapy.all import *
pcap = rdpcap("chall.pcapng")
i = 1
flag_file = open("flag.png", "wb")

cnt = {}

for i in range(len(pcap)):
    cnt.update({pcap[i][UDP].load[3] : i})

for i in range(len(cnt) + 1):
    try:
        flag_file.write(
                pcap[cnt[i]].load[4:]
                )
    except:
        pass
