

# numbers=[10086, 10000, 10010, 95588]
# names = ['中国移动', '中国电信', '中国联通']
# # def myzip(*args)
# def myzip(iter1,iter2):
#     #先拿到两个对象的迭代器
#     it1=iter(iter1)
#     it2=iter(iter2)
#     while True:
#         try:
#             a=next(it1)
#             b=next(it2)
#             yield(a,b)
#         except StopIteration:
#             return   #此生成器函数结束
#     # yield(next(it1),next(it2))
# for t in myzip(numbers, names):
#     print(t)
# d = dict(myzip(numbers, names))  # ???
# print(d)


# 练习:
#   写一个程序，读入任意行文字，当输入空行时结束输入
#     打印带有行号的输入结果
#       如:
#         请输入:hello
#         请输入:world
#         请输入:python
#         请输入:<回车>
#       输入如下:
#         第1行: hello
#         第2行: world
#         第3行: python

def get_input_text():
    L=[]
    while True:
        s=input("请输入：")
        if not s:
            return L
        L.append(s)

def print_text_with_number(L):
    for t in enumerate(L,1):
        print("第%d行： %s" % t)
L=get_input_text()
print_text_with_number(L)