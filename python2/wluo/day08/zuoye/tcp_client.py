

from socket import *

sockfd=socket()
#发起连接
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

#发收消息
while True:
    data=input('>>')
    sockfd.send(data.encode()) 
    if not data:
        break
    data=sockfd.recv(1024) 
    print("From server:",data.decode())
sockfd.close()










# from socket import *

# sockfd=socket()
# #发起连接
# server_addr = ('127.0.0.1',8888)
# sockfd.connect(server_addr)

# #发收消息
# while True:
#     data=input('>>')
#     if data=='##':
#         break
#     else:
#         sockfd.send(data.encode()) 
#         if data=='###':
#             break
#         data=sockfd.recv(1024) 
# sockfd.close()

