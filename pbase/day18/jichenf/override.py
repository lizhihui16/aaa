
#示意覆盖的语法
class A:
    def work(self):
        print('A.work被调用')
class B(A):
    def work(self):
        print('B.work被调用')
b=B()
b.work()  #B.work被调用
a=A()
a.work()   #A.work被调用

b=B()
b.work()
A.work(b)