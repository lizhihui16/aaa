
#coding=utf-8
'''
charroom
env:python 3.5
socket and fork
'''
from socket import *
import os,sys
from threading import Thread
from zuoye1 import Mysqlpython
from dict import *
import re

#封装具体的http server功能
class tcp_c():
    def __init__(self,server_addr,static_dir):
        #添加对象属性
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        #创建套接字
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)#绑定地址

    #启动服务器
    def serve_forever(self):
        self.sockfd.listen(5)
        print('监听 %d'%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('服务器退出')
            except Exception as e:
                print('其他异常',e)
                continue
            #创建线程处理客户端请求
            clientThread = Thread(target = self.handle,args = (connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
    def handle(self,connfd):
        while True:

            msg = connfd.recv(1024)
            # print(msg.decode())
            msglist = msg.decode()
            if msglist == 'Z':
                tcp_c.do_login(msg,connfd)
            elif msglist== 'D':
                tcp_c.do_char(msg,connfd)
            elif msglist == 'Q':
                tcp_c.do_quit(user)

    def do_login(self,msg,connfd):
        msg = connfd.recv(1024)
        msglist = msg.decode().split(' ')

        sqlh=Mysqlpython('zidian')
        user=sqlh.all('select * from yh')
        for i in user:

            if msglist[0] == i[0]:
                connfd.send('该用户以存在'.encode())
                return
        else:
            #将用户加入user
            upd='insert into yh values("%s","%s")'% (msglist[0],msglist[1])
            sqlh.zhixing(upd)
            print(user)
            connfd.send(b'ok')
            print(1)
        while True:
            msg = connfd.recv(1024)
            # print(msg.decode())
            msglist = msg.decode()
            if msglist == 'C':
                tcp_c.do_cha(msg,connfd)
            elif msglist== 'L':
                tcp_c.do_lishi(msg,connfd)
            elif msglist == 'E':
                tcp_c.do_euit(user)

    def do_char(self,msg,connfd):
        msg = connfd.recv(1024)
        msglist = msg.decode().split(' ')

        sqlh=Mysqlpython('zidian')
        user=sqlh.all('select * from yh')
        for i in user:
            if msglist[0] == i[0]:
                connfd.send(b'ok')
                print(1)
                return
        else:
            connfd.send('用户不存在'.encode())
        while True:
            msg = connfd.recv(1024)
            # print(msg.decode())
            msglist = msg.decode()
            if msglist == 'Z':
                tcp_c.do_cha(msg,connfd)
            elif msglist== 'L':
                tcp_c.do_lishi(msg,connfd)
            elif msglist == 'E':
                tcp_c.do_euit(user)

    def do_quit(s,user):
        pass

    def do_cha(self,connfd)
        msg = connfd.recv(1024)
        msglist = msg.decode().split(' ')

        fd = open('./dict.txt')
        while True:
            f= fd.readlist()
            a= r'[a-z]?[a-z]*\s+\S'
            n=re.match(a,f).groupdict()
            if f == n:
                connfd.send(n[])






if __name__ == '__main__':
    #用户使用时自己设定服务器IP
    server_addr = ('0.0.0.0',8000)
    #需要用户提供网页位置
    static_dir = "/home/tarena/aid1808/python2/project/htttp/dianzixidian/dict.txt"

    #创建服务器对象
    tcp_c = tcp_c(server_addr,static_dir)
    #启动服务器
    tcp_c.serve_forever()