# def fry_egg():
#     print("打开天然气")
#     try:
#         count=int(input("请输入鸡蛋个数"))
#         print("完成煎蛋，共煎%d个鸡蛋"% count)
#     finally:
#         print("关闭天然气")
# fry_egg()









# def make_except():
#     print("函数开始")

#     # raise ZeroDivisionError
#     # raise ValueError
#     e=ValueError("值错误")
#     raise e

#     print("函数结束")
# try:
#     make_except()
# except ZeroDivisionError:
#     print("接受到make_except发出的错误通知")
# except ValueError as err:
#     print('',err)
# print("程序正常结束")



def fa():
    print("函数开始")
    raise ValueError("故意制造的一个错误")
    print("函数结束")
def fb():
    print("fb开始")
    try:

        fa()
    except ValueError as err:
        print("fa里发生了值错误已处理")
        raise
    print("fb结束")
try:
    fb()
except ValueError:
    print("再一次收到fb内部发生的错误")