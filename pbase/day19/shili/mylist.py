
class MyList:
    '''创建一个自定义列表类，此MyList内部用列表来存储信息'''
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return 'MyList(%s)'%self.data
    def __len__(self):
        '''方法必须返回整数'''
        # return len(self.data)
        return self.data.__len__()
    def __abs__(self):
        '''此方法实现把sekf的所有元素取绝对值后返回全为正数的自定义列表'''
        lst=[abs(x) for x in self.data]
        L=MyList(lst)    #创建新的列表
        return L
myl=MyList([1,-2,3,-4])
print(myl)
print(len(myl))

myl3=abs(myl)
print(myl3)

# myl2=MyList([])
# print(myl2)