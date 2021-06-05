# Patrick Stumbaugh
# Project 4 - Client/Server Chat

# NOTE - Must use Python3.
# To start program, start this server first by entering in command line:
# python3 server.py

# --------SERVER---------

import time, socket, sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind(("", port))
print("This is your IP: ", s_ip)

new_socket.listen(1)


conn, add = new_socket.accept()


while True:
    message = input("Me : ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print("CLIENT: ", message)
