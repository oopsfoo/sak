import socks
import socket
import dnslib

# requirement:
#   pip install dnslib 
#   pip install pysocks
remote_ip = "8.8.8.8"
remote_port = 53
proxy_ip = "127.0.0.1"
proxy_port = 11223
qname="www.google.com"

pkt = dnslib.DNSRecord.question(qname).pack()
print('----------- this is request[RAW] -----------')
print(pkt)

skt = socks.socksocket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
skt.set_proxy(socks.SOCKS5, proxy_ip, proxy_port)

bytes_send = skt.sendto(pkt, (remote_ip, remote_port))

max_bytes = 4096
(response,src_addr) = skt.recvfrom(max_bytes)

print('----------- this is response[RAW] -----------')
print(response)
print('----------- this is response[decoded] -----------')
print(dnslib.DNSRecord.parse(response))
skt.close()
