from socket import *
from threading import *
import sys

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

def handler(c):
    print('Connect from',c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive')
    c.close()

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#接收客户端请求
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue
    
    #创建线程
    t = Thread(target = handler,args = (c,))
    t.setDaemon(True)
    t.start()
    