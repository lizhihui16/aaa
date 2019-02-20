# keywords_args.py


# 此示例示意函数的命名关键字形参

def fa(a, b, *, c, d):
    '''强制c,d必须用关键字传参 '''
    print(a, b, c, d)

fa(1, 2, d=400, c=300)  # 对的


def fb(a, b, *args, c, d):
    print(a, b, args, c, d)

fb(1, 2, 3, 4, d=400, c=200)
fb(1,2,3,4,5, **{'d':400, 'c':300})

# 问题:
# fb(1,2,3,4, c=400, d=300, e=500)  # 出错,e是多余的

# fa(1, 2, 3, 4)  # 错的
