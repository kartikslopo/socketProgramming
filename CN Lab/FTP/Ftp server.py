import socket

import os

port = 6000
s = socket.socket()
host = '127.0.0.1'
s.bind((host, port))
s.listen(5)


while True:
    conn, addr = s.accept()
    filename = 'cliento.txt'
    b = os.path.getsize(filename)
    f = open(filename, 'rb')
    l = f.read(b)

    while (l):
        conn.send(l)

        l = f.read(b)
    f.close()

    print('Done sending')
    conn.close()