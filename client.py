# Patrick Stumbaugh
# Project 4 - Client/Server Chat

# NOTE - Must use Python3.
# To start program, start the server.py program first.
# Once that is running and awaiting messages, start this client program by entering:
# python3 client.py

# --------CLIENT---------

import time, socket, sys

clientSocket = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
port = 8080

print("This is your IP address: ", ip)

clientSocket.connect(("", port))

while True:
    message = input("> ")
    clientSocket.send(message.encode())
    message = clientSocket.recv(1024).decode()
    print("CLIENT: ", message)
