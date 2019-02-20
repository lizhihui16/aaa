
import multiprocessing as mp
from time import sleep
import os
#编写进程函数
def th1():
    sleep(3)
    print('吃饭')
    print(os.getppid(),'--',os.getpid())

def th2():
    sleep(4)
    print('睡觉')
    print(os.getppid(),'--',os.getpid())
def th3():
    sleep(1)
    print('工作')
    print(os.getppid(),'--',os.getpid())
#创建进程对象
things=[th1,th2,th3]
m = []
for th in things:
    p = mp.Process(target = th)
    m.append(p)
    #启动进程
    p.start()
for i in m:
    #回收进程
    p.join()