# 猜数字游戏：
#     随机生成一个0-100之间的整数，用变量x绑定，让用户输入一个数y，输出猜数字的结果
#     1）如果y等于生成的数x，则提示“恭喜您猜对了”，并退出程序
#     2）如果y大于x，则提示’您猜大了‘，然后继续猜下一次
#     3）如果y小于x，则提示’您猜小了‘
#     直到猜对为止，最后显示用户猜数字的次数后退出程序
# import random
# x=random.randrange(101)
# # print(x)
# i=0
# while True:
    
#     n=int(input('数字'))
#     i+=1
#     if n>x:
#         print("您猜大了")
#     elif n<x:
#         print('您猜小了')
#     elif n==x:
#         print('猜对了')
#         break
# print('您共猜了%d次' % i)




#   1. 模拟'斗地主'发牌 
#     牌共54张
#     花色:
#        黑桃('\u2660'), 梅花('\u2663'), 方块('\u2666'), 红桃('\u2665')
#     大小王
#     数字:
#        A0~10JQK
#     1) 生成54张片
#     2) 三个人玩牌，每人发17张,底牌留三张
#       输入回车, 打印第1个人的17张牌
#       输入回车, 打印第2个人的17张牌
#       输入回车, 打印第3个人的17张牌
#       输入回车, 打印3张底牌

# poke=['大王','小王']
# kinds=['\u2660','\u2663','\u2665','\u2666']
# numbers=['A']+[str(x) for x in range(2,11)]+list('JQK')

# for k in kinds:
#     for n in numbers:
#         poke.append(k+n)

# poke2=poke.copy()
# import random
# random.shuffle(poke2)
# play1=poke2[:17]
# play2=poke2[17:34]
# play3=poke2[34:51]
# play4=poke2[51:]

# poke2.clear()

# input("请输入回车键发给第一个人")
# print(play1)
# input("请输入回车键发给第二个人")
# print(play2)
# input("请输入回车键发给第三个人")
# print(play3)
# input("请输入回车键发底牌")
# print(play４)





# for x in play1:
#     if x in poke2:
#         poke2.remove(x)





# import random as R
# l=['\u2660','\u2663','\u2665','\u2666']
# L=['A',2,3,4,5,6,7,8,9,10,'j','q','k']
# d=['大王','小王']
# for x in l:
#     for y in L:
#         d.append(x+str(y))
# print(d)
# while True:
#     n=input('')
#     a=R.sample(d,17)
#     for b in a:
#         d.remove(b)
#     print(a)
#     if len(d)==3:
#         n=input('')
#         print(d)
#         break




