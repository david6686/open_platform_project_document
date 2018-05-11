# -*- encoding: utf-8 -*-

#上面那個是encode指定utf-8，這樣子才可以有中文傳輸的功能

import socket
import threading
from time import gmtime, strftime


# TODO: 歡迎進入聊天室訊息（給進入者）
# TODO: 取暱稱
# TODO: 取完暱稱，歡迎 某某人訊息（歡迎進入者）
# TODO: 聊天室系統公告: 有誰進入了聊天室
# TODO: 誰發話在什麼時間 （可以用server的時間）
# TODO: （加分題）聊天室公告：某人離開了聊天室
# TODO: （加分題）聊天室人數現況

class Server:
    def __init__(self, host, port):
        # new一個socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))  # 用bind方式  不斷監聽
        self.sock.listen(5)    #listen   可以包含五個連線？
        print('Server', socket.gethostbyname(host), 'listening ...')    #做完上面，會說在哪個ip做listen
        self.mylist = list()

    #確認註冊過的使用者，看要不要接收他
    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())

        try:
            #第一個進來的 送的訊息是不是b'1'  是1就接受  並開一個thread給他
            buf = connection.recv(1024).decode()
            if buf == '1':
                # start a thread for new connection
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()
            # 反之不合法
            else:
                connection.send(b'please go out!daze~')
                connection.close()
        except:
            pass

    # send whatToSay to every except people in exceptNum
    #把connect id 記住，會加進mylist內，就可以做出線上人數多少人
    #傳送訊息的function也就是從list內把除了自己以外的所有人拿出來並傳送訊息（恩...所以送給自己知道怎麼做了吧）
    def tellOthers(self, exceptNum, whatToSay):
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    c.send(whatToSay.encode())
                except:
                    pass

    def subThreadIn(self, myconnection, connNumber):
        # 把使用者connect id加進list
        self.mylist.append(myconnection)
        while True:
            #不斷接收新的訊息，並送出訊息
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    self.tellOthers(connNumber, recvedMsg)
                else:
                    pass

            except (OSError, ConnectionResetError):
                #下線就要從list移除並關掉connect
                try:
                    print(myconnection, "BYEBYE")
                    self.mylist.remove(myconnection)
                except:
                    pass

                myconnection.close()
                return


def main():
    s = Server('localhost', 5550)
    #不斷的checkconnect
    while True:
        s.checkConnection()


if __name__ == "__main__":
    main()

