

#此示例示意assert语句的语法
# def get_score():
#     s=int(input("请输入学生成绩：（０－１００）"))


#     assert 0<=s<=100,"超出范围"
#     # 或
#     # if bool(0<=s<=100)==False:
#     #     raise AssertionError("超出范围")

#     return s
# try:
#     score=get_score()
#     print("学生的成绩为:",score)
# except AssertionError as err:
#     print("AssertionErro类型的错误被触发，且已捕获")
#     print("err=",err)



# L=[2,3,5,7]
# it=iter(L)
# while True:
#     try:
#         x=next(it)
#         print(x)
#     except StopIteration:
#         break




# 有一个集合：s={'唐僧','悟空','八戒','沙僧'}
# 用for语句遍历所有元素如下：
# for x in s:
#     print(x)
# else:
#     print('遍历结束')
# 请将上面的for语句改写为while语句和迭代器实现
s={'唐僧','悟空','八戒','沙僧'}
it=iter(s)
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        print('遍历结束')
        break