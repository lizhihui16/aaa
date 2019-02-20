


# 示意用 @property实现getter 和 setter功能
class Student:
    def __init__(self,s):
        self.__score=s
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,s):
        assert 0<=s<=100
        self.__score=s
s1=Student(59)
# print(s1.get_score())
print(s1.score)
s1.score=99
print(s1.score)
s1.score=9999999999999    #触发异常
