#   有两个人（ Human ）:
#     1. 姓名: 张三，年龄: 35岁
#     2. 姓名: 李四，年龄: 8岁
#     行为:
#       1. 教别人学东西 teach
#       2. 工作赚钱 work
#       3. 借钱 borrow
    #   4. 显示自己的信息
#     用程序描述如下事情:
#       张三 教 李四 学 python
#       李四 教 张三 学 王者荣耀
#       张三 上班 赚了 1000元钱
#       李四 向 张三 借了 200元钱
#       ３５岁的张三有钱８００元，他学会的技能是：王者荣耀
# 　　　　８岁的李四有钱２００元，他学会的技能是：python

class Human:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
        self.money=0  #钱数
        self.skill=[]   # 技能
    def teach(self,other,skill):
        print(self.name,'教',other.name,skill)
        other.skill.append(skill)
    def work(self,money):
        print(self.name,"上班赚了",money,'元钱')
        self.money+=money
    def borrow(self,b,c):
        if c>b.money:
            print('借钱失败')
        else:
            print(self.name,'向',b.name,'借了',c,'元钱')
            self.money+=c
            b.money-=c
    def show_info(self):
        print(self.age,'岁的',self.name,'有钱',self.money,'元','他学会的技能是:',str(self.skill[0]))
zhang3=Human('张三',35)
li4=Human('李四',8)

zhang3.teach(li4,'python')
li4.teach(zhang3,'王者荣耀')

zhang3.work(1000)
li4.borrow(zhang3,200)

zhang3.show_info()
li4.show_info()
