import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("", 1100))
    s.listen(1)
    connection,address=s.accept()
    with connection:
        a=connection.recv(1024)
        print(a.decode("ascii"))
        connection.close()