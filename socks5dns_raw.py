import socket
import struct
import dnslib

# requirement:
#   pip install dnslib 
#   pip install pysocks

# this function without socks5 tcp 
remote_ip = "8.8.8.8"
remote_port = 53
proxy_ip = "192.168.1.140"
proxy_port = 11223
qname="www.google.com"

pkt = dnslib.DNSRecord.question(qname).pack()
print('----------- this is request[RAW] -----------')
print(pkt)

pre_header = bytearray(b'\x00\x00\x00\x01')
send_pkt = pre_header + bytearray(map(int, remote_ip.split('.'))) + struct.pack(">H", 53) + pkt
print('----------- this is full request[RAW] -----------')
print(send_pkt)

skt = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

bytes_send = skt.sendto(send_pkt, (remote_ip, remote_port))

max_bytes = 4096
(response,src_addr) = skt.recvfrom(max_bytes)

print('----------- this is response[RAW] -----------')
print(response)
print('----------- this is response[decoded] -----------')
print(dnslib.DNSRecord.parse(response))
skt.close()
