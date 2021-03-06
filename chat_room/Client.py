import socket
import threading
import json


username_ = None

class Client:
    def __init__(self, host, port, nickname):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')   #byte方式 傳送  送key 假設是1

        self.username = nickname
        self.talkinfo = {"username":self.username}
        self.talkinfo["command"] = "join"
        self.sock.send(json.dumps(self.talkinfo).encode())
        self.talkinfo["command"] = ""

    def sendThreadFunc(self):
        while True:
            try:
                myword = input(self.username+":    ")

                if myword == "\list":
                    self.talkinfo["message"] = myword
                    self.talkinfo["command"] = "list"
                    self.sock.send(json.dumps(self.talkinfo).encode())
                else:
                    self.talkinfo["message"] = myword
                    self.talkinfo["command"] = "message"
                    self.sock.send(json.dumps(self.talkinfo).encode())
                
                self.talkinfo["command"] = ""
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)    ＃去接收  1024是接收的長度
                print("\r"+otherword.decode())
                print("\n"+self.username+":    ", end="")
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')

def main():
    print("Welcome to Chatroom!")
    username_ = input("Input your nickname :")
    c = Client('140.138.224.111', 5550, username_)
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    # 兩個thread一起初始化
    for t in threads:
        t.setDaemon(True)   #父執行緒不用等子執行緒
        t.start()
    t.join()

if __name__ == "__main__":
    main()
