from socket import *
from threading import Thread
import sys

HOST = 'localhost'
PORT = 8277
ADDR = (HOST, PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)

def recv():
    while True:
        data = s.recv(1024)
        if not data: sys.exit(0)
        print data

Thread(target=recv).start()
while True:
    data = raw_input('Enter: ')
    s.send(data)

s.close()
