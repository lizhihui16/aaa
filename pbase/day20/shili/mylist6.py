class MyList:
    '''创建一个自定义列表类，此MyList内部用列表来存储信息'''
    def __init__(self,iterable=()):
        self.data=list(iterable)
    def __repr__(self):
        return 'MyList(%s)'%self.data
    def __contains__(self,e):
        '''重载in运算符，只需要判断e是否在self里'''
        return e in self.data

L1=MyList((1,-2,3,-4,5))

print(3 in L1) 
print(3 not in L1)
print(4 in L1) 
print(4 not in L1)