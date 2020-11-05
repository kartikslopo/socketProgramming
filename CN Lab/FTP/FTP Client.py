import socket
import os

s = socket.socket()
host = '127.0.0.1'
port = 6000
s.connect((host, port))

with open('received_file1', 'wb') as f:
    while True:

        data = s.recv(1024)

        f.write(data)

        if not data:
            break


    d = os.path.getsize('received_file1')
print(data)
print(d)
f.close()
print('Successfully received the file')
s.close()
print('connection closed')