
from socket import *

sockfd=socket()
#发起连接
server_addr = ('0.0.0.0',6888)
sockfd.connect(server_addr)
#发收消息
while True:
    s = input("请输入源文件: ")
    fr=open(s,'rb')
    while True:
        f = fr.readline()
        data =f   
        sockfd.send(data) 
        if not data:
            break

    # data=sockfd.recv(1024)
    # d = input("请输入目标文件: ")
    # fw=open(d,'wb')
    # fw.write(data)
sockfd.close()

