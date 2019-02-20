import os
from time import sleep

print('***************')
a = 1
pid = os.fork()

if pid< 0:
    print("Create process failed")
elif pid == 0:
    print("撒旦法律框架内")
    print("a = %d"%a)  #子进程会复制父进程的所有
    a = 10000
else:
    sleep(1)
    print("爱爱科技")
    print("Parent a = ",a)
