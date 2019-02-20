# from multiprocessing import Pool
# from time import sleep,ctime

# l=[]
# def worker(msg):
#     sleep(2)
#     print(msg)
#     return ctime()
# #创建进程池
# pool = Pool(processes=3)

# #向进程池添加事件
# for i in range(10):
#     msg = 'hello %d'%i
#     r=pool.apply_async(func = worker,args = (msg,))
#     l.append(r)
# #关闭进程池
# pool.close()
# pool.join()
# for i in l:
#     print(i.get())






from multiprocessing import Pool
from time import sleep 

def worker(msg):
    sleep(2)
    print(msg)
#创建进程池
pool = Pool()

#向进程池添加事件
for i in range(10):
    msg = 'hello %d'%i
    #同步执行，一个一个执行
    pool.apply(func = worker,args = (msg,))
#关闭进程池
pool.close()
pool.join()