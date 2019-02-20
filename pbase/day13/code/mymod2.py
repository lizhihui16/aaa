#此示例示意模块内的__all__列表的定义方式和作用
#限制别人用from import *语句时只能导入：f3 var1

__all__=['f3','var1']
def f1():
    pass

def f2():
    f1()

def f3():
    f2()

var1='aaaa'
var2='bbbb'
