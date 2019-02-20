
# # 练习：
# # 　１.写一个程序，输入很多人的姓名，年龄，家庭住址，保存在文件‘infos.txt'中
# #   　（格式自定义，建议用空格或逗号分隔
# #   　如：info.txt
# #         小李　２０　北京市朝阳区
# #         小张　１８　上海市浦东新区
# #   ２.写一个程序，读入infos.txt中的内容，以如下格式打印：
# #       姓名：　小张，年龄：２０，住址：北京市朝阳区
# def get_infos():
#     '''此函数返回字典组成的列表
#     [{'name':'小张','age':20,'address':'北京市朝阳区'}]
#     '''
#     L=[]
#     while True:
#         n=input("姓名")
#         if not n:
#             break
#         a=int(input("年龄"))
#         addr=input("住址")
#         L.append(dict(name=n,age=a,address=addr))
#     return L
# def save_to_flie(L):
#     try:
#         f=open('infos.txt','w')
#         for d in L:
#             f.write(d['name'])
#             f.write(' ')
#             f.write(str(d['age']))
#             f.write(' ')
#             f.write(d['address'])
#             f.write('\n')
#         f.close()
#     except OSRrror:
#         print('')
# L=get_infos()
# print(L)
# save_to_flie(L)





def read_from_flie():
    L=[]
    try:
        f=open('infos.txt','r')
        while True:
            line=f.readline()
            if not line:
                break
            line=line.rstrip()
            items=line.split()
            d=dict(name=items[0],age=int(items[1]),address=items[2])
            L.append(d)
        f.close()
        print('读取成功')
    except OSError:
        print("打开失败")


    return L
def pint_infos(L):
    print(L)
L=read_from_flie()

pint_infos(L)








# f=open("infos.txt",'a')   #打开文件，用f绑定文件流对象
# while True:
#     a=input("")
#     if not a:
#         break
#     f.write("a")
#     b=int(input(""))
#     c=input("")
#     f.write("\n")

# lines=f.readlines()
# for line in lines:
#     line=line.strip()    #去掉末尾的'\n'
#     L=line.split()   #将其拆分为字符串列表
#     print('姓名：',L[0],'年龄：',L[1],'住址',L[2])

# f.close() 


# print("成功关闭文件")
