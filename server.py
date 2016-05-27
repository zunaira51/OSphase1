
import socket
import sys
from thread import *

HOST = ''
PORT = 8277
arr=[]
i=0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'


try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'


s.listen(10)
print 'Socket now listening'


# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n')

    while True:
        # Receiving from client
        data = conn.recv(1024)
        reply =  data
        if not data:
            break

        if conn == arr[0]:
            arr[1].sendall(reply)
        else:
            arr[0].sendall(reply)

    # came out of loop
    conn.close()

# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    arr.append(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn,))
    i+=1
s.close()

