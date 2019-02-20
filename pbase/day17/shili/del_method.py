# 示意析构方法的定义和调用
class car:
    def __init__(self,info):
        self.info=info
        print('汽车',info,'对象被创建')
    def __del__(self):
        '''这是析构方法，形参只有self'''
        print('汽车',self.info,'被销毁')
c1=car('BYD E6')
input("按回车键继续执行程序")
print("程序正常退出")
