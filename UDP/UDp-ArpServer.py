import socket
import subprocess

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host=socket.gethostname()
port=6969
s.bind((host,port))

while True:
    print("Waiting for Client !")
    data,addr=s.recvfrom(1024)
    com="arp -a" + str(data.decode())
    p=subprocess.run(com,capture_output=True,shell=True)
    print(p.stdout)

