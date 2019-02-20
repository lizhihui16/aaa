from socket import *
import random



s = socket()

s.bind('0.0.0.0',8888)
s.listen(5)
while True:
    c,addr = accept()
    co = random.choice(['石头','剪刀','布'])
    print(co)
    while True:
        data = c.recv(1024)
        if not data:
            break
        elif data==co:
            n = c.send(b'平‘)
        elif 

