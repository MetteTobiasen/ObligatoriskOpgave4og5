from socket import *
from threading import *
from random import *


def Choise_Case(sentence):
    match sentence:
        case "random":
            connectionSocket.send("Input two numbers seperated by space".encode())
            input = connectionSocket.recv(1024).decode()
            numbers = input.split()
            if len(numbers) != 2:
                connectionSocket.send("Invalid input. Please enter two numbers separated by a space.".encode())
                return
            try:
                num1, num2 = map(int, numbers)
                random_num = randint(min(num1, num2), max(num1, num2))
                response = f"{random_num}"
                connectionSocket.send(response.encode())
            except ValueError:
                connectionSocket.send("Invalid input. Please enter two valid numbers.".encode())
        case "add":
            connectionSocket.send("input two numbers seperated by space".encode())
            input = connectionSocket.recv(1024).decode()
            numbers = input.split()
            if len(numbers) !=2:
                connectionSocket.send("Invalid input. Please enter two numbers separated by a space.".encode())
                return
            try:
                num1, num2 = map(int, numbers)
                num1AddNum2 = num1 + num2
                response = f"{num1AddNum2}"
                connectionSocket.send(response.encode())
            except ValueError:
                connectionSocket.send("Invalid input. Please enter two numbers separated by space.".encode())
        case "subtract":
            connectionSocket.send("input two numbers seperated by space".encode())
            input = connectionSocket.recv(1024).decode()
            numbers = input.split()
            if len(numbers) !=2:
                connectionSocket.send("Invalid input. Please enter two numbers separated by a space.".encode())
                return
            try:
                num1, num2 = map(int, numbers)
                num1SubtractNum2 = num1 - num2
                response = f"{num1SubtractNum2}"
                connectionSocket.send(response.encode())
            except ValueError:
                connectionSocket.send("Invalid input. Please enter two numbers separated by space.".encode())

def handleClient(connectionSocket, address):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        sentence = sentence.lower().strip()
        Choise_Case(sentence)        


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    Thread(target = handleClient,args = (connectionSocket, addr)).start()