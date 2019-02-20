# a = 1
# def fun(a):
#     a = 2
# fun(a)
# print(a) # 1

# a = []
# def fun(a):
#     a.append(1)
# fun(a)
# print(a) # [1]

# class Person:
#     name="aaa"
# p1=Person()
# p2=Person()
# p1.name="bbb"
# print(p1.name) # bbb
# print(p2.name) # aaa
# print(Person.name) # aaa
# print(Person.name) # aaa


# class MyClass():
#     def __init__(self):
#         self.__superprivate = "Hello"
#         self._semiprivate = ", world!"
# mc = MyClass()
# # print(mc.__superprivate)
# print(mc._semiprivate)





# class Node(object):
#     def __init__(self,sName):
#         self._lChildren = []
#         self.sName = sName
#     def __repr__(self):
#         return "<Node '{}'>".format(self.sName)
#     def append(self,*args,**kwargs):
#         self._lChildren.append(*args,**kwargs)
#         print(self._lChildren)

#     def print_all_1(self):
#         print(self)
#         for oChild in self._lChildren:
#             oChild.print_all_1()
#     def print_all_2(self):
#         def gen(o):
#             lAll = [o,]
#             while lAll:
#                 oNext = lAll.pop(0)
#                 lAll.extend(oNext._lChildren)
#                 yield oNext
#         for oNode in gen(self):
#             print(oNode)
# oRoot = Node("root")
# oChild1 = Node("child1")
# oChild2 = Node("child2")
# oChild3 = Node("child3")
# oChild4 = Node("child4")
# oChild5 = Node("child5")
# oChild6 = Node("child6")
# oChild7 = Node("child7")
# oChild8 = Node("child8")
# oChild9 = Node("child9")
# oChild10 = Node("child10")
# oRoot.append(oChild1)
# oRoot.append(oChild2)
# oRoot.append(oChild3)
# oChild1.append(oChild4)
# oChild1.append(oChild5)
# oChild2.append(oChild6)
# oChild4.append(oChild7)
# oChild3.append(oChild8)
# oChild3.append(oChild9)
# oChild6.append(oChild10)

# # oRoot.print_all_1()
# oRoot.print_all_2()



# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return b

# n=int(input(''))
# c=fib(n)
# print(c)



# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
            
#             cls._instance = orig.__new__(cls, *args, **kw)
#             print(orig)
#         return cls._instance
# class MyClass(Singleton):
#     a = 1
# f=Singleton()
# print(f)




# import re
# p=re.compile('blue|white|red')
# print(p.sub('colour','blue socks and red shoes'))    # colour socks and colour shoes


# reduce(lambda x,y:x*y,range(1,4))


A0=dict(zip(('a','b','c','d','1'),(1,2,3,4,5)))
A1=range(10)




A2=[i for i in A1 if i in A0]
# A3=[A0[s] for s in A0]
# A4=[i for i in A1 if i in A3]
# A5={i:i*i for i in A1}
# A6=[[i,i*i] for i in A1]
print(A0)
print(A2)
# print(A3)
# print(A4)
# print(A5)
# print(A6)
