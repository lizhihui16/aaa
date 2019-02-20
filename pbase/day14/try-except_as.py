# def div_apple(n):
#     print("现在有%d个苹果，您想分给几个人？"% n)
#     s=input('请输入人数：')
#     count=int(s)            #可能触发ValueError错误
#     result=n/count          #ZeroDivisionError
#     print("每个人分类%d个苹果"% result)

# try:
#     div_apple(10)
# except ValueError as err:
#     print('分苹果时发s生值错误')
#     print("发生错误的原因：",err)
#     print('把苹果拿回来')
# except ZeroDivisionError:
#     print('没有人来拿苹果，苹果被收回')
# print('程序正常结束')






def div_apple(n):
    print("现在有%d个苹果，您想分给几个人？"% n)
    s=input('请输入人数：')
    count=int(s)            #可能触发ValueError错误
    result=n/count          #ZeroDivisionError
    print("每个人分类%d个苹果"% result)

try:
    div_apple(10)
    print('分苹果结束')
except :
    print('有异常发生')
else:
    print('没有异常方式')
finally:
    print('我是try的子句的finally子句')
    print('我一定会执行')
print('程序正常结束')
