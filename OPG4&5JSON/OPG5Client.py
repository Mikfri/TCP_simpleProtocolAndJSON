import socket
import json

serverHost = '192.168.0.114'
serverPort = 12002

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

# Modtag og udskriv velkomstbesked fra serveren
welcome_message = clientSocket.recv(1024).decode()
print(welcome_message)

while True:
    method = input("Indtast metoden: ").strip().lower()
    if method not in ['random', 'add', 'subtract', 'quit']:
        print("Ugyldig metode. Brug 'random', 'add', 'subtract' eller 'quit'.")
        continue
    
    if method == 'quit':
        clientSocket.send(json.dumps({"method": method}).encode())
        response = clientSocket.recv(1024).decode()
        response_obj = json.loads(response)
        print(response_obj['result'])  # Udskriv beskeden fra serveren
        break

    try:
        tal1 = int(input("Tal 1: "))
        tal2 = int(input("Tal 2: "))
    except ValueError:
        print("Ugyldig indtastning. Brug kun heltal for 'Tal 1' og 'Tal 2'.")
        continue

    request = {"method": method, "Tal1": tal1, "Tal2": tal2}
    clientSocket.send(json.dumps(request).encode())

    response = clientSocket.recv(1024).decode()
    response_obj = json.loads(response)

    if "result" in response_obj:
        print(f"Resultat: {response_obj['result']}")
    elif "error" in response_obj:
        print(f"Fejl: {response_obj['error']}")

clientSocket.close()