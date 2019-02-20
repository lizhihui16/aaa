# def say_hello():
#     print("hello world")
#     print("hello Tarena")
#     print("hello everyone")
# say_hello()
# say_hello()
# say_hello()
# say_hello()
###############################

# 写一个函数,给两个数,打印最大值
# def mymax(a,b):
#     m=a
#     if b>m:
#         m=b
#     print("最大值的数据是:",m)
# mymax(100,200)
# mymax('abc','123')

# 写一个函数myadd,此函数中的参数列表里有两个参数x,y,此函数的功能是打印x+y的和:
# 如:
# def myadd(x,y):
#     z=x+y        #局部变量
#     print(z)  #...是需要填充的部分
# myadd(100,200)
# myadd("ABC","123")

# def myadd():
#     z=x+y        
#     print(z)
# x=10000
# y=20000
# myadd()


# def say_hello2():
#     print("hello world")
#     print("hello Tarena")
#     # return
#     # return 1+2
#     return[1,2,3,1+3]
#     print("hello everyone")
# r=say_hello2()
# print("r=",r)
# print('程序结束')

# 1.写一个函数myadd2,实现给出两个数,返回这两个数的和
# def myadd2(x,y):
#     z=x+y
#     # return z
# a=int(input("请输入第一数: "))
# b=int(input("请输入第一数: "))
# print("您输入的这两个数的和是",myadd2(a,b))

# 2.写一个函数mymax3,返回三个数中最大的一个值
# 方法1
# def mymax3(a,b,c):
#     z=max(a,b,c)
#     # z=a
#     # if z<b:
#     #     z=b
#     # if z<c:
#     #     z=c
#     return z
# print(mymax3(100,300,200))
# print(mymax3('ABC','123','abc'))
# 方法2
# def mymax3(a,b,c):
#     z=a if a>b else b
#     z=z if z>c else c
#     return z
# print(mymax3(100,300,200))
# print(mymax3('ABC','123','abc'))

# 3.写一个函数 input_numbers,如下:
# def input_numbers():
#     .....#此处自己写
# 此函数用来获取用户循环输入的整数,当用户输入负数时结束输入
# 将用户输入的数字以列表的形式返回,再用内建函数max,min,sum求出输入数的最大值,最小值及和
# L=input_numbers()
# print(L)  #打印列表
# print("用户输入的最大值:",max(L))
# print("用户输入的最小值:",min(L))
# print("用户输入的和:",sum(L))
# 方法1:
# L=[]
# def input_numbers():
#     a=int(input(""))
#     while a>0:
#         L.append(a)
#         a=int(input(""))
# print(input_numbers())
# print("用户输入的最大值:",max(L))
# print("用户输入的最小值:",min(L))
# print("用户输入的和:",sum(L))
# # 方法2:
# def input_numbers():
#     L=[]
#     a=int(input(""))
#     while a>0:
#         L.append(a)
#         a=int(input(""))
#     return L
# L=input_numbers()
# print(L)
# print("用户输入的最大值:",max(L))
# print("用户输入的最小值:",min(L))
# print("用户输入的和:",sum(L))

# def input_numbers():
#     lst=[]
#     while True:
#         a=int(input(""))
#         if a<0:
#             break
#         lst.append(a)

#     return lst
# L=input_numbers()
# print(L)
# print("用户输入的最大值:",max(L))
# print("用户输入的最小值:",min(L))
# print("用户输入的和:",sum(L))

# def input_numbers():
#     lst=[]
#     while True:
#         a=int(input(""))
#         if a<0:
#             return lst
#         lst.append(a)
# L=input_numbers()
# print(L)
# print("用户输入的最大值:",max(L))
# print("用户输入的最小值:",min(L))
# print("用户输入的和:",sum(L))

# 练习:
# 1.写一个函数get_chinese_char_count(s)函数,此函数实现的功能是给定一个字符串,
# 返回这个字符串中中文字符的个数
# def get_chinese_char_count(s):
#     ...
# S=INPUT("请输入中英文混合的字符串: ")
# print("您输入的中文字符的个数是:",get_chinese_char_count(s))
# 方法1
# def get_chinese_char_count(s):
#     l=[]
#     for x in s:
#         if ord(x)>127:
#             l+=x
#     return len(l)
# s=input("请输入中英文混合的字符串:")
# print("您输入的中文字符的个数是:",get_chinese_char_count(s))
# 或
# def get_chinese_char_count(s):
#     l=0
#     for x in s:
#         if ord(x)>127:
#             l+=1
#     return l
# s=input("请输入中英文混合的字符串:")
# print("您输入的中文字符的个数是:",get_chinese_char_count(s))

# 2.定义两个函数:
# sum3(a,b,c) 用于返回三个数的和
# pow3(x) 用于返回x的三次方
# 用以上函数计算:
# 1)计算1的立方+2的立方+3的立方
# 2)计算1+2+3的和的立方
# 即:1**3+2**3+3**3和(1+2+3)**3
# def sum3(a,b,c):
#     z=a+b+c
#     return z
# def pow3(x):
#     l=x**3
#     return l
# print("计算1的立方+2的立方+3的立方:",sum3(pow3(1),pow3(2),pow3(3)))
# print("1+2+3的和的立方:",pow3(sum3(1,2,3)))