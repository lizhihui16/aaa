#此示例示意生成器函数创建生成从０开始到n结束的一系列整数（不包含n)
# def myinteger(n):
#     i=0
#     while i<n:
#         yield i
#         i+=1
# for x in myinteger(5):
#     print(x)

# 写一个生成器函数myeven(start, stop)，用来生成从start开始，到stop结束区间内的一系列偶数

# def myeven(start, stop):  # 不包含stop
#     .... 此处自己实现

# it = iter(myeven(5, 10))
# print(next(it))  # 6
# print(next(it))  # 8

# evens = list(myeven(10, 20))
# print(evens)  # [10, 12, 14, 16, 18]
# for x in myeven(21, 30):
#     print(x)  # 22 24 26 28
start=int(input(''))
stop=int(input(''))
def myeven(start, stop):
    for i in range(start, stop):
        if i%2==0:   
            yield i
for x in myeven(start, stop):
    print(x)

