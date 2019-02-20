# 已知有列表：Ｌ＝[2,3,5,7,10,15]
# 1)写一个生成器函数，让此函数能动态提供数据，数据为原列表的数字的平方加１
# 2)写一个生成器表达式，让此函数能动态提供数据，数据依旧为原列表的数字的平方加１
# 3)写一个列表，此列表内的数据为原列表的数字的平方加１
# L=[2,3,5,7,10,15]
# def f(n):
#     for x in L:
#         yield x**2+1
# L1=list(f(L))
# print(L1)
# 或
# L=[2,3,5,7,10,15]
# def f():
#     for x in L:
#         yield x**2+1
# L1=list(f())
# print(L1)


# ###for y in f(L):
#    #### print(y)


# 2)写一个生成器表达式，让此函数能动态提供数据，数据依旧为原列表的数字的平方加１

# L=[2,3,5,7,10,15]
# gen=list((x**2+1 for x in L))

# print('gen=',gen) 

# 3)写一个列表，此列表内的数据为原列表的数字的平方加１
# L=[2,3,5,7,10,15]
# L=[x**2+1 for x in L]
# print(L)







# 练习：
#     １.写一个生成器函数，给出开始值begin和终止值ｅｎｄ,此生成器函数生成begin~end氛围
#     内的全部素数（不包含end)
#     如：
#     def prime(begin,end):
#         ...
#     L=list(prime(10,20))
#     print(L)
# def is_prime(x):
#     if x<2:
#         return False
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return True
# def prime(begin,end):
#     for x in range(begin,end):
#         if is_prime(x):
#             yield x
# L=list(prime(0,20))
# print(L)
# print(sum(prime(0,200)))


# def prime(begin,end):
#     l1=[]
#     for x in range(begin,end):
#         for y in range(2,x+1):
#             if x%y==0 and x!=y :
#                 break
#             else:
#                 l=[x]
#         else:        
#             l1+=l
#     return l1

# L=list(prime(2,20))
# print(L)



# 练习：
# 　　有一个bytearray 字节数组　ba=bytearray(b'a1b2c3d4')
#     如何得到字节串'1234'和'abcd',将上述字节数组改为：
#     ba=bytearray(b'A1B2C3D4')

# ba=bytearray(b'a1b2c3d4')
# b1=ba[1::2]
# s1=b1.decode('utf-8')
# b2=ba[::2]
# s2=b2.decode()
# ba[::2]=ord('A'),ord('B'),ord('C'),ord('D')
# print(s1,s2,ba)

# ba=bytearray(b'a1b2c3d4')
# b1=ba[1::2]
# b1=bytes(b1)
# b2=ba[::2]
# b2=bytes(b2)

# ba[::2]=range(ord('A'),ord('E'))
# print(b1,b2,ba)
