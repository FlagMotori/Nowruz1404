import hmac
import uuid
import json
import base64
import binascii
import ipaddress
from io import BytesIO
from scapy.all import *
from scapy.layers.inet import TCP
from hashlib import sha256, md5, shake_128
from Crypto.Cipher import AES
from cryptography.hazmat.primitives.ciphers import aead, Cipher, modes, algorithms

vless_pcap = rdpcap("./vless.pcapng")
vmess_pcap = rdpcap("./vmess.pcapng")
vless_packets = []
vmess_packets = {"in": [], "out": []}
for i in range(len(vless_pcap)):
    try:
        vless_packets.append(BytesIO(vless_pcap[i][TCP].load))
    except:
        pass

for i in range(len(vmess_pcap)):
    try:
        a: TCP = vmess_pcap[i][TCP]
        vmess_packets["out" if a.fields["sport"] < 32768 else "in"].append(
            vmess_pcap[i][TCP].load
        )
    except:
        pass

vmess_packets["out"] = BytesIO(b"".join(vmess_packets["out"]))
vmess_packets["in"] = BytesIO(b"".join(vmess_packets["in"]))


def vless(packet: BytesIO):
    packet.read(1)  # version
    u = uuid.UUID(bytes=packet.read(16))  # uuid
    packet.read(int.from_bytes(packet.read(1)))  # p
    packet.read(1)  # command
    port = int.from_bytes(packet.read(2))  # port
    addr_type = int.from_bytes(packet.read(1))  # addr type
    if addr_type == 1:
        addr = ipaddress.ip_address(int.from_bytes(packet.read(4)))
    elif addr_type == 2:
        addr = int.from_bytes(packet.read(16))
    elif addr_type == 3:
        addr = int.from_bytes(packet.read(int.from_bytes(packet.read(1))))
    print("VLESS: FMCTF{{{}_{}}}".format(addr, u))
    return u


KDFSaltConstAuthIDEncryptionKey = b"AES Auth ID Encryption"
KDFSaltConstAEADRespHeaderLenKey = b"AEAD Resp Header Len Key"
KDFSaltConstAEADRespHeaderLenIV = b"AEAD Resp Header Len IV"
KDFSaltConstAEADRespHeaderPayloadKey = b"AEAD Resp Header Key"
KDFSaltConstAEADRespHeaderPayloadIV = b"AEAD Resp Header IV"
KDFSaltConstVMessAEADKDF = b"VMess AEAD KDF"
KDFSaltConstVMessHeaderPayloadAEADKey = b"VMess Header AEAD Key"
KDFSaltConstVMessHeaderPayloadAEADIV = b"VMess Header AEAD Nonce"
KDFSaltConstVMessHeaderPayloadLengthAEADKey = b"VMess Header AEAD Key_Length"
KDFSaltConstVMessHeaderPayloadLengthAEADIV = b"VMess Header AEAD Nonce_Length"


def kdf(*args):
    if len(args) == 0:
        return lambda x=b"": hmac.new(KDFSaltConstVMessAEADKDF, x, "sha256")
    else:
        return lambda x=b"": hmac.new(args[-1], x, kdf(*args[:-1]))


def vmess(packets: dict[BytesIO]):
    key = md5(u.bytes + b"c48619fe-8f02-49e0-b9e9-edf763e17e21").digest()
    auth, headerLen, nonce = (
        packets["in"].read(16),
        packets["in"].read(18),
        packets["in"].read(8),
    )
    decrypt = Cipher(
        algorithms.AES(kdf(KDFSaltConstAuthIDEncryptionKey)(key).digest()[:16]),
        modes.ECB(),
    ).decryptor()
    auth_bytes = decrypt.update(auth) + decrypt.finalize()
    lengthkey = kdf(KDFSaltConstVMessHeaderPayloadLengthAEADKey, auth, nonce)(
        key
    ).digest()[:16]
    lengthnonce = kdf(KDFSaltConstVMessHeaderPayloadLengthAEADIV, auth, nonce)(
        key
    ).digest()[:12]
    headerLen = aead.AESGCM(lengthkey).decrypt(lengthnonce, headerLen, auth)
    headerLen = struct.unpack(">h", headerLen)
    headerkey = kdf(KDFSaltConstVMessHeaderPayloadAEADKey, auth, nonce)(key).digest()[
        :16
    ]
    headernonce = kdf(KDFSaltConstVMessHeaderPayloadAEADIV, auth, nonce)(key).digest()[
        :12
    ]
    req = aead.AESGCM(headerkey).decrypt(
        headernonce, packets["in"].read(headerLen[0] + 16), auth
    )
    version, iv, key, rv, option, p, res, cmd, port, type, addr, _ = struct.unpack(
        f"!B16s16sBBBBBHBi{int(headerLen[0]) - (1 + 16 + 16 + 7 + 1 + 4)}s", req
    )
    s = shake_128(iv)
    c = 0
    b_iv = bytearray(iv)
    while l := packets["in"].read(2):
        ss = s.digest((c+1) * 2)
        data = packets["in"].read(int.from_bytes(l) ^ ((ss[-2] << 8) + ss[-1]))
        b_iv[:2] = c.to_bytes(2)
        print("SEND", aead.AESGCM(key).decrypt(b_iv[:12], data, None))
        c += 1
    res_key, res_iv = sha256(key).digest()[:16], sha256(iv).digest()[:16]
    headerlenkey = kdf(KDFSaltConstAEADRespHeaderLenKey)(res_key).digest()[:16]
    headerlennonce = kdf(KDFSaltConstAEADRespHeaderLenIV)(res_iv).digest()[:12]
    headerlen = struct.unpack(
        ">h",
        aead.AESGCM(headerlenkey).decrypt(
            headerlennonce, packets["out"].read(18), None
        ),
    )
    headerkey = kdf(KDFSaltConstAEADRespHeaderPayloadKey)(res_key).digest()[:16]
    headernonce = kdf(KDFSaltConstAEADRespHeaderPayloadIV)(res_iv).digest()[:12]
    rv, opt, p = struct.unpack(
        "BB2s",
        aead.AESGCM(headerkey).decrypt(
            headernonce, packets["out"].read(headerlen[0] + 16), None
        ),
    )
    s = shake_128(res_iv)
    c = 0
    b_iv = bytearray(res_iv)
    while l := packets["out"].read(2):
        ss = s.digest((c+1) * 2)
        data = packets["out"].read(int.from_bytes(l) ^ ((ss[-2] << 8) + ss[-1]))
        b_iv[:2] = c.to_bytes(2)
        print("RECV", aead.AESGCM(res_key).decrypt(b_iv[:12], data, None))
        c += 1

u = vless(vless_packets[0])
vmess(vmess_packets)
