# # 已知有列表:
# # L=[3,5]
# # 用索引的切片等操作,将原列表改变为:
# # L=[1,2,3,4,5,6]
# # 将列表反转(先后顺序颠倒),删除最后一个元素,打印此列表:
# # print(L)   # [6,5,4,3,2]
# # L=[3,5]
# # print(id(L))

# # L[:]=[1,2,3,4,5,6]
# # L[:]=L[::-1]
# # del L[5]
# # print(L)
# # print(id(L))

# # 1.输入三个数,存于列表中,打印这三个数的最大值,最小值和平均值
# # a=int(input(''))
# # b=int(input(''))
# # c=int(input(''))
# # l=[a,b,c]
# # print(max(l),min(l),sum(l)/3)



# # 2.写程序,让用户循环输入一些整数,当输入-1时结束输入,将这些整数存于列表L中
# # 1)打印您 共输入了几个有效数
# # 2)打印你输入的数的最大值
# # 3)打印你输入的数的平均值
# # l=0
# # L=[]
# # a=int(input(""))
# # while a!=-1:
# #     L+=[a]
# #     a=int(input(''))
# #     l+=1
# # print(L)
# # print(l)
# # print(max(L),sum(L)/l)
# # 或
# # L=[]  #先创建一个列表,然后用L绑定,装备存放数据
# # while True:
# #     a=int(input(""))
# #     if -1==a:
# #         break
# #     L+=[a]
# # print(L)
# # print("您共输入了%d个数" % len(L))


# # 有字符串s="hello",请生成如下字符串:'h e l l o'和'h-e-l-l-o'
# # s='hello'
# # print(' '.join(s))
# # print('-'.join(s))

# #一下生成一个数值为1-9的平方的列表
# # L=[]
# # for x in range(1,10):
# #     L.append(x**2)
# # print(L)

# # 用列表推导式生成1-100内所有奇数的平方的列表
# #   [1,9,25,.....]
# # L=[x**2 for x in range(1,100,2)]
# # print(L)


# # 写程序,输入一个开始的整数值用begin绑定,输入一个结束的整数用end绑定
# #   将从begin开始大end结束的所有偶数存与列表中,并打印
# # begin=int(input(''))
# # end=int(input(''))
# # L=[x**2 for x in range(begin,end) if x%2==0]
# # print(L)

# # 2.写程序,让用户输入很多整数(包含正整数和负整数)保存于列表L中,然后把列表
# # L中的所有正数存于列表L1中,把列表L中的所有负数存于列表L2中,打印原列表L和
# # 正数列表L1和负数列表L2
# # L=[]
# # while True:
# #     a=int(input('整数: '))
# #     if a==0:
# #         break
# #     L+=[a]
# # L1=[x for x in L if x>0]
# # L2=[x for x in L if x<0]
# # print(L,L1,L2)
# # 或
# # L=[]
# # i=0
# # while True:
# #     a=int(input('整数: '))
# #     if a==0:
# #         break
# #     L.append(a)
# # L1=[x for x in L if x>0]
# # L2=[x for x in L if x<0]
# # print("原列表是:",L,"正数的列表是:",L1,"负数的列表:",L2)


# # 用字符串'ABC'和'123'生成如下列表:
# # ['A1','A2','A3','B1','B2','B3','c1','C2','C3']
# # L=[x+y for x in 'ABC' for y in '123']
# # print(L)


# #   2.已知有一个字符串:s='100,200,300,500,800',将其转化为数字的列表,列表
# #   内部为整数:L=[100,200,300,500,800]
# # s='100,200,300,500,800'
# # L1=s.split(",")
# # L=[]
# # for x in L1:
# #     i=int(x)
# #     L.append(i)
# #     或
# # L=[int(x) for x in s.split(",")]
# # print(L)
# #   3.用列表推导式生成如下列表:L=[1,4,7,10,...100]
# # print([x for x in range(1,101,3)])
# #   4.用列表推导式生成如下列表(思考题)
# #   [[1,2,3],[4,5,6],[7,8,9]]

# # print([[x,x+1,x+2] for x in range(1,8,3)])
# # 或
# # print([[y for y in range(x,x+3)] for x in range(1,8,3)])
# # 或
# # 改为for语句
# # L=[]
# # for x in range(1,8,3):
# #     temp=[]
# #     for y in range(x,x+3):
# #         temp.append(y)
# #     L.append(temp)
# # print(L)


# 1.有一些数存于列表中.如L=[1,3,2,1,6,4,2,...98,82]
#   1)将列表L中出现的数字存如到另一个列表L2中
#      要求:
#      重复出现的数字只在L2中保留一份
# #   2)将列表中出现的数字存于列表L3中,重复出现的数字只在L3中只保留一份
# L1=[]
# L2=[]
# L3=[]
# n=input("数:")
# L1=[int(x) for x in n.split(",")]
# for x in L1:
#     if L1.count(x)==2:
#         if x not in L3:
#             L3.append(x)
#     if x not in L2:
#         L2.append(x)
# print(L2,L3)
# 或
# L=[1,3,2,1,6,4,2,98,82]
# L2=[]  
# L3=[]
# for x in L:  
#     if x not in L2:
#         L2.append(x)
#     if xnot in L3 and L.count(x)==2:
#         L3.append(x)
# print("L3=",L3)
# print("L2=",L2)
# # 2.计算出100以内的全部素数,将这些素数存于列表中,让后打印这些列表中的这些素数
# L=[]
# for x in range(1,101):
#     isprime=True
#     if x<2:
#         isprime=False
#     else:
#         for i in range(2,x):
#             if x%i==0:
#                 isprime=False
#                 break
#     if isprime:
#         L.append(x)
# print(L)
############## 或
L=[]
L1=[]     
for x in range(2,100):
    for i in range(2,x):
        if x%i==0:
            break
        else:
            L1=[x]
    else:
        L+=L1
print(L)
# # 3.生成前40个斐波那契(Fibonacci)数列的数
# # 1 1 2 3 5 8 13 21
# # 要求:将这些数保存于列表中,打印这些数
# l=1
# i=0
# L=[]
# while len(L)<41:
#     L.append(l)
#     i,l=l,i+l
# print(L)
# $############或
# L=[]
# a=0
# b=1
# while len(L)<40:
#     L.append(b)
#     c=a+b
#     a=b
#     b=c
# print(L)
# 或######
######
# L=[1,1]
# while len(L)<40:
#     L.append(L[-1]+L[-2])
# print(L)