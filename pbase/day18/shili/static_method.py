# # 示意静态方法的定义和使用

# class A:
#     @staticmethod
#     def myadd(a,b):
#         '''这是静态方法'''
#         return a+b

# #用类来调用静态方法
# print(A.myadd(100,200))   #300
# a=A()
# #用此类的实例来调用静态方法
# print(a.myadd(300,400))   #700






# 用类来描述一个学生的信息(可以修改之前写的Student类)

# class Student:
#     ....此处自己实现

# 学生信息有:
#     姓名，年龄，成绩
# 将这些学生对象存于列表中,可以任意添加和删除学生信息
#     1) 打印学生的个数
#     2) 打印出所有学生的平均成绩
#     3) 打印出所有学生的平均年龄
# (建议用类变量存储学生的个数)

class Student:
    infos=[]
    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.score=s

    @classmethod
    def input_student(cls):
        while True:
            n=input('')
            if not n:
                break
            a=int(input(''))
            s=int(input(''))
            cls.infos.append(Student(n,a,s))

    @classmethod
    def del_student(cls):
        n=input('请输入要删除的学生姓名')
        for index,s in enumerate(cls.infos):
            if s.name==n:
                del cls.infos[index]
                return

    @classmethod
    def print_student_count(cls):
        '打印学生个数'
        print(len(cls.infos))

    @classmethod
    def print_avg_score(cls):
        '打印出所有学生的平均成绩'
        total_score=sum(s.score for s in cls.infos)
        print("平均成绩",total_score/len(cls.infos))

    @classmethod
    def output_student(cls):
        for s in cls.infos:
            print(s.name,s.age,s.score)

Student.input_student()
Student.output_student()
Student.del_student()
Student.output_student()
Student.print_student_count()
Student.print_avg_score()


# class Student:
#     def __init__(self,n,a,s):
#         self.name=n
#         self.age=a
#         self.score=s
# infos=[]
# def input_student():
#     L=[]
#     while True:
#         n=input('')
#         if not n:
#             break
#         a=int(input(''))
#         s=int(input(''))
#         L.append(Student(n,a,s))
#     return L
# def del_student(L):
#     n=input('请输入要删除的学生姓名')
#     for index,s in enumerate(L):
#         if s.name==n:
#             del L[index]
#             return
# def print_student_count(L):
#     '打印学生个数'
#     print(len(L))
# def print_avg_score(L):
    '打印出所有学生的平均成绩'
    total_score=sum(s.score for s in L)
    print("平均成绩",total_score/len(L))

# infos+=input_student()
# print(infos)
# del_student(infos)
# print(infos)
# print_student_count(infos)
# print_avg_score(infos)











# class Stufent:
#     xues_count=0
#     xues_age=0
#     xues_score=0

#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#         self.__class__.xues_count+=1
#         self.__class__.xues_age+=int(age)
#         self.__class__.xues_score+=int(score)
#     def set_score(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#     # def pj(self,score):

#     def show_info(self):
#         print('1',self.name,'今年',self.age,'成绩',self.score)
# L=[]
# while True:
#     name=input('')
#     if not name:
#         break
#     age=input('')
#     score=input('')
#     L.append(Stufent(name,age,score))

# # for s in L:
# #     s.show_info()
# #     s.set_score(name,age,score)
# for s in L:
#     s.show_info()   
# print(Stufent.xues_count)
# print(Stufent.xues_age//Stufent.xues_count)
# print(Stufent.xues_score//Stufent.xues_count)
