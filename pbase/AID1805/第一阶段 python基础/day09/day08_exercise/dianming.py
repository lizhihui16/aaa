# 1. 已知全班学生的名单，存于集合中names
#   写一个点名签到的程序。
#      随机输出学生的姓名，让用户输入:"y"代表已到,输入"n"或其它代表未到。
#      当点名结束后，打印未到者名单

names = {'小张', '小李', '小赵', '老冯'}

S = set() # 此集合用来保存未到者的名单
for n in names:
    result = input(n + "来了没有: ")
    if result == 'y':
        pass
    else:
        S.add(n)

print('未到者名单:', S)


