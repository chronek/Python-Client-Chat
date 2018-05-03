from socket import *
serverName = 'localhost'
SERVER_PORT = 5002
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,SERVER_PORT))
while True:
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
clientSocket.close()