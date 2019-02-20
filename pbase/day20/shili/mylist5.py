



class MyList:
    '''创建一个自定义列表类，此MyList内部用列表来存储信息'''
    def __init__(self,iterable=()):
        self.data=list(iterable)
    def __repr__(self):
        return 'MyList(%s)'%self.data
    def __neg__(self):
        '''重载负号运算符'''
        # return MyList([-x for x in self.data])
        # return MyList((-x for x in self.data))
        return MyList(map(lambda x:-x,self.data))
    def __pos__(self):
        return MyList((abs(x) for x in self.data))


L1=MyList([1,-2,3,-4,5])
L2=-L1
print(L2) 
L3=+L1
print(L3)