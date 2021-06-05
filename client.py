# Patrick Stumbaugh
# Project 4 - Client/Server Chat

# NOTE - Must use Python3.
# To start program, start the server.py program first.
# Once that is running and awaiting messages, start this client program by entering:
# python3 client.py
# The client program will send the first message

# --------CLIENT---------

import socket

# setup socket
clientSocket = socket.socket()
hostInformation = socket.gethostname()
ipAddress = socket.gethostbyname("localhost")
# if using something other than "localhost" for the host:
# hostInformation = socket.gethostname()
# ipAddress = socket.gethostbyname(hostInformation)

# port information - must match server port number
port = 6789

# connect to the port the server is using
clientSocket.connect(("", port))

# print info about connection:
print("Connected to localhost on port:", port)

# print user information needed:
print("Type /q to quit")
print("Enter message to send...")

while True:
    # SEND A MESSAGE TO THE SERVER:
    messageToSend = input("> ")
    if messageToSend == "/q":  # if the client wants to close the chat
        clientSocket.send(
            messageToSend.encode()
        )  # send the message so the server gets the close reequest too
        clientSocket.close()
        break
    clientSocket.send(messageToSend.encode())

    # GET A MESSAGE FROM THE SERVER:
    messageReceived = clientSocket.recv(1024).decode()
    if messageReceived == "/q":  # if the client wants to close the chat
        clientSocket.close()
        break
    print("SERVER: ", messageReceived)
