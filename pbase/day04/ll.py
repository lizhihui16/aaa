# 输入三行文字，让这三行文字依次以20个字符的宽度右对齐输出
# 如：
#     请输入第1行: hello world
#     请输入第2行: abcd
#     请输入第3行:  a
# 输出结果为:
#         hello world
#             abcd
#                 a
# 做完上面的题后再思考:
# 能否以最长字符串的长度进行右对齐显示(左侧填充空格)

# # print('%20s' % "hello world")
# print('%20s' % 'abcd')
# print('%20s' % 'a')

# a=input('')
# b=input()
# c=input()
# d=len(a)
# if len(b)>d:
#     d=len(b)
# if len(c)>d:
#     d=len(c)
# print(" "*(d-len(a))+a)
# print(" "*(d-len(b))+b)
# print(" "*(d-len(c))+c)





# i = input('')
# s = int(i[0])
# n = int(i[2])
# a = i[1]
# if a == '+':
#     print(s+n)
# if a == '-':
#     print(s-n)
# if a == '*':
#     print(s*n)
# if a == '%':
#     print(s%n)
# if a == '/':
#     print(s/n)


#打印20行hello!

# i=1   #初始化循环变量
# while i<=20:   #判断是否要执行其中的语句
#     print('hello')
#     i+=1   #改变循环变量i的值来控制循环次数
# else:
#     print('1314')
# print('结束')
# 打印1-20 的整数
# i=1
# while i<=20:
#     print(i)
#     i+=1 
#输入一个整数n，写出打印这是第n行
# n=int(input("输入整数："))
# i=1
# while i<=n:
#     print("这是第",i,"行")
#     i+=1

# 1.写程序，打印1-20的整数，打印在一行显示，每个数字之间用空格分隔
# 1 2 3 4 5...19 20
# n=int(input("输入整数："))
# i=1
# while i<=n:
#     print(i,end=" ")
#     i+=1
# print()
# # 2.打印1-20的整数，每行打印5个，打印4行
# 如：
# 1 2 3 4 5
# 6 7 8 9 10
# .....
# .....
# n=int(input("输入整数："))
# i=1
# while i<=n:
#     print(i,end=" ")
#     if i%5==0:
#         print()
#     i+=1
        
# 3.输入一个整数，打印一个宽度和高度都是n个字符的张方形如：
# 4 ####
#     #  #
#     #  #
#     ####    
# n=int(input("输入整数："))

# print("#"*n)
# i=1
# while i<=n-2:
#     print("#"+" "*(n-2)+"#")
#     i+=1
# if n>1:
#     print("#"*n)

# 4.写程序，计算1+2+3+4+....+100的和，打印结果。
# i=0
# s=0
# while i<=100:
#     s+=i
#     i+=1
# print(s)


# 5.写程序，输入一个开始值用begin绑定，输入一个结束值用end绑定
#     计算：出begin开始，到end结束的所有整数的和
#     如： 开始值：1
#         结束值：10
#     打印：
#         和是：55
# begin=int(input(''))
# end=int(input(""))
# s=0
# while end>=begin:
#     s+=begin
#     begin+=1
# print(s)

# 6.写一个程序：
#   输入一个开始整数值用变量begin绑定，输入一个结束整数值用变量end绑定
#   打印从begin到end的每个整数，打印在一行内。如：
#   开始：8    结束:30
#   打印： 8 9 10 11.......30
#   完成后思考：如何实现每5个整数打印在一行内，打印多行
#   提示：可以多加一个变量来记录打印个数
# begin=int(input(''))
# end=int(input(""))
# while begin<=end:
#     print(begin,end=" ")
#     begin+=1
# print()

# begin=int(input('请输入开始值： '))
# end=int(input("请输入结束值： "))
# s=0
# while begin<=end:
#     print(begin,end=" ")
#     s+=1
#     begin+=1
#     if s%5==0:
#         print()
# print()


# 打印1-20整数，打印在一行内
#     1 2 3 4....20
# j=0
# while j<10:
#     i=1
#     while i<=20:
#         print(i,end=" ")
#         i+=1
#     print()
#     j+=1

# 输入一个数，打印指定宽度的正方形如：
# 输入5：
# 打印： 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# n=int(input("输入一个数"))
# j=0
# while j<n:
#     i=1
#     while i<=n:
#         print(i,end=" ")
#         i+=1
#     print()
#     j+=1




#  写一个程序，任意输入一些整数，当输入小于零的数时结
#     束输入，当输入完成后，打印您输入的这些正整数的和
#     如：
#     请输入：1
#     请输入：2
#     请输入：3
#     请输入：4
#     请输入：-1
#     打印： 您刚才输入的这些正整数的和是：10
# s=0
# while True:
#     n=int(input(""))
#     if n<0:
#         break
#     s+=n
# print(s) 

# 1.打印从零开始的浮点数，每个数增加0.5，打印出10以内这样的数
#     0.0 0.5 1.0 1.5 .... 9.0 9.5
# i=0.0
# while i<10:
#     print(i,end=' ')
#     i+=0.5
# print()

# 2.写程序求：
#     1/1+1/3+1/5+...+1/99的和
# i=1
# s=0
# while i<100:
#     s=1/i+s
#     i+=2
# print(s)

# 3.输入一个整数表示求三角行的宽度和高度，打印出如下的三角形。如：请输入三角形的宽度 4
# *
# **
# ***
# ****
# n=int(input('请输入三角形的宽度： '))
# i=1
# while i<=n:
#     print("*"*i)
#     i+=1

# 4.写程序，输入一个整数代表正方形的宽和高，打印如下的正方形。如：请输入宽度：5
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8
# 5 6 7 8 9 
# 如：
#     请输入宽度：4  
#     1 2 3 4 
#     2 3 4 5 
#     3 4 5 6 
#     4 5 6 7 
# n=int(input('请输入宽度： '))
# i=1

# while i<=n:
#     j=i
#     while j<=n+i-1:
#         print(j,end=" ")
#         j+=1
#     print()
#     i+=1
