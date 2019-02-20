


class MyList:
    '''创建一个自定义列表类，此MyList内部用列表来存储信息'''
    def __init__(self,iterable=()):
        self.data=list(iterable)
    def __repr__(self):
        return 'MyList(%s)'%self.data
    def __getitem__(self,i):
        return self.data[i]
    def __setitem__(self,i,v):
        # print(i,v)
        self.data[i]=v
    def __delitem__(self, i):
        del self.data[3]

L1=MyList([1,-2,3,-4,5])
x=L1[2]
print(x)
L1[1]=2.2
print(L1)
del L1[3]
print(L1)