# ------------函数变量
# def fn():
#     print('hello world')
# f1=fn
# print(f1)
# fn()
# f1()
# f2=fn()
# print(f2)
# ~~###########~ ~###############~~~~~~`
# def f1():
#     print('hello f1')
# def f2():
#     print('hello f2')
# f1,f2=f2,f1
# f1()
#############!~~~~~~@@@@@@@@@~~~~~
# def f1():
#     print('hello f1')
# def f2():
#     print('hello f2')
# def fx(fn):
#     print(fn)
#     fn()
# fx(f1)
# ~~~~############~~~~~@@@@@@@@
# def goodbye(L):
#     for x in L:
#         print('再见:',x)
# def hello(L):
#     for x in L:
#         print('您好:',x)
# def fx(fn,L):
#     fn(L)
# fx(goodbye,['Tom','Jerry','Spike'])
# ~~~~~~~~~~~~##########~~~~~~~~~~#
# def myinput(fn):
#     L=[1,3,5,7,9]
#     r=fn(L)
#     return  r
# print(myinput(max))
# print(myinput(min))
# print(myinput(sum))
#~~~~~~~~~~~#########~~~~~~~~~#
# def get_function():
#     s=input('请输入您要的操作:')
#     if s=='求最大':
#         return max
#     if s=='求最小':
#         return min
#     if s=='求和':
#         return sum
# L=[2,4,6,8,10]
# f=get_function()
# print(f(L))

# ```````函数嵌套###?
# def fn_outter():
#     print('fn_outter被调用')
#     def fn_inner():
#         print('fn_inner被调用')
#     fn_inner()
#     fn_inner()
#     print('fn_outter调用结束')
# fn_outter()  


# def fn_outter():
#     print('fn_outter被调用')
#     def fn_inner():
#         print('fn_inner被调用')
#     fn_inner()
#     fn_inner()
#     print('fn_outter调用结束')
#     return fn_inner
# f=fn_outter()  
# f()
# ~~~~~~~~~~python的作用域~~~~~``
# v=100
# def f1():
#     v=200
#     print('f1.v=',v)
#     def f2():
#         v=300
#         print("f2.v=",v)
#     f2()
# f1()
# print('全局的v=',v)




# 得出下列程序运行的结果,思考为什么?
# L=[1,2]
# def f1():
#     L=[3,4,5]
# f1()
# print(L)   #[1,2]
# def f2():
#     L+=[3,4,5]
   
# f2()
# print(L)   #出错
# def f3():
#     L[:]=[3,4,5]
#     print(L)
# f3()
# print()  #[3,4,5]

# ～～～～～～######global语句～～～～～～～～#
# v=100
# def f1():
#     global v
#     v=200
# f1()
# print('v=',v)


# 写一个函数hello，部分代码如下：
# count=0
# def hello(name):
#     print('您好',name)
#     ....
# 当调用hello函数时，全局变量count自动做加1操作来记录hello被调用的次数
# 如：
#     hello("Tom")
#     hello("Jerry")
#     print("hello函数共被调用%d次“ % count)

# count=0
# def hello(name):
#     print('您好',name)
#     global count
#     count+=1
# hello("Tom")
# hello("Jerry")
# print("hello函数共被调用%d次" % count)


# 示例～～～～######nonlocal～～～～
# var=100
# def f1():
#     var=200
#     print("f1.var=",var)   #200
#     def f2():
#         var=300
#         print("f2.var=",var)  #300
#     f2()
#     print("f1.var=",var)  # 200
# f1()

# var=100
# def f1():
#     var=200
#     def f2():
#         var=300
#         def f3():
#             nonlocal var
#             var=400
#         f3()
#         print(var)
#     f2()
# f1()
# ～～～～～～～lambda~~~~~~
# def myadd(x,y):
#     return x+y
# 用lambda改写
# myadd=lambda x,y:x+y
# print("20+30=",myadd(20,30))
# print("100+200=",myadd(100,200))


# 1.写一个lambda表达式：fx=lambda n:...
# 此表达式创建的函数判断n这个数的2次方+1能否被5整除，如果能整除返回
# True，否则返回False
# 如：
#     print(fx(3))
#     print(fx(4))
# fx=lambda x: True if (x**2+1)%5==0 else False 
# print(fx(3))
# print(fx(4))
# ～～～～～～～～～～～？
# 2.返回两个数的最大值
# def mymax(x,y):
#     return x if x>y else y
# # mymax=lambda x,y:max(x,y)
# print(mymax(100,200))
# print(mymax("ABC","123"))

# ~~~~~~~~ecal函数用法！！！！！？
# x=100
# y=100
# s='x+y'
# v=eval(s)
# print(v)   #300
# # 假设局部作用域内有x=1；y=2
# v2=eval(s,None,{'x':1,'y':2})
# print(v2)
# #局部有y=2,全局作用域有：x=10,y=20
# v3=eval(s,{'x':10,'y':20},{'y':2})
# print(v3)


# 1.看懂下面的程序在做什么
# def fx(f,x,y):
#     print(f(x,y))
# fx((lambda a,b:a+b),100,200)
# fx((lambda a,b:a**b),3,4)

# 1. 写一个函数mysum(n), 给出一个数n写一个函数来计算
#     1 + 2 + 3 + 4 + ...... + n的和
#     (要求用函数来做)
# def mysum(n):
#     ....
# print(mysum(100))  # 5050
# ～～～～～～～～＃＃＃＃＃＃～～～～～～～～～
# 方法１
# def mysum(n):
#     s=0
#     for x in range(n+1):
#         s+=x
#     return s
# n=int(input('数'))
# print(mysum(n))
# 方法２
# def mysum(n):
#     return sum(range(1,n+1)):
# n=int(input('数'))
# print(mysum(n))
# ~~~~~~~~~~~############~~~~~~~~~~~~~~~~#
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


# 3. 给出一个数n, 写一个函数计算:
# 1 + 2**2 + 3**3 + 4**4 + .... .+ n**n的和  
# (n给个小点的数)
# def f1(n):
#     s=0
#     for x in range(1,n+1):
#         s=s+x**x
#     return s
# n=int(input('数'))
# print(f1(n))
# 方法22
# def f(n):
#     return sum(map(lambda x: x**x,range(1,n+1)))
# n=int(input('数'))
# print(f(n))



# 5.写程序打印杨辉三角（只打印6层) 
#         1
#        1 1
#       1 2 1
#      1 3 3 1
#　　　1 4 6 4 1
#    1 5 10 10 5 1



def get_next_list(L):
    #用给定的一行，返回下一行
    #如L=[1,2,1],则返回【1,3,3,1】
    rl=[1]  #  最左边的1
    #算中间的数字（循环获取从0开始索引）
    for i in range(len(L)-1):
        v=L[i]+L[i+1]
        rl.append(v)
    rl.append(1)
    return rl
#生成全部的行放到一个整体的列表L中，并返回
def yh_list(n):   #n为行数
    rl=[]
    L=[1]
    while len(rl)<n:
        rl.append(L)
        L=get_next_list(L)  #计算出下一行
    return rl
#把杨辉三角的列表转为字符串列表
def get_yh_string(L):
    rl=[]
    for line in L:
        s=' '.join([str(x for x in line)])
        rl.append(s)
    return rl
def print_yh_triangle(L):
    max_len=len(L[-1])
    for s in L:
        print(s.center(max_len))

L=yh_list(6)
SL=get_yh_string(L)
print_yh_triangle(SL)
# print(get_yh_string(L))





# def f():
#     L=[1,2,3]
#     return L
# L=f()
# print(f())





















