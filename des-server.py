from socket import socket, AF_INET, SOCK_STREAM
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import json
from base64 import b64decode
import time


key = b'mycustom'

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(("", 1100))
    s.listen(1)
    connection,address = s.accept()
    with connection:
        receipt = connection.recv(1024)
        utf_message = receipt.decode('utf-8')
        json_message = json.loads(utf_message)
        message = b64decode(json_message['message'])
        iv = b64decode(json_message['iv'])
        cipher = DES.new(key, DES.MODE_CBC, iv)


        start = time.time()*1000
        print(f'started at {start}')
        message_decoded = cipher.decrypt(message)

        end = time.time()*1000
        print(f'end at {end}')
        print(f'time to decript was {end-start} miliseconds')


        message_unpadded = unpad(message_decoded, 8).decode('utf-8')


        print("The message was: ", message_unpadded)
        connection.close()