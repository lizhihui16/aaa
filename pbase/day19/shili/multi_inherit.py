

#示意多继承标识符冲突的问题

class A:
    def m(self):
        print('A.m被调用')
class B:
    def m(self):
        print('B.m被调用')
class AB(A,B):
    pass
ab=AB()
ab.m()