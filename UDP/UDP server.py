import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('localhost',12345))

while True:
    data,addr=sock.recvfrom(4096)
    print(str(data))
    message=bytes(('Hello this is UDP SERVER !').encode('utf-8'))
    sock.sendto(message,addr)


