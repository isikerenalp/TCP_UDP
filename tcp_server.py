# -*- coding: utf-8 -*-
import socket

def Main():
    host = "127.0.0.1"
    port = 5000
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    c, addr = s.accept() # client & address
    print("Connection from: ",str(addr))
    while "TRUE":
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("Sending: ",str(data))
        c.send(data.encode('utf-8'))
    c.close()
if __name__ == '__main__':
    Main()
