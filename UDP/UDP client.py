import socket
c_sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg="Hello Server, Client here !"
c_sock.sendto(msg.encode('utf-8'),('localhost',12345))
data,addr=c_sock.recvfrom(4096)
print('Server Says : ')
print(str(data))
c_sock.close()