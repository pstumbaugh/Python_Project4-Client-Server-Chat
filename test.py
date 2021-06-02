# Establish connection with client.
    serverSocket, addr = clientSocket.accept()

    if initialConnection == True:
        print("Connected by: ", addr)
        print("Type /q to quit")
        print("Enter message to send:")
        initialConnection = False

    messageToSend = input()

    # send a thank you message to the client.
    serverSocket.send(messageToSend)