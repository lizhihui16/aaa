from socket import *
#创建tcp套接字
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)
while True:
    c,addr=s.accept()
    print('Connect from',addr)
    data=c.recv(4096)
    print('*******************')
    print(data)
    print("********************")
    #按照ｈｔｔｐ响应格式组织字串
    data='''HTTP/1.1 200 OK
    Content-Encoding: gzip
    Content-Type: text/html

    <h1>Welcome to tedu Python</h1>
    <p>这是一个测试</p>
    '''
    c.send(data.encode()) #发送给浏览器
    c.close()
s.close()