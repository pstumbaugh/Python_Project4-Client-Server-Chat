# Patrick Stumbaugh
# Project 4 - Client/Server Chat

# --------CLIENT---------

import time, socket, sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
port = 8080

print("This is your IP address: ", ip)
name = input("Enter Friend's name: ")


socket_server.connect(("", port))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, " has joined...")
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())
