


#示意初始化的定义及自动调用

# class car:
#     def __init__(self,c,b,m):
#         self.color=c
#         self.brand=b
#         self.model=m
#         print('初始化方法被调用')
#     def run(self,speed):
#         print(self.color,'的',self.brand,self.model,'正在以',speed,'公里／小时的速度行驶')


# a4=car('红色','奥迪','A4')
# a4.run(199)



# 练习:
#   写一个学生类Student类，此类用来描述学生信息
#   　学生信息有：
#     　　姓名，年龄，成绩
#      1) 为该类添加初始化方法，实现在创建对象时自动设置 '姓名', '年龄', '成绩' 属性
#      2) 添加 set_score 方法，能为对象修改成绩信息
#      3) 添加show_info方法打印学生对象的信息
#     class Student:
#         def __init__(.......):
#              .....
#         def set_score(self, score):
#             ....
#         def show_info(self):
#             ....
#     L=[]
#     L.append(Student('小张',20,100))
#     L.append(Student('小李',20))
#     L.append(Student('小赵',19,85))
#     for s in L:
#         s.show_info()
#     L[1.set_score(70)]
#     ...
class Student:
    def __init__(self,name,age,score=0):
            self.name=name
            self.age=age
            self.score=score
    def set_score(self, score):
        self.score=score
        # print(self.name,'今年',self.age,'成绩',self.score)

    def show_info(self):
        print(self.name,'今年',self.age,'成绩',self.score)
L=[]
L.append(Student('小张',20,100))
L.append(Student('小李',20))
L.append(Student('小赵',19,85))
for s in L:
    s.show_info()
L[1].set_score(70)
for s in L:
    s.show_info()