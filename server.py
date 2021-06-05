# Patrick Stumbaugh
# Project 4 - Client/Server Chat

# NOTE - Must use Python3.
# To start program, start this server first by entering in command line:
# python3 server.py
# The client program will send the first message

# --------SERVER---------

import socket

# setup socket
serverSocket = socket.socket()
ipAddress = socket.gethostbyname("localhost")
# if using something other than "localhost" for the host:
# hostInformation = socket.gethostname()
# ipAddress = socket.gethostbyname(hostInformation)

# port information - must match client port number
port = 6789
print("Server listening on localhost, port: %s" % port)

# set socket re-use option
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# connect (bind) and listen for outside connections (only 1 allowed for this program)
serverSocket.bind(("", port))
serverSocket.listen(1)  # waits here until connection is requested

# new connection requested, accept the connection request
conn, connInfo = serverSocket.accept()
print("Connected by ", connInfo)

firstMessage = True
print("Waiting for message...")

while True:
    # GET MESSAGE FROM CLIENT:
    messageReceived = (conn.recv(1024)).decode()
    if messageReceived == "/q":  # if the client wants to close the chat
        conn.close()
        break
    print("CLIENT: ", messageReceived)
    if firstMessage == True:  # prompts for first message from server back to client
        print("Type /q to quit")
        print("Enter message to send...")
        firstMessage = False

    # SEND A MESSAGE TO THE CLIENT:
    messageToSend = input("> ")
    if messageToSend == "/q":  # if the server wants to close the chat
        conn.send(
            messageToSend.encode()
        )  # send the message so the client gets the close reequest too
        conn.close()
        break
    conn.send(messageToSend.encode())
