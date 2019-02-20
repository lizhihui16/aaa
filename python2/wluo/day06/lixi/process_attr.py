
from multiprocessing import Process
from time import sleep,ctime 


def tm():
    for i in range(4):
        sleep(2)
        print(ctime())

p = Process(target = tm,name = 'Tarena')

p.daemon = True

p.start()
print('名字',p.name)
print('Process PID',p.pid)
print('Process alive',p.is_alive())
# p.join()