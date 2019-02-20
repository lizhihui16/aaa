'''
ftp 文件服务器程序
fork server训练
'''

from socket import *
import os,sys
import time

#全局变量设置
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
FILE_PATH = "/home/tarena/aid1808/python2/dsa/"

class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        print('执行List')
        #获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send('文件库为空'.encode())
            return 
        else:
            print(2)
            self.connfd.send(b'ok')
            time.sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH+file):
                files = files+file+'#'
        self.connfd.sendall(files.encode())

    def do_get(self,filename):
        try:
            fd = open(FILE_PATH+filename,'rb')
        except:
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)
        #发送文件内容
        while True:
            data  = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
            self.connfd.send(data)
        print('传输完毕')
        
    def do_put(self,upload):
        try:
            fd = open(FILE_PATH+upload,'wb')
        except:
            self.connfd.send('上传失败'.encode())
            return
        else:
            self.connfd.send(b'ok')
        #接收文件
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()
        print('接收完毕')

        

#创建网络连接
def main():
    #创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    print("Listen the port 8888....")

    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit('服务器退出')
        except Exception as e:
            print('服务器异常：',e)
            continue
        print('连接用户端：',addr)
        #创建子进程
        pid = os.fork()
        if pid == 0:
            p = os.fork()
            if p == 0:
                sockfd.close
                ftp = FtpServer(connfd)
                while True:
                    data = connfd.recv(1024).decode()
                    if not data or data[0] == 0:
                        connfd.close()
                        sys.exit('客户端退出')
                    elif data[0] == 'L':
                        ftp.do_list()
                    elif data[0] == 'G':
                        filename = data.split(' ')[-1]
                        ftp.do_get(filename)
                    elif data[0] == 'P':
                        upload = data.split(' ')[-1]
                        ftp.do_put(upload)
            else:
                os._exit(0)
        else:
            connfd.close()
            os.wait()

if __name__=='__main__':
    main()
