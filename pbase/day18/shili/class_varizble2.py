

class car:
    #类变量，用于保存汽车对象的个数
    total_count=0
    def __init__(self,info):
        self.info=info
        print('汽车',info,'被创建')
        self.__class__.total_count+=1
    def __del__(self):
        print('汽车',self.info,'被销毁')
        # self.__class__.total_count-=1
        car.total_count-=1
c1=car('BYD E6')
c2=car('吉利 E7')
print('当前有%d个汽车对象'%car.total_count)

del c2
print(car.total_count)