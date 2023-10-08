from socket import*
import threading
import json
import random

serverPort = 12002
#serverHost = '192.168.0.114'    # CMD ipconfig.. for at finde din IP..

serverSocket = socket(AF_INET, SOCK_STREAM)
#serverSocket.bind((serverHost, serverPort))
serverSocket.bind(('', serverPort))
serverSocket.listen(2)  # Angiver det maksimale antal ventende forbindelser
print('Server is ready to listen')

valid_methods = ['random', 'add', 'subtract', 'quit']

def handleClient(connectionSocket, addr):
     # Send en velkomstbesked til klienten
    welcome_message = "Velkommen til serveren!\nDu kan bruge følgende metoder: 'random', 'add', 'subtract', 'quit'."
    connectionSocket.send(welcome_message.encode())

    Conversation = True
    while Conversation:
        try:
            request = connectionSocket.recv(1024).decode()
            request_obj = json.loads(request)

            method = request_obj.get("method", "").strip().lower()
            
            if method not in valid_methods:
                response = json.dumps({"error": "Ugyldig metode. Brug 'random', 'add', 'subtract' eller 'quit'."})
                connectionSocket.send(response.encode())
                if method != 'quit':
                    continue
            
            if method == 'quit':
                response = json.dumps({"result": "Afbrydelse af forbindelse."})
                connectionSocket.send(response.encode())
                break

            tal1 = request_obj.get("Tal1", 0)
            tal2 = request_obj.get("Tal2", 0)

            if method == 'random':
                result = random.randint(tal1, tal2)
            elif method == 'add':
                result = tal1 + tal2
            elif method == 'subtract':
                result = tal1 - tal2
            else:
                result = "Ukendt metode"

            response = json.dumps({"result": result})
            connectionSocket.send(response.encode())
        except Exception as e:
            response = json.dumps({"error": f"Fejl: {str(e)}"})
            connectionSocket.send(response.encode())

    print(f"'{addr}' left Conversation")
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target = handleClient, args = (connectionSocket, addr)).start() #Hvergang en forsøger at connect serveren.. Skabes en ny tråd
    print (f"{addr} has joined Conversation")

