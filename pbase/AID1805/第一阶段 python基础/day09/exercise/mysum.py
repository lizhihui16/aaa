# 练习:
#   写一个函数 mysum 可以传入任意个实参,返回所有实参的和
#     def mysum(*args):
#        ....

#     print(mysum(1, 2, 3, 4))  # 10
#     print(mysum(5, 6, 7, 8, 9, 10))  # 45

# 方法1
# def mysum(*tuple_numbers):
#     s = 0
#     for x in tuple_numbers:
#         s += x
#     return s

# 方法2
def mysum(*args):
    return sum(args)

print(mysum(1, 2, 3, 4))  # 10
print(mysum(5, 6, 7, 8, 9, 10))  # 45
