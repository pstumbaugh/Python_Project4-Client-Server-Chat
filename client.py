# Patrick Stumbaugh
# Project 4 - Client/Server Chat

# NOTE - Must use Python3.
# To start program, start the server.py program first.
# Once that is running and awaiting messages, start this client program by entering:
# python3 client.py

# --------CLIENT---------

import time, socket, sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
port = 8080

print("This is your IP address: ", ip)

socket_server.connect(("", port))

while True:
    message = (socket_server.recv(1024)).decode()
    print("SERVER: ", message)
    message = input("Me : ")
    socket_server.send(message.encode())
