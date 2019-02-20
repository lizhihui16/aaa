from multiprocessing import Process
import time 

class Clockprocess(Process):
    def __init__(self,value):
        self.value  = value
        super().__init__()#加载父类
    def run(self):
        for i in range(5):
            print("打印五遍 {}".format(time.ctime()))
            time.sleep(self.value)

p = Clockprocess(3)
p.start()
p.join()