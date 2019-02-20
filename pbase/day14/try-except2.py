# def div_apple(n):
#     print("现在有%d个苹果，您想分给几个人？"% n)
#     s=input('请输入人数：')
#     count=int(s)            #可能触发ValueError错误
#     result=n/count          #ZeroDivisionError
#     print("每个人分类%d个苹果"% result)

# try:
#     div_apple(10)
# except (ValueError,ZeroDivisionError):
#     print('分苹果时发s生值错误，已捕获并转为正常状态')
# print('程序正常结束')










def div_apple(n):
    print("现在有%d个苹果，您想分给几个人？"% n)
    s=input('请输入人数：')
    count=int(s)            #可能触发ValueError错误
    result=n/count          #ZeroDivisionError
    print("每个人分类%d个苹果"% result)

try:
    div_apple(10)
except :
    print('有异常发生')
else:
    print('没有异常方式')
print('程序正常结束')
