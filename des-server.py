from socket import socket, AF_INET, SOCK_STREAM
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import json



key = b'mycustom'

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(("", 1100))
    s.listen(1)
    connection,address = s.accept()
    with connection:
        receipt = connection.recv(1024)
        a = json.loads(receipt)
        
        cipher = DES.new(key, DES.MODE_CBC, a.iv)
        message = unpad(cipher.decrypt(a.message), 8)
        print("The message was: ", message)
        connection.close()