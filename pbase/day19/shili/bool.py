


# class A:
#     pass
# a=A()
# print(bool(a))   # True
# if a:
#     print("a为真值")
# else:
#     print("a为假值")



# class A:
#     def __bool__(self):
#         print('__bool__方法被调用')
#         return False
# a=A()
# print(bool(a))   # False
# if a:
#     print("a为真值")
# else:
#     print("a为假值")



class A:
    # def __bool__(self):
    #     print('__bool__方法被调用')
    #     return False
    def __len__(self):
        print("__len__方法被调用")
        return 5
a=A()
print(bool(a))   # False
if a:
    print("a为真值")
else:
    print("a为假值")
