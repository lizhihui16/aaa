
# import socket
# #创建套接字
# sockfd=socket.socket(socket.AF_INET,
#                      socket.SOCK_STREAM,
#                      proto=0)
# #设置绑定地址
# sockfd.bind(('0.0.0.0',8866))
# #设置监听
# sockfd.listen(5)
# print("Waiting for connect...")
# #等待处理客户端连接
# connfd,addr=sockfd.accept()
# print('Connect from',addr)     #打印客户端地址
# #收发消息
# while True:
#     data=connfd.recv(1024)
#     if data.decode()=='##':
#         print('Receive message:',data.decode())
#         connfd.close()
#         sockfd.close()
#         break
#     else:
# # print('Receive message:',data.decode())
#         print('Receive message:',data.decode())
#         n=connfd.send('Receive your msg\n'.encode())
#         print('Send %d bytes'%n)

# #关闭套接字
# # connfd.close()
# # sockfd.close()




import socket
#创建套接字
sockfd=socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM,
                     proto=0)
#设置绑定地址
sockfd.bind(('0.0.0.0',8888))
#设置监听

sockfd.listen(5)
print("Waiting for connect...")
#等待处理客户端连接
while True:
    connfd,addr=sockfd.accept()
    print('Connect from',addr)     #打印客户端地址
    #收发消息
    while True:
        data=connfd.recv(1024)
        print('Receive message:',data.decode())
        n=connfd.send('Receive your msg\n'.encode())
        print('Send %d bytes'%n)

        if data.decode()=='###':
            print('Receive message:',data.decode())
            # connfd.close()
            # sockfd.close()
            break
        # elif data.decode() is '':
        #     continue
    # print('Receive message:',data.decode())

#关闭套接字
    # connfd.close()
    # sockfd.close()