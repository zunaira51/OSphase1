import socket               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 8667               # Reserve a port for your service.
s.connect((host, port))
while True: 
	message=raw_input("Enter message: ")
	if message=="end":
		s.close()
		break
	s.send(message)
	data=s.recv(1024)
	print data
  
