# 　２.自己写一个MyList，实现重写len,str,让MyList类型的对象变为可迭代对象
class MyList:
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __repr__(self):
        return "MyList(%s)"%self.data
    def __len__(self):
        '''要求必须返回迭代器'''
        return self.data.__len__()#返回迭代器
    def __str__(self):
        return self.data.__str__()
myl=MyList([1,-2,3,-4])
print(myl)
print(len(myl))       
l=MyList('abcd')
print(l)
 









# 　３.写一个类，Fibonacci实现迭代器协议，此类的对象作为可迭代　对象生成相应的斐波那契数
#     １　１　２　３　５　８　１３....
#     如:
#     class Fibonacci:
#         def __init__(self,n):
#             ...
#         ...
#     实现如下操作:
#         for x in Fibonacci:
#             print(x)
#         L=[x for x in Fibonacci(50)]
#         print(L)
#         print(sum(Fibonacci(100)))

# class Fibonacci:
#     def __init__(self,n):
#         self.count=n  #记录要生成的数据个数
#     def __iter__(self):
#         return FiboIterator(self.count)
# class FiboIterator:
#     '''由迭代器生成Fibonacci数'''
#     def __init__(self,cnt):
#         self.count=cnt
#         self.a=0
#         self.b=1
#         self.cur_count=0    #记录已经生成了多少个
#     def __next__(self):
#         if self.cur_count > self.count:  #生成完毕
#             raise StopIteration
#         v=self.b   #要返回的值
#         #算出下一个数
#         self.a,self.b=self.b,self.a+self.b
#         self.cur_count+=1
#         return v   
# for x in Fibonacci(5):
#     print(x)
# L=[x for x in Fibonacci(50)]
# print(L)
# print(sum(Fibonacci(100)))




# class Fibonacci:
#     def __init__(self,n):
#         self.count=n  #记录要生成的数据个数
#         self.a=0
#         self.b=1
#         self.cur_count=0  
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.cur_count > self.count:  #生成完毕
#             raise StopIteration
#         v=self.b   #要返回的值
#         #算出下一个数
#         self.a,self.b=self.b,self.a+self.b
#         self.cur_count+=1
#         return v   
# for x in Fibonacci(5):
#     print(x)
# L=[x for x in Fibonacci(50)]
# print(L)
# print(sum(Fibonacci(100)))
