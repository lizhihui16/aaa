from socket import *
import sys,os

#创建套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

s = socket()  #TCP套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#客户端处理函数
def client_handler(c):
    print('客户端：',c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive your message')
    c.close()
    sys.exit(0)#将子进程销毁
#循环等待客户端链接
print("监听8888")
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('退出进程')
    except Exception as e:
        print("Error:",e)
        continue
    
    #创建新的进程处理客户端请求
    pid = os.fork()

    #子进程处理客户端请求
    if pid  == 0:
        p = os.fork()  #创建二级子进程处理僵尸进程
        if p == 0:
            s.close()
            client_handler(c)  #客户端处理函数
        else:os._exit(0)
    #父进程或者创建进程失败都继续等待下个客户端链接
    else:
        c.close()
        os.wait()
        continue 