s = 100 #总钱数
l = []

# 思路１　先求出100文钱可以买多少种组合

for a in range(1,int(100/5+1)): # a代表公鸡，最少能买1只，最多买20只，用for循环遍历
    b = (100 - a*5)//3 #　给定公鸡的数量后，求母鸡最多可以买多少只
    c = (100 - a*5)%3*3 #　给定公鸡和母鸡数量后，小鸡可以买多少只
    if b and c and a+b+c==100: #　购买组合中，三种鸡的数量必须大于１
        l.append((a,b,c)) # 将此种组合以元组的形式放入列表
print(l) #没有满足要求的组合





#　上面方法是遍历公鸡的数量后，且在母鸡数量最大的情况下，三种鸡的组合
# 下面方法是遍历公鸡数量后，再遍历母鸡的数量，求三种鸡的组合
for a in range(1,int(100/5+1)):
    b = (100 - a*5)//3
    if b :
        for i in range(1,b+1): #　i是母鸡的数量，在给定公鸡的数量情况下，从1到最大遍历一下
            c = (100-a*5-i*3)*3 # 小鸡的数量
            if c and a + i + c ==100:
                l.append((a,i,c))
print(l)
