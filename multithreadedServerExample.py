import socket
import threading
import time
import random

SERVER_PORT = 5002
clients = []
#addresses = []

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            clients.append(client)
            #addresses.append(address)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024

        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    #time.sleep(random.randint(1, 20)) #1-20 second delay to test threading with multiple clients (to see wich ones gets the response first)
                    for idx, myClient in enumerate(clients):
                        myClient.send(response)
                else:
                    raise ValueError('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    ThreadedServer('',SERVER_PORT).listen()
