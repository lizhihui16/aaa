# 输出字符串：Tom's pet is a cat. The cai's name is "Tiechui"
# #用转意符号实现
# print("Tom's pet is a cat. The cat's name is \"Tiechui\"")

# 2.实现10以内+ - * / %的计算，要求只能用一个input语句，
# 可能用到if语句，如：input()-->读取字符串 7*7 终端输出 49
# while True:
#     s=input("")
#     s1=int(s[0])
#     s2=int(s[-1])
#     s3=s[1]

#     if s3=="+":
#         print(s1+s2)
#     elif "-" in s:
#         print(s1-s2)
#     elif "//" in s:
#         print(s1//s2)
#     elif "%" in s:
#         print(s1%s2)
#     elif s3=="/":
#         print(s1/s2)
#     elif "*" in s:
#         print(s1*s2)
#     else:
#         break



# 1.编写一个小程序要求实现如下输出
#     请输入名字：
#     请输入年龄：
#     ‘名字’ 今年 ‘年龄’ 岁  #使用占位符
# n=input('请输入姓名： ')
# m=int(input('请输入年龄： '))
# print('%s今年%d岁'%(n,m))



# str1="   My name is Mr Green"
# str2="HELLO"
# 要求分别实现以下输出
# 1）"My name is Mr Green"
# 2）"My Green"
# 3）"   My name is Mr Green"
# 4）"   HELLO"      #宽度为10
# 5）"helli"
# 6）输出str1和str2中长度最长的字符串的长度 # max（）
# str1="   My name is Mr Green"
# str2="HELLO"
# print(str1.strip())
# print(str1.replace("   My name is Mr Green",'My Green'))


# 搜索什么是冒泡排序
# 以下为python的冒泡排序的一种
# l=[1,2,5,3,6,8,4]
# for i in range(len(l)-1,0,-1):
#     print(l[i],end=" ")
# print()
# for i in range(0,len(l),1):
#     print(i)
#     for j in range(i+1,len(l),1):
#         # print(j)
#         if l[j]<l[i]:
#             print(i,l)
#             l[j],l[i]=l[i],l[j]
# print(l)

# s='python2best'
# s1=[3,5,4,2]
# (1)生成列表s2=['p','y','t','h','o','n','2','b','e','s','t']
# (2)将s2列表的值改为['p','y','t','h','o','n','3']
# (3)在s2列表尾部追加元素"!"
# (4)返回列表s2的长度
# (5)删除s2中的元素'3',用pop方法
# (6)清空s2列表中的所有元素
# (7)计算s1列表中各元素的和
# (8)将列表s1中元素按升序排列,然后反转
# s='python2best'
# s1=[3,5,4,2]
# s2=[x for x in s]
# print(s2)
# del s2[-1:-6:-1]
# s2[len(s2):len(s2)]=[3]
# print(s2)
# s2.append('!')
# print(s2)
# s2.pop()
# print(s2)
# s2.clear()
# print(s2)
# print(len(s2))
# print(sum(s1))
# s1.sort()
# print(s1)
# s1.reverse()
# print(s1)
# 1.s1="Welcome to China" 生成列表L为['Welcome','to','china']
#   s2=['hello','tar','gz'] 生成字符串s为"hello.tar.gz"
# s1="Welcome to China"
# print(s1.split(" "))
# s2=['hello','tar','gz']
# print('.'.join(s2))

# 2.请创建一个元组T为(20,30,40,50,40,30,20)  计算t中30的个数
# t=(20,30,40,50,40,30,20)
# print(t.count(30))

# 3.创建一个字典D={"name":"Bob","age":30}  要求:会用两种方法创建,
# 创建新键值对"score":90   age的值改为25
# D={}
# D['name']="Bob"
# D['age']=30
# print(D)
# D['score']=90
# print(D)
# D['age']=25
# print(D)
# print(D['age'])


# 9月13号
#1. l=list()      
# l=[]
# a=()
# a=tuple()
# b={}
# b=dict()
# m=set()
# # ##############3###########
# d={}
# d['name']='Lucy'
# d['age']=20
# 3########################


# 输入一段只包括字母的字符串,不区分大小写,写一个程序,
# 返回此字符中最长的按照顺序排列的子串
# s=input("")
# L[]
# l=''
# for y in s:
#     a=y
#     l=a
#     for x in s:
#         if x>=a:
#             a=x
#             l=l+a
    
#         len(l)

# a=100
# b=200
# s=input("")
# m=eval(s)
# n=exec(s)
# print(m)
# print(n)



# f=open('rarena.txt','wb')
# s2='HelloTarena'
# s=s2.encode()
# print(s)
# f.write(s)
# f.close()
f=open('rarena.txt','rb')
f.read()

print(f.tell())
