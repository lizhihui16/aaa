# f=open("mynote.txt",'rb')
# b=f.read()  #返回的是字节串
# print('读取的长度:',len(b))
# print('内容是:',b)
# s=b.decode()
# print('转为字符串s为',s)
# f.close


#字符串
b='Welcome to 中国'
#字符串转为字节串
s=b.encode()
print(s)