# 2. 写一个函数print_even,传入一个参数n代表终止数.
#   此函数调用将打印 2 4 6 8 ..... n 之间所有的偶数
#   函数定义如下:
#     def print_even(n):
#          .... 此处自己完成
#     # 测试调用:
#     print(8)
#     # 2 4 6 8
#     print(15)
#     # 2 4 6 8 10 12 14

def print_even(n):
    for i in range(2, n + 1):
        if i % 2 == 0:
            print(i, end=' ')
    print()


# 测试调用:

print_even(8)
# 2 4 6 8

print_even(15)
# 2 4 6 8 10 12 14