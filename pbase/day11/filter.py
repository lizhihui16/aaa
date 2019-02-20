# 生成１－１００的奇数

# def isodd(x):
#     return x%2==1
# for x in filter(isodd,range(100)):
#     print(x)
# 生成１－１００的偶数
even=[x for x in filter(lambda x:x%2==0,range(1,100))]
print(even)

# def isprime(x):
#     if x<2:
#         return False
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return True
# primes=[x for x in filter(isprime,range(1,100))]
# print(primes)



# sorted 函数
# L=[5,-2,-4,0,3,1]
# L2=sorted(L)
# print('L2=',L2)     #[-4,-2,0,1,3,5]
# l3=sorted(L,reverse=True)
# print("l3=",l3)    #[5,3,1,0,-2,-4]

# l4=sorted(L,key=abs)
# print(l4)      #[0,1,-2,3,-4,5]
# names=['Tom','Jerry','Spike','Tyke']
# l5=sorted(names,key=len)
# print(l5)
# l6=sorted(names)
# print('l6=',l6)

# names=['Tom','Jerry','Spike','Tyke']
# 排序的依据是'moT','yrreJ','ekipS','ekyT'
# 结果是：
#     ['Spike','Tyke','Tom','Jerry']
#     (注：如果没有现成的函数可用，需要之间写函数)
# l=['Tom','Jerry','Spike','Tyke']
# def mm(s):
#     return s[::-1]
# l1=sorted(l,key=mm)
# print(l1)

