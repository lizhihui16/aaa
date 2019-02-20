


#运算符重载
# class MyNumber:
#     def __init__(self,value):
#         self.data=value
#     def __repr__(self):
#         return 'MyNumber(%d)' % self.data
#     def add(self,other):
#         v=self.data+other.data
#         obj=MyNumber(v)  #创建一个新对象
#         return obj
# n1=MyNumber(100)
# n2=MyNumber(200)
# print(n1)
# n3=n1.add(n2)
# print(n1,'+',n2,'=',n3)    # MyNumber(100) + MyNumber(200) = MyNumber(300)



# class MyNumber:
#     def __init__(self,value):
#         self.data=value
#     def __repr__(self):
#         return 'MyNumber(%d)' % self.data
#     def __add__(self,other):
#         v=self.data+other.data
#         obj=MyNumber(v)  #创建一个新对象
#         return obj
#     def __sub__(self,rhs):        
#         return MyNumber(self.data-rhs.data)

# n1=MyNumber(100)
# n2=MyNumber(200)
# print(n1)
# n3=n1+n2    #等同于n1.__add__(n2)
# print(n1,'+',n2,'=',n3)    # MyNumber(100) + MyNumber(200) = MyNumber(300)
# n4=n1-n2
# print(n1,'-',n2,'=',n4)



# 实现两个自定义的列表相加操作
# class MyList:
#   ...
# L1=myList(range(1,4))
# L2=MyList([4,5,6])
# L3=L1+L2
# print(L3)   #MyList([1,2,3,4,5,6])
# L4=L2+L1
# print(L4)   #MyList([4,5,6,1,2,3])
# L5=L1*3
# print(L5)   #MyList([1,2,3,1,2,3,1,2,3])

# class MyList:
#     '''创建一个自定义列表类，此MyList内部用列表来存储信息'''
#     def __init__(self,iterable=()):
#         self.data=list(iterable)
#     def __repr__(self):
#         return 'MyList(%s)'%self.data
#     def __add__(self,rhs):
#         return MyList(self.data+rhs.data)
#     def __mul__(self,rhs):        
#         return MyList(self.data*rhs)

# # 或
# # class MyList:
# #     def __init__(self,ite=()):
# #         self.data=[x for x in ite]
# #     def __repr__(self):
# #         return 'MyList(%s)'%self.data
# #     def __add__(self,other):
# #         v=self.data+other.data
# #         obj=MyList(v)  #创建一个新对象
# #         return obj
# #     def __mul__(self,rhs):        
# #         return MyList(self.data*rhs)
        
# L1=MyList(range(1,4))
# L2=MyList([4,5,6])
# L3=L1+L2
# print(L3)   #MyList([1,2,3,4,5,6])
# L4=L2+L1
# print(L4)   #MyList([4,5,6,1,2,3])
# L5=L1*3
# print(L5)   #MyList([1,2,3,1,2,3,1,2,3])









class MyList:
    def __init__(self,ite=()):
        self.data=[x for x in ite]
    def __repr__(self):
        return 'MyList(%s)'%self.data
    def __add__(self,other):
        v=self.data+other.data
        obj=MyList(v)  #创建一个新对象
        return obj
    def __rmul__(self,lhs):        
        return MyList(self.data*lhs)
        
L1=MyList(range(1,4))
L2=MyList([4,5,6])
L3=L1+L2
print(L3)   #MyList([1,2,3,4,5,6])
L4=L2+L1
print(L4)   #MyList([4,5,6,1,2,3])
L5=3*L1
print(L5)   #MyList([1,2,3,1,2,3,1,2,3])
