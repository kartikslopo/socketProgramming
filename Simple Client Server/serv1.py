import socket

s=socket.socket()

s.bind(("Localhost",9999))
s.listen(5)
print("Waiting...")

while True:
    c,addr=s.accept()

    n=c.recv(1024).decode()
    print("Connected with",addr,n)
    p=input("Enter Message:")
    c.send(bytes(p,'utf-8'))

    c.close()