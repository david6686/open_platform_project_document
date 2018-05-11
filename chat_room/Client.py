import socket
import threading

class Client:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')   #byte方式 傳送  送key 假設是1

    def sendThreadFunc(self):
        while True:
            try:
                myword = input()     #不斷的等待接收使用者的輸入
                self.sock.send(myword.encode())    # 一樣encode起來送出去
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)    ＃去接收  1024是接收的長度
                print(otherword.decode())
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')

def main():
    c = Client('localhost', 5550)    #new Client    addr,port number  要看誰當server喔
    #  切兩個thread  兩個同時跑  不斷的收與送
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
