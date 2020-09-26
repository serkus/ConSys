#-*- coding: UTF-8 -*-
#!/usr/bin/env python3
import socket

hostname = "0.0.0.0"	#sld, tld
port= 448
#thon TCP Client 
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection client
client.connect((hostname, port))

client.send('GET /index.html HTTP/1.1\r\nHost: {}.{}\r\n\r\n'.format(sld, tld))
white True:
	response = client.recv(4096)
	print response
