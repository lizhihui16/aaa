#    在终端输出图形：
#     **********
#     *        *
#     *        *
#     **********
#     2.一个学生毕业薪资是10000元，每年涨２０％，问十年后他的薪资是多少？
    
# print("**********")
# print("*        *")
# print("*        *")
# print("**********")

# print((1+0.2)**10*10000)




#  制定一个半径r为３厘米的圆
#     １.计算圆的周长？
#     ２.计算圆的面积？
# r=3
# pi=3.14
# s=pi*r**2
# l=2*pi*r
# print(s,l)



# class A(object):
#     def go(self):
#         print("go A go!")
# class B(A):
#     def go(self):
#         super(B, self).go()
#         print("go B go!")
# class C(A):
#     def go(self):
#         super(C, self).go()
#         print("go C go!")
# class D(B,C):
#     def go(self):
#         super(D, self).go()
#         print("go D go!") 
# class E(B,C): 
#     pass
# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
# # a.go()#
# # b.go()#
# # c.go()#
# d.go()#
# # e.go()#


class Parent():
    x=1
class Child1(Parent):
    pass
class Child2(Parent):
    pass

print(Parent.x,Child1.x,Child2.x)
Child1.x=2
print(Parent.x,Child1.x,Child2.x)
Parent.x=3
print(Parent.x,Child1.x,Child2.x)
