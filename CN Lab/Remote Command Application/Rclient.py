import socket
import sys
import subprocess
s=socket.socket()
host=socket.gethostname()
port=1234
s.connect((host,port))
message=input("Enter Command :")
s.send(message.encode())
while True:
    data=s.recv(1024).decode()
    print("server",data)
    if data=="exit" or not data:
        print("Client exiting")
        break
    msg=input("enter client message:")
    s.send(msg.encode())
s.close()