from socket import *
import sys
import time
from zuoye1 import Mysqlpython


class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'Z')  #发送请求
        name = input("姓名：")
        mima = input("密码：")
        l=name + ' ' +mima
        self.sockfd.send(l.encode())
        msg = self.sockfd.recv(128)
        msg = msg.decode()
        if msg == 'ok':
            while True:
                print('+========命令选项========+')
                print('|****     查看单词    ****|')
                print('|****     历史记录    ****|')
                print('|****      退出      ****|')
                print('+========================+\n')

                cmd = input('输入命令>>')
                if cmd.strip() == '4':
                    ftp.do_danci()
                elif cmd.strip() =='5':
                    ftp.do_jilu()
                elif cmd.strip() == '6':
                    ftp.do_fanhui()
        
    
    def do_get(self):
        self.sockfd.send(b'D')  #发送请求
        name = input("姓名：")
        mima = input("密码：")
        l=name + ' ' +mima
        self.sockfd.send(l.encode())
        msg = self.sockfd.recv(128)
        msg = msg.decode()
        if msg == 'ok':
            while True:
                print('+========命令选项========+')
                print('|****     查看单词    ****|')
                print('|****     历史记录    ****|')
                print('|****      退出      ****|')
                print('+========================+\n')

                cmd = input('输入命令>>')
                if cmd.strip() == '4':
                    ftp.do_danci()
                elif cmd.strip() =='5':
                    ftp.do_jilu()
                elif cmdstrip() == '6':
                    ftp.do_fanhui()
        else:
            print('用户不存在')

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit('谢谢使用')

    def d0_danci(self):
        self.sockfd.send(b'Z')  #发送请求
        a = input('单词：')
        self.sockfd.send(a.encode())
        msg = self.sockfd.recv(1024)
        print(msg)

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
        print('|****      注册      ****|')
        print('|****      登录      ****|')
        print('|****      退出      ****|')
        print('+========================+\n')

        cmd = input('输入命令>>')
        if cmd.strip() == '1':
            ftp.do_list()

        elif cmd.strip() == '2':
            ftp.do_get()

        elif cmd.strip() =='3':
            ftp.do_quit()
            
        else:
            print('请输入正确命令')

if __name__ == '__main__':
    main()
