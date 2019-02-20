

# try:
#     with open('text.txt','w') as f:

#         s=int(input('请输入整数')) #

#         f.write('hello')
# except OSError:
#     print("文件打开失败")
# except:
#     print('写取数据失败')





# try:
#     f=open('text.txt','w')
#     try:

#         s=int(input('请输入整数')) #

#         f.write('hello')

# except OSError:
#     print("文件打开失败")
# except:
#     print('写取数据失败')


# def mycopy(src_file,dst_file):
#     '''
#     src_file:源文件名
#     dst_file:目标文件名
#     '''
#     try:
#         with open(src_filr,'rb') as fr,\
#                 open(dst_file,'wb') as fw: #写
#             while True:
#                 datd=fr.read(4096)
#                 if not data:
#                     break
#                 fw.write(data)
#     except OSError:
#         print('复制失败')
#         # return False 
#     except:
#         print('可能u盘被拔出')
#     return True
# s = input("请输入源文件: ")
# d= input("请输入目标文件: ")
# if mycopy(s,d):
#     print('复制成功')
# else:
#     print('复制失败')










class A:
    v=100
    def __init__(self):
            self.v=200
a1=A()
a2=A()
del a2.v

print(A.v)
print(a1.v)
print(a2.v)
print(a1.__class__.v)