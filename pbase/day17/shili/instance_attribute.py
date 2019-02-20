


# #示意创建和使用实例属性

# class Dog:
#     '''这是一种可爱的小动物'''
#     def eat(self,food):
#         print(self.color,'的',self.kinds,'正在吃',food)
#         #以下让当前的小狗自己记住吃的是什么
#         self.last_food=food
#     def show_info(self):
#         '''显示信息'''
#         print(self.color,'的',self.kinds,'上次吃的是',self.last_food)

# dog1=Dog()
# dog1.kinds='哈士奇'   #创建属性
# dog1.color='黑白相间'    #创建属性
# dog1.color='白色'      #修改属性

# print(dog1.color,'的',dog1.kinds)
# dog1.eat("骨头")

# dog2=Dog()
# dog2.color='棕色'
# dog2.kinds='藏獒'
# dog2.eat('狗粮')


# dog1.show_info()
# dog2.show_info()





# 练习：
#     定义一个‘人’类
#      class Human:
#       def set_info(self, name, age, address='不详'):
#           '''此方法为'人', 添加:姓名,年龄，家庭住址属性'''
#           # ... 此处自己实现
#       def show_info(self):
#           '''此处显示此人的信息'''
#           # ... 此处自己实现
#         如:
#         h1 = Human()
#         h1.set_info('小张', 20, '北京市朝阳区')
#         h2 = Human()
#         h2.set_info('小李', 18)
#         h1.show_info()  # 小张 今年 20 岁 家庭住址: 北京市朝阳区
#         h2.show_info()  # 小李 今年 18 岁 家庭住址: 不详


class Human:
    def set_info(self,name,age,address='不详'):
        self.name=name
        self.age=age
        self.address=address

    
    def show_info(self):
        print(self.name,'今年',self.age,'岁','家庭住址',self.address)
h1 = Human()
h1.set_info('小张', 20, '北京市朝阳区')
h2 = Human()
h2.set_info('小李', 18)
h1.show_info()  # 小张 今年 20 岁 家庭住址: 北京市朝阳区
h2.show_info()  # 小李 今年 18 岁 家庭住址: 不详














# class Human:
#     def set_info(self,name,age,address='不详'):
#         print('姓名',self.name,'年龄',self.age,'家庭住址',self.address)

    
#     def show_info(self):
#         print(self.name,'今年',self.age,'岁','家庭住址',self.address)
# h1 = Human()
# h1.name='小张'
# h1.age=20 
# h1.address='北京市朝阳区'
# h2 = Human()
# h2.name='小李'
# h2.age=18
# h2.address='不详'

# h1.show_info()  # 小张 今年 20 岁 家庭住址: 北京市朝阳区
# h2.show_info()  # 小李 今年 18 岁 家庭住址: 不详