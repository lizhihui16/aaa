def myyield():
    '''这是一个生成器函数，此函数用来动态生成２，３，５，７'''
    yield 2
    yield 3
    yield 5
    yield 7
    #用迭代器访问这个生成器
# gen=myyield()
# print(gen)#gen是一个生成器对象
# it=iter(gen)
# print(next(it)) #2
# print(next(it)) #3
# print(next(it)) #5
# print(next(it)) #7
# print(next(it))  #StopIteration



for x in myyield():
    print(x)

