from socket import *
from multiprocessing import Process
import sys

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

def worker(c):
    print('进程',c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive')
    c.close()
    sys.exit(0)

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

    print(1)
    p = Process(target = worker,args = (c,))
    #或
    # p = Process(target = worker)

    p.daemon=True
    p.start()
    # p.join()

