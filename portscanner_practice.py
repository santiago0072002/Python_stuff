import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '127.0.0.1'

def pscan(port):
	try:
		s.connect((server, port))
		return True
	except:
		return False
	
for x in range(1, 443 + 1): 
	if pscan(x):
		print("port", x, " is open")
	else:
		print("port", x , " is closed")