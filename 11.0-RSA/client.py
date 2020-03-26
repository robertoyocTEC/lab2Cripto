from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from socket import socket, SOCK_STREAM, AF_INET
import time


message = b"hola como estas soy roberto"

recipient_key = RSA.import_key(open("11.0-RSA/keys/public.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)


start = time.time() * 1000
print(f'started at {start}')

encripted = cipher_rsa.encrypt(message)

end = time.time() * 1000

print(f'end at {end}')

print(f'time to encript was {end-start} miliseconds')

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(("192.168.0.6", 1100))
    data = s.send(encripted)
    s.close()


