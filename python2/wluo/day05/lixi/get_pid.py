import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('asd')
elif pid == 0:
    sleep(1)
    print("CHild PID",os.getpid())
    print(os.getppid())#父进程的PID号
else:
    print("Parent PID",os.getpid())
    print(pid)  #子进程PID号
