

#示意自定义的类定义为可迭代对象
class MyList:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return "MyList(%s)"%self.data
    def __iter__(self):
        '''要求必须返回迭代器'''
        return MyList_Iterator(self.data)#返回迭代器

class MyList_Iterator:
    '此类用来创建能访问MyList类型对象的迭代器'
    def __init__(self,data):
        #绑定可迭代对象的数据
        self.data=data
        self.cur_index=0  #设置迭代器的起始位置
    def __next__(self):
        '''此方法用来实现迭代器协议'''
        if self.cur_index>=len(self.data):
            raise StopIteration
        r=self.data[self.cur_index]
        self.cur_index+=1
        return r
L=MyList("ABCD")
print(L)
for x in L:
    print(x)