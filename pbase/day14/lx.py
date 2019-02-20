# 练习：
# 　１．写一个函数get_score()来获取学生输入的成绩（０－１００）的数，如果用户
# 　输入的不是０－１００的整数则返回０，否则返回输入的整数
# 如：
#     def get_score():
#         ...
#     score=get_score()
#     print("你输入的成绩是：",score)
# 方法１　　在调用get_score时加入try语句
# def get_score():
#     score=int(input('请输入整数：'))
#     if not (0<=score<=100):
#         return 0    
#     return score
# try:
#     score=get_score()
# except ValueError:
#     score=0
# print("你输入的成绩是：",score)



# 方法２　　在get_score函数内部加入try语句来进行错误处理
def get_score():
    try:
        s=int(input('请输入整数：'))
    except ValueError:    
        return 0

    if not (0<=s<=100):
        return 0    
    return s

score=get_score()
print("你输入的成绩是：",score)







# 　示例：　
#     写一个函数get_age()用来获取一个人的年龄信息，此函数规定用户只能
#     输入１－１４０之间的整数，如果用户输入的数是其他的数值，则直接触发
#     ValueError类型的错误！
#     如：
#     def get_age():
#         ...
#     try:
#         age=get_age()
#         print("用户输入的年龄是",age)
#     except ValueError as err:
#         print("用户输入的不是１－１４０的数字，获取年龄失败")
# def get_age():
#     a=int(input("年龄:"))
#     if a<1 or a>140:

#         raise ValueError('用户输入年龄不合适')

#     return a
# try:
#     age=get_age()
#     print("用户输入的年龄是",age)
# except ValueError as err:
#     print("用户输入的不是１－１４０的数字，获取年龄失败")


# def get_age():
#     try:
#         a=int(input("年龄:"))
#     except ValueError:
#         raise ValueError("用户输入的不是数字")
#     if a<1 or a>140:

#         raise ValueError('用户输入年龄不合适')

#     return a
# try:
#     age=get_age()
#     print("用户输入的年龄是",age)
# except ValueError as err:
#     print("用户输入的不是１－１４０的数字，获取年龄失败")
#     print(err)


