# from socket import *
# from time import sleep,ctime

# #创建tcp套接字
# sockfd=socket()
# sockfd.bind(('0.0.0.0',8888))
# sockfd.listen(3)

# #设置为非阻塞函数
# sockfd.setblocking(False)
# while True:
#     print('Waiting for connect...')
#     try:
#         connfd,addr = sockfd.accept()
#     except BlockingIOError:
#         sleep(2)
#         print(ctime())
#         continue
#     else:
#         print('Connect from',addr)
#         data = connfd.recv(1024)
#         print('Receive:',data.decode())
#         connfd.close()
# sockfd.close()





from socket import *
from time import sleep,ctime

#创建tcp套接字
sockfd=socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)

# #设置为非阻塞函数
# sockfd.setblocking(False)

#设置超时时间
sockfd.settimeout(5)

while True:
    print('Waiting for connect...')
    try:
        connfd,addr = sockfd.accept()
    # 捕获非阻塞异常
    # except BlockingIOError:
    #     sleep(2)

    #捕获超时异常
    except timeout:
        print(ctime())
        continue
    else:
        print('Connect from',addr)
        data = connfd.recv(1024)
        print('Receive:',data.decode())
        connfd.close()
sockfd.close()








