#!/usr/bin/python
import socket
try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(("192.168.1.5",110))
	r = s.recv(1024)
	print r
	s.send("USER teste\r\n")
	r = s.recv(1024)
	print r
	s.send("PASS teste\r\n")
	r = s.recv(1024)
	print r
	s.send("QUIT\r\n")
	r = s.recv(1024)
	print r
except:
	print "Nao se conectou"
