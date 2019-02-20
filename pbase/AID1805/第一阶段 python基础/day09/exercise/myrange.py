# 2. 写一个 myrange函数,参数可以传1~3个,实际意义同range函数规则相同,此函数返回符合range(...) 函数规则的列表
#   如:
#     L = myrange(4)
#     print(L)  # [0, 1, 2, 3]
#     L = myrange(4, 6)
#     print(L)  # [4, 5]
#     L = myrange(1, 10, 3)
#     print(L)  # [1, 4, 7]

# 方法1
# def myrange(start, stop=None, step=1):
#     r_lst = []  # 即将返回的列表
#     # 调整三个形参的值
#     if stop is None:
#         stop = start
#         start = 0

#     if step > 0:
#         while start < stop:
#             r_lst.append(start)  # 把当前数加入到列表中
#             start += step  # 让start 向后移动,准备下次操作
#     else:  # 当步长小于0的情况
#         for x in range(start, stop, step):
#             r_lst.append(x)
#     # 此处把符合条件的数据加到列表r_lst中


#     return r_lst

# 方法2
def myrange(start, stop=None, step=1):
    # 调整三个形参的值
    if stop is None:
        stop = start
        start = 0

    return list(range(start, stop, step))

L = myrange(4)
print(L)  # [0, 1, 2, 3]
L = myrange(4, 6)
print(L)  # [4, 5]
L = myrange(1, 10, 3)
print(L)  # [1, 4, 7]
L = myrange(10, 1, -3)
print(L)

