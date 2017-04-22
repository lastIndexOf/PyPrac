from socket import *

HOST = 'localhost'
PORT = 7777
ADDR = (HOST, PORT)
BUFSIZ = 1024

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)

while True:
	data = raw_input('> ')

	if not data:
		break

	client.send(data)
	data = client.recv(BUFSIZ)
	
	if not data:
		break

	print data

client.close()