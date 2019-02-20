# # 1. 写一个函数mysum(n), 给出一个数n写一个函数来计算
# #     1 + 2 + 3 + 4 + ...... + n的和
# #     (要求用函数来做)
# # def mysum(n):
# #     ....
# # print(mysum(100))  # 5050

# # def mysum(n):
# #     s=0
# #     for x in range(n+1):
# #         s+=x
# #     return s
# # n=int(input('数'))
# # print(mysum(n))


# # 2. 写一个函数myfac 来计算n!(n的阶乘)
# #     n! = 1*2*3*4*....*n
# # def myfac(n):
# #     ....
# # print(myfac(5))  # 120

# # def myfac(n):
# #     s=1
# #     for x in range(1,n+1):
# #         s*=x
# #     return s
# # n=int(input('数'))
# # print(myfac(n))


# # 3. 给出一个数n, 写一个函数计算:
# # 1 + 2**2 + 3**3 + 4**4 + .... .+ n**n的和  
# # (n给个小点的数)
# # def f1(n):
# #     s=0
# #     for x in range(1,n+1):
# #         s=s+x**x
# #     return s
# # n=int(input('数'))
# # print(f1(n))

# # def f1(n):
# #     for x in range(1,n+1):
# #         if x==1:
# #             print('1'.center(n))
# #         elif x==2:
# #             print('1 1'.center(n))
# #         elif x>2:
# #             for a in range(1,x,x-2): 
# #                 print(a,end=' ')
                   
# #             # print(end=" ",sep=" ")

# # f1(4)


# # 6.实现带界面的学生信息管理系统的项目
# # +---------------------------+
# # | 1) 添加学生信息             |
# # | 2) 显示学生信息             |
# # | 3) 删除学生信息             |
# # | 4) 修改学生成绩             |
# # | 5) 退出                    |
# # +---------------------------+
# # (要求：用函数来实现，每个功能写一个函数与之想对应)
# L=[]
# def input1():
    
#     while True:
#         a=input("姓名:")
#         if not a:
#             break
#         else:           
#             b=int(input("年龄:"))
#             c=int(input("成绩:"))
#             d={}
#             d['name']=a
#             d['age']=b 
#             d['score']=c
#             L.append(d)
#     return L
# # print(input1())

    
# def print1(L):
#     print('+---------------+----------+----------+')
#     print('|      name     |    age   |  score   |')
#     print('+---------------+----------+----------+')
#     for d in L:
#         # line='|'+d['name'].center(15)
#         # line='|'+str(d['age']).center(11)
#         # line='|'+str(d['score']).center(9)+'|'
#         line='|'+d['name'].center(15)+'|'+str(d['age']).center(10)+'|'+str(d['score']).center(10)+'|'
#         print(line)
#     print('+---------------+----------+----------+')
# # L=input1()
# # print(L)
# print1(L)

# def sc():
#     a=input("姓名:")
#     for d in L:
#         if d['name']==a:
#             L.remove(d)
# def xg():
#     a=input("姓名")
#     b=int(input("年龄:"))
#     c=int(input("成绩:"))
#     for d in L:
#         if d['name']==a:
#             d['name']=a
#             d['age']=b
#             d['score']=c
# def main():
#     # infos = []  # 用于保存学生信息的列表
#     while True:
#         # 打印菜单:
#         # show_menu()
#         print("1) 添加学生信息")
#         print("2) 显示学生信息")
#         print("3) 删除学生信息")
#         print("4) 修改学生信息")
#         print("q) 退出")
#         s = input('请选择: ')
#         if s == '1':
#             input1()
#         elif s == '2':
#             print1(L)
#         elif s=='3':
#             sc()
#         elif s=='4':
#             xg()

#         elif s == 'q':
#             break
# main()


class Student:
    def __init__(self,name,a,b):
        self.name=name
        self.a=a
        self.b=b
    def s(self):
        print(self.name,self.a,self.b)
sl=Student('Bob',13888888888,'666666@qq.com')
sl.s()
