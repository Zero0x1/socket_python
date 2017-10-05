import socket
import sys

s = socket.socket();

s.connect((sys.argv[1], 80))
s.send("GET / HTTP/1.1\r\nHost: {sys.argv[1]}\r\nConnection: close\r\n\r\n")

data = s.recv(10000)
s.close()

print data
