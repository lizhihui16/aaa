from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0',8988))
s.listen(3)

#关注套接字
print('监控IO')
rs,ws,xs = select([s],[],[],3)
print('处理IO')