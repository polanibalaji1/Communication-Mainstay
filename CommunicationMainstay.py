import socket
s=socket.socket()
s.bind(('192.168.43.160',12345))    #Use the IP address of your system after connecting to WIFI / Hotspot
s.listen(5)
while(true):
    c,addr=s.accept()
    print('Got Connection from :',addr)
    t=c.recv(1024)
    c.send("We have Received your Request")
    print(t)
