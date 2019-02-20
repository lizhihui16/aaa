# 1. 思考题:
#   查看:
#     >>> help(print)
#   猜想print函数的参数列表是如何定义的????



# def myprint(*args, sep=' ', end='\n'):
#     L = [str(x) for x in args]  # 把所有元组转为字符串列表
#     s = sep.join(L)
#     s += end
#     print(s, end='')

def myprint(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)


myprint(1, 2, 3, 4)
myprint('hello', 'world', sep="#")

myprint(1, 2, 3, 4, sep=':', end='我是结尾\n')
