#此示例示意递归调用和根据条件结束递归
# def fx(n):
#     print('递归进入第',n,'层')
#     if n==3:
#         return
#     fx(n+1)
#     print('递归退出第',n,'层')
# fx(1)
# print('程序结束')

# 2. 写一个函数myfac 来计算n!(n的阶乘)
#     n! = 1*2*3*4*....*n
# def myfac(n):
#     ....
# print(myfac(5))  # 120

# def myfac(n):
#     s=1
#     for x in range(1,n+1):
#         s*=x
#     return s
# n=int(input('数'))
# print(myfac(n))
# 方法2
# def myfac(n):
#     #如果为1则知道1的阶乘是1，直接返回
#     if n==1:
#         return 1
#     #否则，进入递推阶段等待下一个结果后再返回
#     return n*myfac(n-1)
# print(myfac(88))


# 用递归的方式求1+2+3+....+n的和
# def mysum(n):
#     ...
# print(mysum(100))

# def mysum(n):
#     if n==1:
#         return 1
#     return n+mysum(n-1)
# print(mysum(100))



# 已知有五位朋友在一起，第五位朋友说他比第四位朋友大2岁
# 第四位朋友说他比第三位朋友大2岁
# 第三位朋友说他比第二位朋友大2岁
# 第二位朋友说他比第一位朋友大2岁
# 第一位朋友说他10岁
# 求第n人的年龄
# def getage(n):
#     if n==1:
#         return 10
#     return 2+getage(n-1)
# print(getage(10))


# fdfdxffc nb 


#定义很多函数每个函数求x**y次方，y是可变的
# def pow2(x):
#     return x**2
# def pow3(x):
#     return x**3
# def pow4(x):
#     return x**4
# .....
# def pow99(x):
#     return x**99
#经闭包实现
# def make_power(y):
#     def fn (x):
#         return x**y
#     return fn
# pow2=make_power(2)
# print('5的平方是：',pow2(5))

# 用闭包来创建的任意的
# f(x)=a*x**2+b*x+c的函数
# def get_fx(a,b,c):
#     def Fx(x):
#         return a*x**2+b*x+c
#     return Fx
# f123=get_fx(1,2,3)
# print(f123(20))
# print(f123(50))
# f456=get_fx(4,5,6)
# print(f456(20))
# print(f456(50))




# 3.已知有列表：
# L=[[3,5,8],10,[[13,14],15,18],20]
# 1)写个函数print_list(lst) 打印出所有的数字，即：
#     print_list(L)   #打印3 5 8 13...
# 2)写一个函数sum_list(lst)返回这个列表中所有数字的和
#     print(sum_list(l))  #106
# 注：type(x)可以返回一个变量的类型，如：
# >>>type(20) is int  #True
# >>>type([1,2,3]) is list    #True

# L=[[3,5,8],10,[[13,14],15,18],20]
# def print_list(lst):
#     for n in lst:
#         if type(n) is list:
#             print_list(n)
#         else:
#             print(n,end=' ')
# print_list(L)
# print()
# # 或

# L=[[3,5,8],10,[[13,14],15,18],20]
# def print_list(lst):
#     for n in lst:
#         if type(n) is int:
#             print(n,end=' ')
#         else:
     
#             print_list(n)
# print_list(L)
# print()



L=[[3,5,8],10,[[13,14],15,18],20]
def sum_list(lst):
    s=0
    for n in lst:
        if type(n) is int:
            s+=n
        else:
     
            s+=sum_list(n)
    return s
sum_list(L)
print(sum_list(L))






