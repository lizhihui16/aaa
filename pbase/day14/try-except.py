# def div_apple(n):
#     print("现在有%d个苹果，您想分给几个人？"% n)
#     s=input('请输入人数：')
#     count=int(s)            #可能触发ValueError错误
#     result=n/count          #ZeroDivisionError
#     print("每个人分类%d个苹果"% result)

# try:
#     div_apple(10)
# except ValueError:
#     print('分苹果时发s生值错误，已捕获并转为正常状态')
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
except ValueError:
    print('有值错误发生')
except:
    print('此时方式的错误是值错误以外的错误类型')
    print('已捕获并转为正常状态')
print('程序正常结束')
