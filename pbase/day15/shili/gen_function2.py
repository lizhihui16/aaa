def myyield():
    '''这是一个生成器函数，此函数用来动态生成２，３，５，７'''
    print("即将生成２")
    yield 2
    yield 3
    yield 5
    yield 7
    print("生成器函数调用结束")
    #用迭代器访问这个生成器
gen=myyield()
it=iter(gen)#拿到迭代器时，生成函数不执行
print(next(it))   #即将生成２
print(next(it))   #3
print(next(it))   #5
print(next(it))   #7
