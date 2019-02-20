# double_star_keyword_args.py


# 此示例示意双星号字典形参的用法
def fa(**kwargs):
    '''kwargs绑定字典'''
    print("多余的关键字传参的个数是:", len(kwargs))
    print("kwargs =", kwargs)

fa(a=10, b=20, c=30)

def fb(*args, a, **kwargs):
    print(args, a, kwargs)

fb(1,2,3, b=20, c=30, a=10)


