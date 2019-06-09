import socket
s=socket.socket()
s.bind(('192.168.43.160',12345))
s.listen(5)
while(true):
    c,addr=s.accept()
    print('Got Connection from :',addr)
    t=c.recv(1024)
    c.send("We have Received your Request")
    print(t)
