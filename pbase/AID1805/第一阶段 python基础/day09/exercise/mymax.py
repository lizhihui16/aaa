# 1. 写一个函数mymax,实现返回两个数的最大值:
#   如:
#     def mymax(a, b):
#        ... <<-- 此处自己实现

#     print(mymax(100, 200))  # 200
#     print(mymax("ACB", "ABC"))  # ACB


# 方法1 经典算法
# def mymax(a, b):
#     # 求最大值用变量zuida绑定
#     zuida = a
#     if b > zuida:
#         zuida = b
#     # 把zuida绑定的数据送回给调用
#     return zuida

# 方法2
# def mymax(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# 方法3
# def mymax(a, b):
#     if a > b:
#         return a
#     return b

# 方法4
# def mymax(a, b):
#     return a if a > b else b

# 方法5
def mymax(a, b):
    return max(a, b)



print(mymax(100, 200))  # 200
print(mymax("ACB", "ABC"))  # ACB
