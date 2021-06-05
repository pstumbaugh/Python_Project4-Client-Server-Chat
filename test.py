import time, socket, sys

# socket information
clientSocket = socket.socket()
serverHost = socket.gethostname()
ipAddress = socket.gethostbyname(serverHost)

# port information (must match port from server side)
port = 6789

print("This is your IP address: ", ipAddress)

clientSocket.connect(("", port))

while True:
    message = (clientSocket.recv(1024)).decode()
    print("[*]Server: ", message)
    message = input("Me : ")
    clientSocket.send(message.encode())


# SERVER
import time, socket, sys

# socket information
serverSocket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

# port information (must match port from client side)
port = 6789

# set socket re-use option
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(("", port))

# print out connection information
print("Server listening on port: %s" % port)

serverSocket.listen(1)

conn = serverSocket.accept()

print("Connected by ", conn[1])

while True:
    message = input("Me : ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print("[*]Client: ", message)
