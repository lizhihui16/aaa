
from socket import *
import sys
import time

class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')  #发送请求
        data = self.sockfd.recv(128).decode()
        if data == 'ok':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print('文件列表展示完毕')
        else:
            #无法执行操作
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit('谢谢使用')
    
    def do_get(self,filename):
        self.sockfd.send(('G '+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'ok':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("%s下载完毕"%filename)
        else:
            print(data)
    
    def do_put(self,upload):
        try:
            f = open(upload,'rb')
        except:
            print("没有找到文件")
            return
        self.sockfd.send(('P '+upload).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'ok':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break 
                self.sockfd.send(data)
            f.close()
            print('%s上传完毕'%upload)
#网络连接
def main():
    if len(sys.argv)<3:
        print('args is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    addr = (HOST,PORT)

    sockfd = socket()
    try:
        sockfd.connect(addr)
    except Exception as e:
        print('连接服务器失败：',e)
        return

    #创建对象
    ftp = FtpClient(sockfd)

    while True:
        print('+========命令选项========+')
        print('|****      list      ****|')
        print('|****    get file    ****|')
        print('|****    put file    ****|')
        print('|****      quit      ****|')
        print('+========================+\n')

        cmd = input('输入命令>>')
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() =='quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            upload = cmd.split(' ')[-1]
            ftp.do_put(upload)

        else:
            print('请输入正确命令')

if __name__=='__main__':
    main()
