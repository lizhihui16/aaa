# 导入自定义模块并调用其中函数
import mymod

mymod.mysum(100)
print(mymod.name1)

from mymod import myfac as fac
fac(6)

from mymod import *
mysum(200)
print(name2)


import os
print(os.name)


print('test_mymod.py里的__name__属性值为：')
print('++++：',__name__)