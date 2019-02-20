# com_give_args.py


# 此示例示意 函数的组合 传参

def myfun(a, b, c):
    """注意此函数不会变化"""
    print('a =', a)
    print('b =', b)
    print('c =', c)

# myfun(1, c=3, b=2)  # 正确
# myfun(b=2, a=1, 3)  # 错的
myfun(100, *[200, 300])  # 正确 
myfun(*"AB", 300)  # 正确
myfun(*[100], c=300, b=200)  # 正确
myfun(*"AB", **{"c":300})  # 正确