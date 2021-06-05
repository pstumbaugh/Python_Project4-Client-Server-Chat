# Patrick Stumbaugh
# Project 4 - Client/Server Chat

# NOTE - Must use Python3.
# To start program, start this server first by entering in command line:
# python3 server.py

# --------SERVER---------

import time, socket, sys

serverSocket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080

# set socket re-use option
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(("", port))
print("This is your IP: ", s_ip)

serverSocket.listen(1)

conn, add = serverSocket.accept()

while True:
    message = (conn.recv(1024)).decode()
    print("Client: ", message)
    message = input("> ")
    conn.send(message.encode())
