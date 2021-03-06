from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from socket import socket, SOCK_STREAM, AF_INET
import json
import time

key = b'mycustom16bytesk'

iv = b'cipheriv16bytesl'

message = b'hola como estas soy roberto'

cipher = AES.new(key, AES.MODE_CBC, iv=iv)

padded_message = pad(message, 16)

start = time.time() * 1000
print(f'started at {start}')
encripted = cipher.encrypt(padded_message)

end = time.time() * 1000

print(f'end at {end}')

print(f'time to encript was {end-start} miliseconds')

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(("192.168.0.6", 1100))
    data = s.send(encripted)
    s.close()


