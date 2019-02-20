#coding = utf8

from socket import *
import sys 
import getpass

#网络连接
def main():
    if len(sys.argv) < 3:
        print('aaaaaa')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket()
    try:
        s.connect((HOST,PORT))
    except Exception as es:
        print(e)
        return
    
    while True:
        print('+========命令选项========+')
        print('|****    1.注册      ****|')
        print('|****    2.登录      ****|')
        print('|****    3.退出      ****|')
        print('+========================+\n')

        try:
            cmd = int(input('输入选项：'))
        except Exception as e:
            print('命令错误')
            continue
        
        if cmd not in [1,2,3]:
            print('没有该选项')
            continue
        elif cmd == 1:
            do_register(s)
        elif cmd == 2:
            do_login(s)
        elif cmd == 3:
            s.send(b'E')
            sys.exit('谢谢使用')

def do_register(s):
    while True:
        name = input('User:')
        passwd = getpass.getpass('密码：')
        passwd1 = getpass.getpass('重新输入密码：')
        if (' ' in name) or (' ' in passwd):
            print('用户名或密码不能有空格')
            continue
        if passwd != passwd1:
            print('两次密码不一致')
            continue

        msg = "R %s %s"%(name,passwd)
        #发送请求
        s.send(msg.encode())

        #等待回复
        data = s.recv(128).decode()
        if data == 'ok':
            print('注册成功')
        elif data == 'EXISTS':
            print("该用户已存在")
        else:
            print('注册失败')
        return 


def do_login(s):
    while True:
        name = input('User:')
        passwd = getpass.getpass('密码：')

        msg = "L %s %s"%(name,passwd)

        s.send(msg.encode())
        #等待回复
        data = s.recv(128).decode()
        if data == 'ok':
            print('登录成功')
            login(s,name)
        elif data == 'EXISTS':
            print("该用户不存在")
        else:
            print('密码错误')

def login(s,name):
    while True:
        print('''
        =======查询界面============
        1.查词   2.历史记录  3.退出
        ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝''')

        try:
            cmd = int(input('输入选项：'))
        except Exception as e:
            print('命令错误')
            continue
        
        if cmd not in [1,2,3]:
            print('没有该选项')
            continue
        elif cmd == 1:
            do_register(s)
        elif cmd == 2:
            do_login(s)
        elif cmd == 3:
            return


if __name__ == '__main__':
    main()
