
#coding=utf-8
'''
charroom
env:python 3.5
socket and fork
'''
from socket import *
import os,sys

def do_quit(s,user,name):
    msg = '\n%s 退出了聊天室'%name
    for i in user:
        if i ==name:
            s.sendto(b'Exit',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    del user[name]



def do_char(s,user,name,msg):
    msg = '\n%s 说： %s'%(name,msg)
    for i in user:
        if i!=name:
            s.sendto(msg.encode(),user[i])


def do_login(s,user,name,addr):
    if (name in user) or name == '管理员':
        s.sendto('该用户以存在'.encode(),addr)
        return
    s.sendto(b'OK',addr)
    #通知其他人
    msg = "\n欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户加入user
    user[name] = addr


def do_request(s):
    #{'zhangsan':('127.0.0.1',8888)}
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        # print(msg)
        # print(addr)
        msglist = msg.decode().split(' ')
        #区分请求类型
        if msglist[0] == 'L':
            do_login(s,user,msglist[1],addr)
        elif msglist[0] == 'C':
            #重新组织消息
            msg = ' '.join(msglist[2:])
            do_char(s,user,msglist[1],msg)
        elif msglist[0] == 'Q':
            do_quit(s,user,msglist[1])

#创建网络链接
def main():
    addr = ('0.0.0.0',8888)

    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(addr)

    #用于接收各种客户端请求，调用相应的函数处理
    pid = os.fork()
    if pid < 0:
        print('创建进程失败')
        return
    elif pid == 0:
        while True:
            msg = input('管理员消息：')
            msg = 'C 管理员 ' + msg
            s.sendto(msg.encode(),addr)
    else:
        do_request(s)


if __name__ =='__main__':
    main()