
from socket import *
s=socket()

# import socket
# s=socket.socket()

#设置端口可以立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
print(s.family)

print(s.type)

s.bind(('176.47.2.234',8888))
#获取套接字绑定地址
print(s.getsockname())
#获取文件描述符
print(s.fileno())

s.listen(3)
c,addr=s.accept()
#客户端连接套接字获取对应客户端地址
print(c.getpeername())

c.recv(1024)

c.close()
s.close()