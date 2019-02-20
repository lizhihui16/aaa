
from socket import *

s=socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind(('176.47.2.234',5454))
while True:
    try:
        msg,addr = s.recvfrom(1024)
        print('从{}获取广播:{}'.format(addr,msg.decode()))
    except KeyboardInterrupt as e:
        print('退出接收')
        break
    except Exception as e:
        print(e)
s.close()