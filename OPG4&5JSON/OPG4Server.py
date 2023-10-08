from socket import *
import threading
import random

serverPort = 12002
serverHost = '192.168.0.114'    # CMD ipconfig.. for at finde din IP..

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(2)  # Angiver det maksimale antal ventende forbindelser
print('Server is ready to listen')

def handleClient(connectionSocket, addr):
    welcome_message = "Velkommen til serveren! Indtast en af foelgende metoder: (random/add/subtract)\n ... eller (quit) for at forlade serveren\n\nSkriv en metode efterfulgt af to vaerdier.\n\n"
    connectionSocket.send(welcome_message.encode())
    
    Conversation = True
    while Conversation:
        method = connectionSocket.recv(1024).decode().strip().lower()
        
        if method == 'quit':
            Conversation = False

        elif method in ['random', 'add', 'subtract']:
            try:
                connectionSocket.send("\nInput foerste value:  ".encode())
                value1 = int(connectionSocket.recv(1024).decode())

                connectionSocket.send("\nInput anden value:  ".encode())
                value2 = int(connectionSocket.recv(1024).decode())
                
                if method == 'random':
                    response = str(f"Dit random result: {random.randint(value1, value2)}")
                elif method == 'add':
                    response = str(f"Resultat: {value1 + value2}")
                elif method == 'subtract':
                    response = str(f"Resultat: {value1 - value2}")
                
                connectionSocket.send(response.encode())
            except ValueError:
                response = "INAVLID INPUT!\n  Vaerdierne skal vaere heltal!\n"
                connectionSocket.send(response.encode())
        else:
            response = "INVALID METHOD!\n  Brug: (random/add/subtract/quit) \n"
            connectionSocket.send(response.encode())

    print(f"'{addr}' left Conversation")
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
    print(f"'{addr}' has joined Conversation")
