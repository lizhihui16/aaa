# 练习:
#   1. 利用上题input_number获取用户输入的数字列表
#   写一个函数split_number(L) 传入得到的列表
#     将所有的数字分为奇数和偶数,分别放在两个列表odds 和 evens 中
#   同时返回这两个列表打印其中的数据
#   def split_number(L):
#      此处自己实现
#   L = input_number()  # 1, 2, 3, 4, 5, 6
#   t = split_number(L)  # 返回一个元组,元组里放两个列表
#   odds, evens = t
#   print("所有的奇数是:", odds)  # [1, 3, 5]
#   print("所有的偶数是:", evens)  # [2, 4, 6]


def input_number():
    L = []  # 创建一个列表,准备存储数字
    # 此处自己实现
    while True:
        n = int(input("请输入一个正整数"))
        if n < 0:
            break
        L.append(n)
    return L


def split_number(L):
    L1 = []  # 用来存放奇数
    L2 = []  # 创建一个列表,用来存放偶数
    for x in L:
        if x % 2 == 1:
            L1.append(x)
        else:
            L2.append(x)
    return (L1, L2)  # 打包成为元组后返回


lst = input_number()  # 1, 2, 3, 4, 5, 6
t = split_number(lst)  # 返回一个元组,元组里放两个列表

odds, evens = t
print("所有的奇数是:", odds)  # [1, 3, 5]
print("所有的偶数是:", evens)  # [2, 4, 6]



