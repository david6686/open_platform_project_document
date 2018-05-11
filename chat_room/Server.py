# -*- encoding: utf-8 -*-

#上面那個是encode指定utf-8，這樣子才可以有中文傳輸的功能

import json
import socket
import threading
from time import gmtime, strftime, localtime


# DONE: 歡迎進入聊天室訊息（給進入者）
# DONE: 取暱稱
# DONE: 取完暱稱，歡迎 某某人訊息（歡迎進入者）
# DONE: 聊天室系統公告: 有誰進入了聊天室
# DONE: 誰發話在什麼時間 （可以用server的時間）
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

    # 確認註冊過的使用者，看要不要接收他
    def checkConnection(self):
        connection, addr = self.sock.accept()
        # 現在有新的連線進來
        print('Accept a new connection', connection.getsockname(), connection.fileno())

        try:
            # 第一個進來的 送的訊息是不是b'1'  是1就接受  並開一個thread給他
            buf = connection.recv(1024).decode()
            if buf == '1':
                # start a thread for new connection
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()
                connection.send('歡迎進入幻想鄉!'.encode())

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

    def getTime(self) -> str:
        return strftime('%H:%M:%S', localtime())

    def subThreadIn(self, myconnection, connNumber):
        # 把使用者connect id加進list
        self.mylist.append(myconnection)
        message_template = '{username}: {message}    {time}'
        system_message_template = {
            'join': 'SYSTEM: 歡迎 {username} 加入聊天室 {time}',
            'exit': 'SYSTEM: {username} 離開了我們 QQAQQ 普天同慶XDD   {time}',
            '\list': 'SYSTEM: 目前有 {member_number} 人在線上'
        }
        while True:
            #不斷接收新的訊息，並送出訊息
            try:
                recvedMsg = myconnection.recv(1024).decode()
                data = json.loads(recvedMsg)
                data['time'] = self.getTime()
                if 'command' in data:
                    if data['command'] == '\list':
                        data['member_number'] = len(self.mylist)
                        self.tellOthers(connNumber, system_message_template[data['command']].format(**data))
                    else:
                        self.tellOthers(connNumber, system_message_template[data['command']].format(**data))
                elif recvedMsg:
                    self.tellOthers(connNumber, message_template.format(**data))
                else:
                    pass

            except (OSError, ConnectionResetError):
                #下線就要從list移除並關掉connect
                try:
                    self.mylist.remove(myconnection)

                except:
                    pass

                myconnection.close()
                return


def main():
    s = Server('140.138.224.111', 5550)
    #不斷的checkconnect
    while True:
        s.checkConnection()


if __name__ == "__main__":
    main()

