from socket import socket, AF_INET, SOCK_STREAM
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import json
from base64 import b64decode
import time

key = b'mycustom16bytesk'

iv = b'cipheriv16bytesl'

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(("", 1100))
    s.listen(1)
    connection,address = s.accept()
    with connection:
        receipt = connection.recv(1024)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        start = time.time()*1000
        print(f'started at {start}')
        message_decoded = cipher.decrypt(receipt)

        end = time.time()*1000
        print(f'end at {end}')
        print(f'time to decript was {end-start} miliseconds')


        message_unpadded = unpad(message_decoded, 8).decode('utf-8')


        print("The message was: ", message_unpadded)
        connection.close()