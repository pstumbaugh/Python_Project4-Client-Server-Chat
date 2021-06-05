# Patrick Stumbaugh
# Project 4 - Client/Server Chat

# NOTE - Must use Python3.
# To start program, start the server.py program first.
# Once that is running and awaiting messages, start this client program by entering:
# python3 client.py

# --------CLIENT---------

import time, socket, sys

clientSocket = socket.socket()
hostInformation = socket.gethostname()
ipAddress = socket.gethostbyname(hostInformation)

# port information - must match server port number
port = 6789

clientSocket.connect(("", port))

print("Connected to localhost on port:", port)

while True:
    message = input("> ")
    clientSocket.send(message.encode())
    message = clientSocket.recv(1024).decode()
    print("CLIENT: ", message)
