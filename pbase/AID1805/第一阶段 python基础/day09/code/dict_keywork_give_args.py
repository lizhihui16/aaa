# dict_keywork_give_args.py


# 此示例示意字典关键字传参

def myfun(a, b, c):
    """注意此函数不会变化"""
    print('a =', a)
    print('b =', b)
    print('c =', c)


d = {'a':111, 'c':333, 'b': 222}
myfun(**d)  # 等同于 myfun(a=111,c=333,b=222)

# 以下是错误传法
# d2 = {1: '一', 'c':333, 'b': 222}
# myfun(**d2)
