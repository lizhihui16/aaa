# # 1. 任意输入一个字符串:
# #     1) 计算您输入的空格的个数，并打印出来
# #     2) 计算您输入的'a' 字符的个数，并打印出来
# #       (要求用for语句实现)
# #     思考:
# #       用while语句能否实现上述功能
# # n=input('')
# # m=0
# # for x in n:
# #     if x==' ':
# #         m+=1
# # print(m)

# # range(1,10)


# # s='abcde'
# # for ch in s:
# #     print("ch----->",ch)
# # else:
# #     print('遍历字符串',s,'结束')

# #   任意输入一段字符串
# # 1)计算这个字符串的'a'这个字符的个数,并打印
# # 2)计算出空格的个数,并打印出来
# # (要求用for语句,不允许使用S.count方法)
# # 思考:用while语句能否实现上述功能?
# # s=input('')
# # i=0
# # j=0

# # for d in s:
# #     if 'a'==d:
# #         i+=1
# #     elif ' '==d:
# #         j+=1
# # 或
# # m=0
# # while m<len(s):
# #     if 'a'==d:
# #         i+=1
# #     elif ' '==d:
# #         j+=1
#     # m+=1
# # print(i)
# # print(j)
# # 或
# # print(s.count('a'))


# # 用for语句打印1~20的整数,打印在一行内
# # for x in range(1,21):
# #     print(x,end=' ')
# # print()

# # 用for语句打印1~20的整数,每行打印5个,打印4行
# # for y in range(1,21):
# #     print(y,end=' ')
# #     if y%5==0:
# #         print()
# # print()

# # 3.求100以内有哪些数与自身+1的乘积再对11求余,结果等于8?
# # 提示:x*(X+1)%11==8
# # for x in range(100):
# #     if x*(x+1)%11==8:
# #         print(x)

# # 4.输入一段字符串,判断您输入的字符串中有几个文字符:
# # 注:中文字符的编码值一定大于127.
# # n=input("字符串")
# # i=0
# # for x in n:
# #     if ord(x)>127:
# #         i+=1
# # print(i)

# # 写一个程序,打印26个大写英文字母和26个小写英文字母
# # A B C D...X Y Z a b c ...x y z
# # for x in range(65,91):
# #     print(chr(x),end=" ")
# # for y in range(97,123):
# #     print(chr(y),end=" ")
# # for x in range(ord('A'),ord('Z')+1):
# #     print(chr(x),end=" ")       
# # for y in range(ord('a'),ord('z')+1):
# #     print(chr(y),end=" ")
# # print()

# #   1.输入一个整数代表开始用begin绑定,输入一个整数用end绑定
# #     打印begin-end(不包含end)之间的全部奇数
# # begin=int(input("输入一个整数: "))
# # end=int(input("输入一个整数: "))
# # # for x in range(begin,end):
# # #     if x%2==1:
# # #         print(x,end=' ')
# # # print()
# # # 或
# # for x in range(begin,end):
# #     if x%2==0:
# #         continue
# #     print(x,end=' ')
# # print()


# #   2.求1-100 之间所有不能被2,3,5,7 整除的数
# #     1)打印这些数
# #     2)打印这些数的和
# # s=0
# # for x in range(1,101):
# #     if x%2!=0:
# #         if x%3!=0:
# #             if x%5!=0:
# #                 if x%7!=0:
# #                     print(x,end=' ')
# #                     s+=x
# # print(s)
# # 或
# # s=0
# # for x in range(1,101):
# #     if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
# #         print(x,end=' ')
# #         s+=x
# # print(s)



# # 1.写一个程序,让用户输入很多正整数,当输入负数时结束输入
# # 将用户输入的数存在于列表L中,打印这个列表如:
# # 请输入:1
# # 请输入:2
# # 请输入:3
# # 请输入:4
# # 打印:
# # [1,2,3,4]
# # L=[]
# # while True:
# #     x=int(input("正整数:"))
# #     if x<0:
# #         break
# #     L+=[x]
# # print(L)




# # 1.写程序输入一个三角形的宽和高,打印相应的三角形.如
# #   输入:3
# #   1)*
# #     **
# #     ***
# #   2)  *
# #      **
# #     ***
# #   3)***
# #     **
# #     *
# #   4)***
# #      **
# #       *
# n=int(input('三角形的高: '))
# i=1
# # 1)
# # while i<=n:
# #     print(i*"*")
# #     i+=1
# 或
# for stars in range(1,n+1):
#     print("*"*stars)


# 3)
# while i<=n:
#     print((n-i+1)*"*")
#     i+=1
# 或
# for stars in range(n,0,-1):
#     print("*"*stars)

#     print("*"*stars)
# 2)
# # while i<=n:
# #     print((n-i+1)*" "+ i*"*")
# #     i+=1
# 4)
# # while i<=n:
# #     print(i*" "+(n-i+1)*"*")
# #     i+=1


# # 2.写一个程序,任意输入一个整数,判断这个数是否为素数(prime)
# #   素数(也叫质数),只能被1和自身整除的正整数
# #   如:2 3 5 7 11 13 17....
# #   提示:
# #   用排除法:当判断x是否为素数是,只要让x分别除以2,3,4,5....x-1,只要
# #   有任何一个数能被整除,则说明x不是素数,否则为素数
# n=int(input('整数: '))
# i=2
# while i<n:
#     if n%i==0:
#         print("否")     
#         break
#     i+=1
# else:
#     print("是")
# 或
# for m in range(2,n):
#     if n%m==0 and n!=2:
#         print("否")
#         break
# else:
#     print("是")
# 或
# x=int(input(''))
# if x<2:
#     print(x,"不是素数")
# else:
#     for i in range(2,x):
#         if x%i==0:
#             print("不是")
#             break
#         else:
#             print('是')

# for x in range(2,n):
#     for y in range(2,n):
#         if x*y==n:
#             print("否")
#             break
# else:
    # print("是")


# # 3.编写程序求下列多项式的值:
# # Sn=1/1-1/3+1/5-1/7+.....
# # 1)求1000000个这样的分数相加的和是多少?
# # 2)将上一步的和乘以4打印出来,是多少?
# # s=(-1)**(n-1)/(n*2-1)
# # n=int(input('整数: '))
# i=1
# m=0
# while i<=1000000:
#     s=(-1)**(i-1)/(i*2-1)
#     m+=s
#     i+=1
# print(m*4)
# 或
# Sn=0.0
# fenmu=1
# i=0
# sign=1  #
# while i<1000000:
#     r=sign*1/fenmu
#     Sn+=r
#     sign*=-1
#     fenmu+=2
#     i+=1
# print(Sn)
# print(Sn*4)



# 4.算出100~999之间的水仙花数(Narcissistic Number)
#     水仙花数是指百位的3次方+十位的3次方+个 位的3次方等于原整数
#     如:153=1**3+5**3+3**
# for x in range(100,1000):
#     s=(x//100)**3+(x%100//10)**3+(x%10)**3
#     if x!=s:
#         continue
#     print(s)
# 或
# for x in range(100,1000):
#     s=str(x)  #转为字符串
#     bai=int(s[0])
#     shi=int(s[1])
#     ge=int(s[2]
#     s=bai**3+shi**3+ge**3
#     if x==s:
#         print(x)
或
for x in range(1,10):
    for y in range(10):
        for z in range(10):
            a=x*100+y*10+z
            if a==x**3+y**3+z**3:
