from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
import json

key = b'mycustom'

message = 'hola como estas soy roberto'
data = message.encode('ascii')

cipher = DES.new(key, DES.MODE_CBC)

padded_message = pad(data, 8)

encripted = cipher.encrypt(padded_message)

cipher_iv = cipher.iv

container = {
    'message': message,
    'iv': cipher_iv
}


send_encoded = b64encode(json.dumps(container))

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(("192.168.0.10", 1100))
    data = s.send(send_encoded)
    s.close()
