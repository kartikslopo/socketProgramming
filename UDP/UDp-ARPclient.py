import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hos=socket.gethostname()
print(hos)
port=6969
h2=socket.gethostbyname(hos)
print(h2)
msg=input("Enter the IP address : ")
s.sendto(msg.encode(),(hos,port))