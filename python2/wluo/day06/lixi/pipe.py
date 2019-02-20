# from multiprocessing import Process,Pipe
# import os,time

# #创建管道对象
# fd1,fd2 = Pipe()
# def fun(name):
#     time.sleep(3)
#     #写
#     fd1.send(name)
# jobs = []
# for i in range(5):
#     p = Process(target = fun,args = (i,))
#     jobs.append(p)
#     p.start()

# for i in range(5):
#     #读
#     data = fd2.recv()
#     print(data)

# for i in jobs:
#     i.join()





from multiprocessing import Process,Pipe
import os,time

#创建管道对象
#如果为单项管道fd1-->recv
#            fd2-->send
fd1,fd2 = Pipe(False)
def fun(name):
    time.sleep(3)
    #写
    fd2.send(name)
jobs = []
for i in range(5):
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()

for i in range(5):
    #读
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()