class MyList:
    '''创建一个自定义列表类，此MyList内部用列表来存储信息'''
    def __init__(self,iterable=()):
        self.data=list(iterable)
    def __repr__(self):
        return 'MyList(%s)'%self.data
    # def __add__(self,rhs):
    #     return MyList(self.data+rhs.data)
    def __iadd__(self,rhs):
        self.data.extend(rhs.data)
        return self
    def __mul__(self,rhs):        
        return MyList(self.data*rhs)
L1=MyList(range(1,4))
L2=MyList([4,5,6])
L1+=L2
print(L1)   #MyList([1,2,3,4,5,6])
print(L2) 