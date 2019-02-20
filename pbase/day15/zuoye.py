# 练习：
#   １．打印９＊９乘法表。
#     １×１＝１
#     １＊２＝２　２＊２＝４
#     １＊３＝３　２＊３＝６　３＊３＝３
#     ...
#     1*9=9 ...                         9*8=81
# for x in range(1,10):
#     for y in range(1,x+1):
#         z=x*y
#         print('%d×%d=%d'%(y,x,z),sep='',end=' ')
#     print()
#   2.写一个生成器函数 myrange(start,stop,step) 来生成一系列整数
#      要求:
#        myrange功能与range功能完全相同
#        不允许调用range(函数)
#      然后用自己写的myrange结合生器表达式求1~100内奇数的平方和

# def myrange(start,stop=None,step=1): 
#     if stop is None:
#         stop=start
#         start=0
#     if step>0:
#         while start<stop:
#             yield start
#             start+=step
#     elif step<0:
#         while start>stop:
#             yield start
#             start+=step            

# L=[x**2 for x in myrange(1,100,2)]
# print(sum(L))



# def myrange(start,stop,step): 
#     while True:
#         if start<stop:
#             yield start
#             start+=step
#         else:
#             break
# stop=int(input(""))
# try:
#     start=int(input(""))
# except:
#     start=0
# try:
#     step=int(input(""))
# except:
#     step=1
# finally:
#     for x in myrange(start,stop,step):
#         x
#         print(x,end=' ')
# print()


# s=0
# for x in myrange(1,100,2):
#     s+=(x**2)
# print(s)




#   ３.写一个myfilter生成器函数，功能与filter函数功能完全相同
#   　如：
#       def myfilter(fn,iter1):
#          ...
#       L=[x for x in myfilter(lambda x: x%2, range(10))]
#           #  L=[1,3,5,7,9]
# def myfilter(fn,iter1):
#     L=[]
#     while True:
#         for y in iter1:
#             if fn(y)==True:
#                 L.append(y)
#                 return L
#         # else:
#             #     myfilter(fn,iter1)

# print(myfilter(lambda x: x%2==1,range(10)))
# # #     #  L=[1,3,5,7,9]          


# def myfilter(fn,iter1):
#     for x in iter1:
#         if fn(x)==True:
#             yield x
# L=[x for x in myfilter(lambda x: x%2, range(10))]
# print(L)



# def isodd(x):
#     return x%2==1
# for x in filter(isodd,range(100)):
#     print(x)
# 练习：
# 　把１－１００之间的全部素放在列表ｐｒｉｍｅs中
    # def isprime(x):
    #     if x<2:
    #         return False
    #     for i in range(2,x):
    #         if x%i==0:
    #             return False
    #     return True
    # primes=[x for x in filter(isprime,range(1,100))]
    # print(primes)


#   4.将以前所有练习自己不看之前的代码重写一遍
