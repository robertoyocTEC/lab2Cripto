from socket import socket, AF_INET, SOCK_STREAM
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time


with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(("", 1100))
    s.listen(1)
    connection,address = s.accept()
    with connection:
        receipt = connection.recv(1024)
        private_key = RSA.import_key(open("11.0-RSA/keys/private.pem").read())

        cipher_rsa = PKCS1_OAEP.new(private_key)

        start = time.time()*1000
        print(f'started at {start}')
        message_decoded = cipher_rsa.decrypt(receipt)

        end = time.time()*1000
        print(f'end at {end}')
        print(f'time to decript was {end-start} miliseconds')


        print("The message was: ", message_decoded.decode('utf-8'))
        connection.close()