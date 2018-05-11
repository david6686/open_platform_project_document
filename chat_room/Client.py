import socket
import threading
import json

username_ = None

class Client:
    def __init__(self, host, port, nickname):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')

        self.username = nickname
        self.talkinfo = {"username":self.username}

    def sendThreadFunc(self):
        while True:
            try:
                myword = input(self.username+":    ")
                self.talkinfo["message"] = myword
                self.sock.send(json.dumps(self.talkinfo).encode())
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)
                print(otherword.decode())
                
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')

def main():
    print("Welcome to Chatroom!")
    username_ = input("Input your nickname")
    c = Client('140.138.224.111', 5550, username_)
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

if __name__ == "__main__":
    main()
