from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from socket import socket, SOCK_STREAM, AF_INET


key = b'mycustom'

message = 'hola como estas soy roberto'
data = message.encode('ascii')

cipher = DES.new(key, DES.MODE_CBC)

padded_message = pad(data, 8)

encripted = cipher.encrypt(padded_message)

send = {
    'message': encripted,
    'iv': cipher.iv
}

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(("192.168.0.2", 1100))
    data = s.send(send)
    s.close()
