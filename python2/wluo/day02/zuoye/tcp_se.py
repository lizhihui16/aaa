
from socket import *

#创建tcp套接字
# sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#绑定ip
sockfd.bind(('0.0.0.0',6888))

#设置监听
sockfd.listen(5)
print('设置监听')

while True:
    
    connfd,addr=sockfd.accept()
    print('连接客户端的地址',addr)
    data=connfd.recv(1024)
    d = input("请输入目标文件: ")
    fw=open(d,'wb')
    if not data:
        break
    fw.write(data)
    print(data.decode())
    # s = input("请输入源文件: ")
    # fr=open(s,'rb')
    # f=fr.readline()
    # data =f  
    # n=sockfd.send('结束'.encode())
    connfd.close()
    fw.close()
sockfd.close()
