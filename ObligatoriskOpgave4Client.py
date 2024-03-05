from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
keep_communicating = True

while keep_communicating:
    sentence = input('Choose command: (random, add, subtract): ')
    if sentence == "close":
        keep_communicating = False
    else:
        clientSocket.send(sentence.encode())
        response = clientSocket.recv(1024).decode()
        print('From Server:', response)
        numbers = input('Numbers: ')
        clientSocket.send(numbers.encode())
        response = clientSocket.recv(1024).decode()
        print('From Server:', response)
              
clientSocket.close() 



