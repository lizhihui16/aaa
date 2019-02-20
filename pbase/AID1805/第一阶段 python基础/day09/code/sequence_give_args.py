# sequence_give_args.py


# 此示例示意序列传参

def myfun(a, b, c):
    """注意此函数不会变化"""
    print('a =', a)
    print('b =', b)
    print('c =', c)

s = "ABC"
L = [4,5,6]
t = (1.1, 2.2, 3.3)

# myfun(s[0], s[1], s[2])  # 按位置传
myfun(*s)
myfun(*L)
myfun(*t)

