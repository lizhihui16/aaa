from multiprocessing import Process,Queue
import time 

#创建消息队列
q = Queue()

#存
def fun1():
    for i in range(10):
        time.sleep(1)
        q.put((1,i))

#取
def fun2():
    for i in range(10):
        time.sleep(2)
        a,b = q.get()
        print("sum = ",a+b)

p1 = Process(target = fun1)
p2 = Process(target = fun2)

p1.start()
p2.start()
p1.join()
p2.join()