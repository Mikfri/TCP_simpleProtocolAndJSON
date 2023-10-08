from socket import *
import threading

serverHost = '192.168.0.114'
serverPort = 12002

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

welcome_message = clientSocket.recv(1024).decode()
print(welcome_message)

def receive_messages():
    while True:
        message = clientSocket.recv(1024).decode()
        print(message)

# Start tråden, der modtager beskeder
threading.Thread(target=receive_messages, daemon=True).start() #daemon.. En tråd som kører i baggrunden.
# Køres tråden som en daemon: Programmet kan afsluttes, selvom tråden stadig kører.
# Køres tråden som IKKE-daemon: Tråden forhindrer programmet i at afslutte, indtil tråden er færdig.

while True:
    # Indtast en metode
    method = input("Indtast en metode (random/add/subtract/quit): ").lower()
    clientSocket.send(method.encode())

clientSocket.close()
