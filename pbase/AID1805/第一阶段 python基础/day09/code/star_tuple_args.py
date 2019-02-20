

# 此示例示意星号元组形参的用法

# 以下为位置形参, 调用者最多只能传递三个实参
# def fa(a, b, c):
#     pass

def fb(*args):
    '''args绑定一个元组'''
    print("实参的个数是:", len(args))
    print("args=", args)


fb()
fb(1, 2, 3, 4)
