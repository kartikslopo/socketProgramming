import socket
c=socket.socket()

c.connect(('localhost',9999))
n=input("Enter Name:")
c.send(bytes(n,'utf-8'))
print(c.recv(1024).decode())