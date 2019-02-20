# keyword_give_args.py


# 此示例示意关键字传参

def myfun(a, b, c):
    """注意此函数不会变化"""
    print('a =', a)
    print('b =', b)
    print('c =', c)


myfun(b=2, c=3, a=1)
myfun(c=333, b=222, a=111)

# 以下是错误的
# myfun(a=2, c=3, a=1)
# myfun(d=2, c=3, a=1)

