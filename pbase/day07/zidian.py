# 创建一个字典:d={'name':'tarena','age':15}  为此字典添加地址(address)键,
# 对应的值为"北京市海盯区",如果如下:
# d={'name':'tarend','age':16,'address':"北京市海定区"}  #字面值
# d=dict([('name','tarena'),('age',15)])     #用可迭代对象创建字典
# d=dict(name='tarena',age=15)    #关键字传参
# d['address']="北京海淀区"
# print(d)

# 1.写程序,实现以下要求:
#     1.将如下数据形成一个字典seasons:
#     键         值
#     1-------->'春季有1,2,3月'
#     2-------->'夏季有4,5,6月'
#     3-------->'秋季有7,7,9月'
#     4-------->'冬季有10,11,12月'
# d=dict(([1,'春季有1,2,3月'],[2,'夏季有4,5,6月'],
#       [3,'秋季有7,7,9月'],[4,'冬季有10,11,12月']))
# print(d)
# 或
# d={}
# d[1]='春季有1,2,3月'
# d[2]='夏季有4,5,6月'
# d[3]='秋季有7,7,9月'
# d[4]='冬季有10,11,12月'
# print(d)
# 2.让用户输入一个整数,代表季度,打印这个季度的信息,如果用户输入的信息不存在与字典内,
# 则打印"信息不存在"
# n=int(input())
# if n in d:
#     print(d[n])
# else:
#     print('信息不存在')
# a=int(input('zhengshu '))
# if 0<a<5:
#     if a==1:
#         print(d[1])
#     elif a==2:
#         print(d[2])
#     elif a==3:
#         print(d[3])
#     elif a==4:
#         print(d[4])
# else:
#     print('信息不存在')


# s={'name':'tarena',(2001,1,1):"生日"}
# for k in s:  # k用来绑定字典的键
#     print(k,'对应的值是:',s[k])

# 输入一段字符串,打印出这个字符串中出现过的字符及出现的次数
# 如:
# 输入: ABCDABCABA
# 打印:
# a:4次
# b:3次
# c:2次
# d:1次
# s=input('请输入文字: ')
# # 方法1:
# 用字典来存储数据,键为字母,值为出现次数
# d={}
# for ch in s:  #ch 绑定每一个字符
#        #判断如果ch已经出现过,将原有计数加1
#     if ch in d:
#         d[ch]=d[ch]+1
#         #ch没有出现过,要在d内创建ch键,值为1
#     else:
#         d[ch]=1
# for k,v in d.items():
#     print(k,':',v,'次')
# # print(d)
#方法2
# #先将字符串去重,放入到列表中
# L=[]#用来存放出现过得字符
# for ch in s:
#     #如果ch没有在L中,说明第一次出现,放到L中
#     if ch not in L:
#         L.append(ch)
# print(L)
# for ch in L:
#     print(ch,',',s.count(ch),'次')


# 2. 有如下字符串:
# L=['tarena','xiaozhang','hello']
# 要生成键为单词,值为单词长度的字典:
# L=['tarena','xiaozhang','hello']
# L={x: len(x) for x in L}
# print(L)



# 1.已知有两个等长的列表
# list1=[1001,1002,1003,1004]
# list2=["Tom","Jerry","Spike","Tyke"]
# 写程序生成如下字典:
# {"Tom":1001,"Jerry":1002,"Spike":1003,"Tyke":1004}
# 方法1:
# d={}
# for i in range(len(list1)):
#     d[list[i]]=list1
# print(d)
# 方法2
# {list2[i:list1[i] for i in range(len(list1))}
# 方法3
# list1=[1001,1002,1003,1004]
# list2=["Tom","Jerry","Spike","Tyke"]
# L={x:y for y in list1 for x in list2}
# print(L)


# 2.任意输入多个学生的姓名,年龄,成绩,每个学生信息存入一个字典中,然后再放入列表中(每个学生信息
# 需要手动输入)
# 如:
# 请输入姓名:tarena
# 请输入年龄:15
# 请输入成绩:99
# 请输入姓名:name2
# 请输入年龄:22
# 请输入成绩:100
# 请输入姓名:<直接回车结束输入>
# 在程序内部生成如下列表:
# L=[{'name',:tarena,'age':15,'score':99},
# {'name',:name2,'age':22,'score':100}]
# 1)打印出上述列表
# 2)以下列表格的形式打印出上述信息
# +---------------+----------+----------+
# |      name     |    age   |  score   |
# +---------------+----------+----------+
# |    tarena     |    15    |    99    |
# |    name2      |    22    |    100   |
# +---------------+----------+----------+
# l=[]
# m={}
# a=input("name: ")
# while a!=' ':
#     b=int(input('age: '))
#     c=int(input('score: '))
#     L={'age':b,'score':c,'name':a}
#     # # print(L)
#     l.append(L)
#     a=input("name: ")
# print(l)

# n='+'+'-'*17+'+'+"-"*15+'+'+'-'*15+'+'
# print(n)
# print("""|       name      |      age      |     scor      |""")
# print(n)
# for x in l:
#     print('|'+' '*7+x.get('name')+' '*7+'|'+" "*5,x.get('age'),' '*6+'|'+" "*6,x.get('score'),' '*4,'|')



# # print('|'+' '*5+l[0].get('name')+' '*6+'|'+" "*5,l[0].get('age'),' '*6+'|'+" "*6,l[0].get('score'),' '*4,'|')
# # print('|'+' '*6+l[1].get('name')+' '*6+'|'+" "*5,l[1].get('age'),' '*6+'|'+" "*5,l[1].get('score'),' '*4,'|')

# print(n)
# 方法2
L=[]

#循环输入姓名,年龄,成绩
while True:
    n=input('请输入姓名: ')
    if not n:#姓名为空结束输入
        break
    a=int(input('请输入年龄: '))
    s=int(input('请输入成绩: '))
    d={}
    d['name']=n
    d['age']=a
    d['score']=s
    L.append(d)
print(L)
print('+---------------+----------+----------+')
print('|      name     |    age   |  score   |')
print('+---------------+----------+----------+')
for d in L:
    # line='|'+d['name'].center(15)
    # line='|'+str(d['age']).center(11)
    # line='|'+str(d['score']).center(9)+'|'
    line='|'+d['name'].center(15)+'|'+str(d['age']).center(10)+'|'+str(d['score']).center(10)+'|'
    print(line)
print('+---------------+----------+----------+')
