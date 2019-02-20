def mydeco(fn):
    def fx():
        print('--------这是fn被调用之前----')
        fn()
        print('--------这是fn被调用之后----')
    return fx
@mydeco
def myfunc():
    print("myfunc被调用！")
myfunc()
myfunc()
myfunc()
# 以上@mydeco等同于在def myfunc之后加了如下语句
# myfunc=mydeco(myfunc)


# 此示例用装饰器改变原来函数的调用流程（业务流程）
# 银行业务
# def privileged_check(fn):
#     def fx(n,x):
#         print('权限验证')
#         fn(n,x)
#     return fx

# def message_send(fn):
#     def fy(n,x):
#         fn(n,x)
#         print('发送消息',n)
#     return fy


# @privileged_check
# def save_money(name,x):
#     print(name,'存钱',x,'元')

# @message_send
# @privileged_check   
# def withdraw(name,x):
#     print(name,'取钱',x,'元')
# # ～～～～～～一下是小张写的程序
# save_money('小王',200)
# save_money('小赵',400)
# withdraw('小李',500)

# 1.输入一个圆的半径，打印出这个圆的面积
# import math
# r=float(input(''))
# s=math.pi*r**2
# print(s)
# 2.输入一个圆的面积，打印出这个圆的半径
# import math as m
# area=float(input(""))
# r=m.sqrt(area/m.pi)
# print(r)

# from math import pi,sqrt
# r=float(input(''))
# s=pi*r**2
# print(s)
# s1=float(input())
# r1=sqrt(s1/pi)
# print(r1)

# import time
# print('这是第一句')
# time.sleep(5)  #让程序睡5秒
# print("这是第二句")

# 写一个程序，输入你的生日
#     1) 算出你已经出生多少天?
#     2) 算出你出生的那天是星期几
# y=int(input('请输入出生时的年：'))
# m=int(input('请输入出生时的月：'))
# d=int(input('请输入出生时的日：'))
# import time
# t=(y,m,d,0,0,0,0,0,0)
# t1=time.mktime(t)
# t2=time.time()
# tx=(t2-t1)//(60*60*24)
# print('您已出生',tx,'天')

# # 用出生时间的UTC秒数
# t=time.localtime(t1)
# d={0:"一",1:'二',2:'三',3:'四',4:'五',5:'六',6:"日"}
# print('您出生的那时是星期：',d[t[6]])





# 练习：
#   1.编写函数fun，其功能是计算下列多项式的和
#   f(n)=1+1/1!+1/2!+1/3!+...+1/n!
# def fun(n):
#     s=1
#     for m in range(1,n+1):
#         y=1
#         for x in range(1,1+m):
#             y*=x
#         s=s+1/y
#     return s
# print(fun(20))

# #或
# def fun(n):
#     from math import factorial as fa
#     y=sum(map(lambda x:1/fa(x),range(n+1)))

#     return y
# print(fun(20))

# 或
# from math import factorial as fac
# def f(n):
#     s=0
#     for x in range(n+1):
#         s+=1/fac(x)
#         return s
# print(f(20))









#   2.写一个程序，以电子时钟格式显示时间：
#   格式：
#   HH:MM:SS  如： 15:58:26
# import time
# def clock_run():
#     while True:
#         t=time.localtime()
#         print('%02d:%02d:%02d'%t[3:6],end='\r')
#         time.sleep(1)
# clock_run()




#   3.编写一个闹钟程序，启动时设置定时时间，到时间后打印"时间到" 然后退出程序

# a=int(input('请输入年：'))
# b=int(input('请输入月：'))
# c=int(input('请输入日：'))
# d=int(input('请输入时：'))
# e=int(input('请输入分：'))
# f=int(input('请输入秒：'))
# import time
# t=(a,b,c,d,e,f,0,0,0)
# t1=time.mktime(t)
# t2=time.time()
# t3=t1-t2
# time.sleep(t3)
# print('时间到')

# def time():

#     import time
#     t=(a,b,c,d,e,f,0,0,0)
#     t1=time.mktime(t)
#     # t2=time.time()
#     while True:
#         t2=time.time()
#         # print(t2)
#         t2=time.localtime(t2)
#         time.sleep(1)
#         print('当前时间',t2[3],':',t2[4],':',t2[5])
#         if t2[5]==f:
#             return "时间到"
#             break

# a=int(input('请输入年：'))
# b=int(input('请输入月：'))
# c=int(input('请输入日：'))
# d=int(input('请输入时：'))
# e=int(input('请输入分：'))
# f=int(input('请输入秒：'))
# print(time())

# import time
# def alarm(h,m):
#     print("闹钟设置时间为%02d:%02d"%(h,m))
#     while True:
#         # t=time.localtime()[3:5]
#         t=time.localtime()
#         t2=t[3:5]
#         if t2==(h,m):
#             print("时间到！！！")
#             break
#         # 显示时间
#         print("%02d:%02d:%02d"%t[3:6],end='\r')
#         # 睡一秒
#         time.sleep(1)


# hour=int(input('请输入小时：'))
# minnute=int(input('请输入分钟：'))
# alarm(hour,minnute)










