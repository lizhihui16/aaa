

# from socket import *

# sockfd=socket()
# #发起连接
# sockfd.connect(('0.0.0.0',8888))
# #发收消息
# # s = input("请输入源文件: ")
# fr=open('ye.jpg','rb')

# while True:
#     data = fr.readline()
    
#     if not data:
#         break
#     sockfd.send(data) 
# fr.close()
# sockfd.close()








from socket import *

sockfd=socket()
#发起连接
server_addr = ('0.0.0.0',6888)
sockfd.connect(server_addr)
#发收消息
while True:
    s = input("请输入源文件: ")
    fr=open(s,'rb')
    fr.truncate(pos = None)
    while True:
        f = fr.readline()
        sockfd.send(data) 
        if not data:
            break

    # data=sockfd.recv(1024)
    # d = input("请输入目标文件: ")
    # fw=open(d,'wb')
    # fw.write(data)
sockfd.close()

