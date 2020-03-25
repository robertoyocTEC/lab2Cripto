import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.2", 1100))
data=s.send(b'holas')
s.close()
print('finished')