# 2. 写一个函数 input_number
#     def input_number():
#         此处自己实现
#     此函数用来获取用户循环输入的整数,当输入负数时结束输入.
#     将用户输入的数字以"列表"的形式返回,再用内建函数max, min, sum求出用户输入的最大值,最小值和平均值

#     L = input_number()
#     print(L)  # 打印用户输入的列表
#     print("用户输入的最大值是:", max(L))
#     print("用户输入的最小值是:", min(L))
#     print("用户输入的平均是:", sum(L)/len(L))



def input_number():
    L = []  # 创建一个列表,准备存储数字
    # 此处自己实现
    while True:
        n = int(input("请输入一个正整数"))
        if n < 0:
            break
        L.append(n)
    return L

L = input_number()
print(L)  # 打印用户输入的列表
print("用户输入的最大值是:", max(L))
print("用户输入的最小值是:", min(L))
print("用户输入的平均是:", sum(L)/len(L))

