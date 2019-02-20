


# 示意多继承的语法
class Car:
    def run(self,speed):
        print('汽车以',speed,'Km/h的速度')
class Plane:
    def fly(self,height):
        print('飞机以海拔',height,'米高度飞行')
class PlaneCar(Car,Plane):
    '''PlaneCar类同时继承自汽车类和飞机类'''

p1=PlaneCar()
p1.fly(10000)
p1.run(300)