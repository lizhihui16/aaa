from socket import *

#确保两端使用同一个套接字文件
sock_file = './sock'

sockfd = socket(AF_UNIX,SOCK_STREAM)
sockfd.connect(sock_file)

#信息收
while True:
    msg = input(">>")
    if not msg:
        break
    sockfd.send(msg.encode())
sockfd.close()