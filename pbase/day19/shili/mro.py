


#示意__mro__类的属性和用法

# class A:
#     def go(self):
#         print('A')
# class B(A):
#     def go(self):
#         print('B')
#         super().go() #C
# class C(A):
#     def go(self):
#         print('C')
# class D(B,C):
#     def go(self):
#         print('D')     #D
#         super().go()  #B
# d=D()
# d.go()


s="I'm a 'Teacher'"
s1=str(s)
print(s1)
s2=repr(s)
print(s2)