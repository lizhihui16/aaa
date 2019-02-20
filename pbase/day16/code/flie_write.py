

# 打开文件
f=open('myfile.txt','w')
print("打开文件成功")
# 写文件
f.write('这是第一行文字')
f.write('\n\n')
f.write('ABCDEFG')
f.writelines(['aaaaaaaaaaa','bbbbbbbbb','ccccccccccccc'])
print("写成功")

# 关闭文件
f.close
print("文件已关闭")