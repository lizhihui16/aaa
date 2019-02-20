# def power2(x):
#     return x**2
# #生成一个可迭代对象，此可迭代对象可以生成１－９的自然数的平方
# for x in map(power2,range(1,10)):
#     print(x)

#生成一个可迭代对象，此可迭代对象可以生成
# １**4,2**3,3**2,4**1
#pow(x,y,z=None)
# for x in map(pow,range(1,5),range(4,0,-1)):
#     print(x)

# for x in map(pow,range(1,5),range(4,0,-1),range(5,100)):
#     print(x)


# 求：1**2+2**2+3**2+...+9**2的和

# 方法１
# def mx(x):
#     return x**2
# # a=0
# # for x in map(mx,range(1,10)):
# #     a+=x
# # print(a)
# # 方法２
# m=map(mx,range(1,10))
# print(sum(m))
# # 方法３
# print(sum(map(mx,range(1,10))))

# 求：１**3＋２**3+3**3+...+9**3的和
# 方法１
# print(sum(map(lambda x:x**3,range(1,10))))
# 方法２
# def mx(x,y=3):
#     return x**y
# a=0
# for x in map(mx,range(1,10)):
#     a+=x
# print(a)

# 求：１**9+2**8+3**7+...+9**1的和

# def mx(x,y):
#     return  x**y
# s=0
# for a in map(mx,range(1,10),range(9,0,-1)):
#     s+=a
# print(s)

# print(sum(map(pow,range(1,10),range(9,0,-1))))