from socket import *
from time import ctime

HOST = 'localhost'
PORT = 7777
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcp = socket(AF_INET, SOCK_STREAM)
tcp.bind(ADDR)
tcp.listen(5)

while True:
	print 'waiting for client connection..'
	tcpClient, addr = tcp.accept()
	print '...connected from ', addr

	while True:
		data = tcpClient.recv(BUFSIZ)

		if not data:
			break

		tcpClient.send('time: ' + ctime() + ', data: ' + data)

	tcpClient.close()

tcp.close()