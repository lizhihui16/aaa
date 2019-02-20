# 示例示意文件的打开操作
# 打开文件
# try:
# f=open("mynote.txt")   #打开文件，用f绑定文件流对象

# print("成功打开文件")



# f.close()
# # except:
# print("成功关闭文件")



# 文件打开和读
try:
    f=open("/home/tarena/aid1808/pbase/day16/code/mynote.txt",'r')   #打开文件，用f绑定文件流对象

    s=f.readline()
    print("您读到的是:",s)

    print("成功打开文件")



    f.close()
except:
    print("成功关闭文件")
