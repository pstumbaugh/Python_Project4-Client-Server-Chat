# Patrick Stumbaugh
# Project 4 - Client/Server Chat

# NOTE - Must use Python3.
# To start program, start this server first by entering in command line:
# python3 server.py

# --------SERVER---------

import time, socket, sys

serverSocket = socket.socket()
ipAddress = socket.gethostbyname("234")
# if using something other than "localhost" for the host:
# hostInformation = socket.gethostname()
# ipAddress = socket.gethostbyname(hostInformation)

# port information - must match client port number
port = 6789
print("Server listening on localhost, port: %s" % port)

# set socket re-use option
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(("", port))

serverSocket.listen(1)

conn, connInfo = serverSocket.accept()
print("Connected by ", connInfo)

while True:
    message = (conn.recv(1024)).decode()
    print("Client: ", message)
    message = input("> ")
    conn.send(message.encode())
