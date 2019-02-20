# 练习：
#     写程序实现复制文件功能：
#     要求：
#         １．源文件路径和目标文件路径需要手动输入
#         ２．要考虑关闭文件问题
#         ３．要考虑复制超大文件问题
#         ４．要能复制二进制文件
# src_file = input("请输入源文件: ")
# dst_file = input("请输入目标文件: ")

# # 先打开源文件，准备读数据
# try:
#     src = open(src_file, 'rb')
#     try:
#         # 打开目标文件，准备写数据
#         try:
#             dst = open(dst_file, 'wb')
#             try:
#                 # 开始复制文件，每次复制4K字节,直至复制完成
#                 while True:
#                     b = src.read(4096)  # 4096 = 4k
#                     if not b:
#                         print("复制成功")
#                         break
#                     dst.write(b)
#             finally:
#                 dst.close()
#         except OSError:
#             print("打开写文件", dst_file, '失败')
#     finally:
#         src.close()
# except OSError:
#     print("打开文件", src_file, "失败!")


def mycopy(src_file,dst_file):
    '''
    src_file:源文件名
    dst_file:目标文件名
    '''
    try:
        fr=open(src_filr,'rb')  #读
        try:
            try:
                fw=open(dst_file,'wb')  #写
                try:
                    while True:
                        datd=fr.read(4096)
                        if not data:
                            break
                        fw.write(data)
                except:
                    print('可能u盘被拔出')
                finally:
                    fw.close()
            except　OSError:
                print('打开失败')
                return False
        finally:
            fr.close()  #关闭读文件
    except　OSError:
        print("打开读失败")
        return False    
    return True
s = input("请输入源文件: ")
d= input("请输入目标文件: ")
if mycopy(s,d):
    print('复制成功')
else:
    print('复制失败')