
#示意类变量的定义和用法
class car:
    #类变量，用于保存汽车对象的个数
    total_count=0  #创建类变量
print(car.total_count)   # 读取类变量
car.total_count+=100   #修改类变量
print(car.total_count) 

c1=car()
print(c1.total_count)   #100  借助对象访问类变量  
c1.total_count=999      #999 创建实例变量
print(c1.total_count) 
print(car.total_count)    #100
#类变量可以通过此类的对象的 __class__属性间接访问
c1.__class__.total_count=8888
print(c1.total_count)    #999
print(car.total_count)    #8888