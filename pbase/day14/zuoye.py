# 1. 一个球从100米高空落下，每次落地后反弹高度为原高度的一半，再落下，写程序
#     1) 算出皮球在第10次落地后反弹多高
#     2) 打印10次皮球反弹后共经历了多少米路程

# 方法１
# def get_last_height(meter,times):
#     for _ in range(times):
#         meter/=2
#     return  meter
# print("球第１０次落地后的高度",get_last_height(100,10))
# def get_distance(meter,times):
#     s=0
#     for _ in range(times):
#         #记录下落时行程
#         s+=meter
#         #算出反弹高度
#         meter/=2
#         #记录反弹的行程
#         s+=meter
#     return  s
# print('球在第１０次反弹后总行程是：',get_distance(100,10),'米')
# ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃?
# 方法２
# def pl(n):
#     h=100
#     i=0
#     while True:
#         if i!=n:
#             h=h/2
#             i+=1
#         else:
#             break
#     return h
# def lc():
#     global n
#     s=100
#     m=1
#     while True:
#         if n!=m:
#             s=s+pl(m)*2
#             m+=1
#         else:
#             s=s+pl(m)
#             break
#     return s
# n=int(input(''))
# print(pl(n))
# print(lc())



# 2. 分解质因数,输入一个正整数，分解质因数
#     如输入: 90 则打印:
#     90 = 2*3*3*5
#     (质因数是指最小能被原数整除的素数(不包含1))
# 方法１
def get_zhiyin_list(x):
    '''此函数将返回包含x的所有质因数的列表
    如：x=90
    则返回[2,3,3,5]
    '''
    L=[]
    #循环查找质因数，如果找到质因数就加入到L列表中，直到x等于１为止
    while x>1:
        #以下循环只找一个质因数，找到以后循环停止，再返回上面的循环
        for i in range(2,x+1):
            if x%i==0:
                L.append(i)
                x=int(x/i)
                break
    return L
n=int(input(""))
L=get_zhiyin_list(n)
s='*'.join((str(x) for x in L))
print(n,'=',s)
# ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃3##########3#
# 方法２
# l=[]
# n=int(input(""))
# a=[]
# def f(n):
#     global a
#     global l
#     b=0
#     if n<2:
#         print("不能分解质因数")
#     else:
#         for x in range(2,n):
#             if n%x==0:
#                 b=int(n/x)
#                 l=[x,int(n/x)]
#                 a.append(l[0])
#                 if l[1]==l[0]:
#                     a+=l[1:2]
#                     break
#                 else:
#                     f(l[1])
#                     break
#         else:
#             a+=[n]
#         # break
#     return a
# c=f(n)
# print(c)
# s = '*'.join([str(x) for x in c])
# print("%d = %s" % (n,s))
