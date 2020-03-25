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

        start = time.time()
        print(f'started at {start}')
        message_decoded = unpad(cipher.decrypt(message), 8).decode('utf-8')

        end = time.time()
        print(f'end at {end}')
        print(f'time to encript was {end-start} seconds')


        print("The message was: ", message_decoded)
        connection.close()