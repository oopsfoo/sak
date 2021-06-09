import socket
import socketserver
import threading

from hexdump import hexdump 

# requirement:
#   pip install pyhexdump 

server_ip = "127.0.0.1"
server_port = 11223 

class TcpHandler(socketserver.StreamRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print('------------recv TCP pkt[RAW] -------------')
        hexdump(self.data)

class UdpHandler(socketserver.DatagramRequestHandler):
    
    def handle(self):
        print('------------recv UDP pkt[RAW] -------------')
        hexdump(self.request[0])

tcp_svr = socketserver.TCPServer((server_ip, server_port), TcpHandler)
udp_svr = socketserver.UDPServer((server_ip, server_port), UdpHandler)

tcp_thread = threading.Thread(target=tcp_svr.serve_forever)
tcp_thread.setDaemon(True);
tcp_thread.start();

udp_svr.serve_forever()
tcp_svr.shutdown()
udp_svr.shutdown()