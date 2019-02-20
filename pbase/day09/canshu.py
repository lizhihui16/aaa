#     print('a的值是:',a)
#     print('b的值是:',b)
#     print('c的值是:',c)
# mymin(1,2,3)#位置传参
# mymin(4,5,6) #位置传参

# s1=[11,22,33]
# mymin(s1[0],s1[1],s1[2])  #序列传参
# mymin(*s1)#序列传参   fun1(11,22,33)

# s2=(44,55,66)
# s3="ABC"
# mymin(*s2)   #序列传参
# mymin(*s3)    #序列传参

# mymin(c=300,b=200,a=100)      #关键字传参
# mymin(b=20, c=30,a=10)       #关键字传参
# mymin(c=3,b=2,d=1)  #报错

# d1={'c':33,'b':22,'a':11}
# mymin(**d1)                #字典关键字传参
# d2={'c':33,'b':22,'d':11}
# mymin(**d2)      #  报错

# ------------缺省参数
# def info (name,age=1,address='不详'):
#     print(name,'今年',age,'岁','家庭住址:',address)
# info('魏明泽',35,'北京市朝阳区')
# info('Tarena',16)
# info('张飞')


# 写一个程序myadd,此函数可以计算两个数,三个数和四个数的和
# 如:
# def myadd(a,b,c=0,d=0):
#     z=a+b+c+d
#     return z
# print(myadd(10,20))
# print(myadd(100,200,300))
# print(myadd(1,2,3,4))


# --------------星号元组形参
# def func(*args):
#     print("用户传入的参数是:",len(args))
#     print('args=',args)
# func()
# func(1,2,3)
# func(1,2,3,'AAA',"BBB",'CCC')

# 写一个函数,mysum可以传入任意个数字的实参,此函数调用将返回实参的和
# 如:
# def mysum(...):
#     ...
# print(mysum())
# print(mysum(1,2,3))

# def mysum(*args):
#     # return sum(args)
#     s=0
#     for x in args:
#         s+=x
#     return s
# print(mysum())
# print(mysum(1,2,3))

# 2.写一个函数min_max()函数,此函数至少要传入一个参数,并返回全部这些数数
# 的最大值,最小值(形成元组,最小值在前,最大值在后),调用此回函数,得到最小值
# 和最大值并打印出来
# 如:
# def min_max(...):
#     ,,,
# print(min_max(10,20,30))
# x,y=min_max(8,6,4,3,9,2,1)
# print('最小值:',x)
# print('最大值:',y)
# print(min_max())

# def min_max(a,*args): 
# #     # return(min(a,min(args)),max(a,max(args)))
# #     return(min(a,*args),max(a,*args))

# # 或
#     # z=a
#     # m=a
#     # for x in args:
#     #     if z>x:
#     #         z=x
#     #     if m<x:
#     #         m=x
#     # return (z,m)
# print(min_max(10,20,30))
# x,y=min_max(8,6,4,3,9,2,1)
# print('最小值:',x)
# print('最大值:',y)
# # print(min_max())


# --------------命名关键字传参
# def f1(*,c,d):
#     print('c=',c)
#     print('d=',d)
# f1(3,4)     #报错
# f1(d=4,c=3)   #正确
# d1={'c':30,'d':40}
# f1(**d1)


# def f2(a,b,*args,c,d):
#     print(a,b)
#     print(args)
#     print(c,d)
# f2(1,2,3,4,d=200,c=100)
# f2(11,22,33,**{'c':11,'d':22})


# --------------双星号形参
# def fun(**kwargs):
#     print("关键字传参个数是",len(kwargs))
#     print('kwargs=',kwargs)
# fun(a=1,b='BBBB',c=[2,3,4])   #关键字传参
# fun()



# def fun(*args,**kwargs):
#     print(args)
#     print('kwargs=',kwargs)
# fun(2,3,4,5,a=1,b='BBBB',4,45,6,87,c=[2,3,4])



# print()
# print(1,2,3,4)
# print(1,2,3,4,sep='#')
# # print(1,2,3,4,sep='#',end='\n\n')
# print()



# 写一个myrange函数,参数可以传入1-3个,实际含义与range 函数相同
# 此函数返回range(...)函数列表
# 如:
#     L = myrange(4)
#     print(L)  # [0, 1, 2, 3]
#     L = myrange(4, 6)
#     print(L)  # [4, 5]
#     L = myrange(1, 10, 3)
#     print(L)  # [1, 4, 7]
#     (注:可以调用range)
# def myrange(a,b=None,c=None):
#     if b is None:
#         start=0   #开始为0
#         stop=a    #结束为0,定义变量
#     else:
#         start=a
#         stop=b
#     if c is None:
#         step=1
#     else:
#         step=c
#     print('开始值:',start,'结束值:',stop,'步长:',step)
#     return list(range(start,stop,step))
# print(myrange(4))
# print(myrange(4,6))
# print(myrange(1,10,3))

# ----------全局变量和局部变量--------------
# a=100
# b=200
# def fx(c):
#     d=400
#     print(a,b,c,d)
# fx(300)
# print('a=',a)
# print('b=',b)


# -----------
# a=1
# b=2
# c=3
# def fn(c,d):
#     e=300
#     print("locals()返回:",locals())
#     print("globals()返回:",globals())
#     print(c)  #访问局部变量100
#     print(globals()['c'])      #访问全局变量c
# fn(100,200)




# 素数/质数
# 2,3,5,7,11,13
# 1.写一个函数isprime(x)判断x是否是素数,如果是素数返回True,否则返回False
#     def isprime(x):
#     ...
#     print(isprime(4))  #False
#     print(isprime(5))  #True
# 方法1
# def isprime(x):
#     if x>=2:
#         for a in range(2,x):
#             if x%a==0:
#                 print('False')
#                 break
#         else:
#             print('True')
#     else:
#         print('False')
# x=int(input(""))
# isprime(x)
#方法2
def isprime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
print(isprime(2))
# 2.写一个函数prime_m2n(m,n)返回从m开始,到n结束的范围内的素数(不包含n),返回
# 这些素数的列表,并打印
# 如:
# L=prime_m2n(5,10)
# print(L)   #[5,7]
#方法1
def prime_m2n(m,n):
    L=[]
    for x in range(m,n):
        if isprime(x):
            L.append(x)
    return L
L=prime_m2n(5,10)
print(L)
# 方法2

# L=[]
# def prime_m2n(m,n):
#     for x in range(m,n):
    
#         if x>=2:
#             for a in range(2,x):
#                 if x%a==0:
#                     break
#             else:
#                 L.append(x)
#     return L

# m=int(input(''))
# n=int(input(''))
# prime_m2n(m,n)
# print(L)

# 3.写一个函数primes(n)返回指定范围n以内的素数(不包含n)的全部素数的列表,并打印
# L=primes(10)
# print(L)   #[2,3,5,7]
#     1)打印100以内的全部素数
#     2)打印200以内的全部素数的和
# 方法1 
def primes(n):
    return prime_m2n(0,n)
L=primes(10)
print(L)
# L=[]
# def primes(n):
#     for x in range(n):
    
#         if x>=2:
#             for a in range(2,x):
#                 if x%a==0:
#                     break
#             else:
#                 L.append(x)
#     return(L,sum(L))
# n=int(input(''))
# primes(n)
# print(L)
# print(sum(L))



# 4)改下之前的学生信息管理程序:改为用两个函数实现
#     1.写函数input_student()来获取学生信息,当输入姓名为空时结束输入,形成字典组成
#     的列表并返回
#     2.写函数print_student(L)将上述函数得到的打印成为表格显示
#     如:
#     def input_student():
#         ...
#     def print_student(L):
#         ...
#     L=input_student()
#     print(L)
#     print_student(L)
# ##########
# def input_student():
#     L=[]
#     while True:
#         n=input('请输入姓名: ')
#         if not n:#姓名为空结束输入
#             break
#         a=int(input('请输入年龄: '))
#         s=int(input('请输入成绩: '))
#         d={}
#         d['name']=n
#         d['age']=a
#         d['score']=s      
#         L.append(d)
#         # print(L)
#     return L
# def print_student(L):
#     print('+---------------+----------+----------+')
#     print('|      name     |    age   |  score   |')
#     print('+---------------+----------+----------+')
#     for d in L:
#         # line='|'+d['name'].center(15)
#         # line='|'+str(d['age']).center(11)
#         # line='|'+str(d['score']).center(9)+'|'
#         line='|'+d['name'].center(15)+'|'+str(d['age']).center(10)+'|'+str(d['score']).center(10)+'|'
#         print(line)
#     print('+---------------+----------+----------+')
# L=input_student()
# print(L)
# print_student(L)    



