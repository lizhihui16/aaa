
from socket import *
from time import sleep

#目标地址
dest = ('176.47.2.234',5454)

s = socket(AF_INET,SOCK_DGRAM)
#设置可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("往后余生，风雪是你".encode(),dest)
s.close()