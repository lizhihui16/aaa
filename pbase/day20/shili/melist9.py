class MyList:
    '''创建一个自定义列表类，此MyList内部用列表来存储信息'''
    def __init__(self,iterable=()):
        self.data=list(iterable)
    def __repr__(self):
        return 'MyList(%s)'%self.data
    def __getitem__(self,i):
        if type(i) is int:
            print("您正在做索引操作")
        elif type(i) is slice:
            print('您正在执行切片重载')
            print("起始值",i.start)
            print("终止值",i.stop)
            print("步长",i.step)

        return self.data[i]
L1=MyList([1,-2,3,-4,5])
x=L1[1::2]
print(x)
x=L1[3]
print(x)