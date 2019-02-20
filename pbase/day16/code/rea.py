f=open('/home/tarena/aid1808/pbase/day16/data.txt')
while True:
    line=f.readline()
    if line=="":
        break
    line=line.strip()    #去掉末尾的'\n'
    L=line.split()   #将其拆分为字符串列表
    print('姓名：',L[0],'电话：',L[1])
f.close() 

# f=open('/home/tarena/aid1808/pbase/day16/data.txt')
# lines=f.readlines()
# for line in lines:
#     line=line.strip()    #去掉末尾的'\n'
#     L=line.split()   #将其拆分为字符串列表
#     print('姓名：',L[0],'电话：',L[1])
# f.close() 















# f=open('/home/tarena/aid1808/pbase/day16/data.txt')
# s=f.read(3)
# s1=f.read(12)
# print("姓名：",s,"电话：",s1) 
# s2=f.read(3)
# s3=f.read(12)
# print("姓名：",s2,"电话：",s3) 
# s4=f.read(4)
# s5=f.read(13)
# print("姓名：",s4,"电话：",s5) 
