# -*- coding: utf-8 -*-
import socket

def Main():
    host = "127.0.0.1"
    port = 5000
    s = socket.socket()
    s.connect((host,port))
    print("Please Press (q) to Exit")
    message = input("Message: ")
    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        # print("Received from server ",data)
        message = input("Message: ")
    s.close()
if __name__ == '__main__':
    Main()
