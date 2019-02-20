#此示例特殊的控制字符及转义字符的用法
# print("ABCD\rab")
# print("ABCD\tab")
# print("ABcdffff\tab")
# print("ABCD\bab")


# 写一个程序，打印一个高度为４行的矩形方框
# 如：
# 请输入宽度：１０
# 打印：
# ＃＃＃＃＃＃＃＃＃＃
# ＃　　　　　　　　＃　
# ＃　　　　　　　　＃　
# ＃＃＃＃＃＃＃＃＃＃
# m=int(input('请输入宽度'))
# print("#"*m)
# print("#"+" "*(m-2)+"#")
# print("#"+" "*(m-2)+"#")
# print("#"*m)

# m=int(input('请输入宽度'))

# print("#"*m)
# print("#"," "*(m-2),"#",sep="")
# print("#"," "*(m-2),"#",sep="")
# print("#"*m)


# 输入一个字符串，打印如下内容：
#     1）打印这个字符串的第一个字符
#     2）打印这个字符串最后一个字符
#     3）如果这个字符串的长度为奇数，打印中间这个字符
#     注：求字符串长度的函数是Len（s）

# s=input("输入字符串: ")
# print("第一个字符是：",s[0])
# print("最后一个字符是：",s[-1])
# if len(s)%2!=0:
#     print(s[len(s)//2])

    # (-1)**(n-1)*1/((n-1)*2+1)


# 1.写一个程序，输入一个字符串，把字符串的第一个字符和最后一个字符去掉后，
# 打印出处理后的字符串
# n=input('字符串')
# print(n[1:len(n)-1:1])
#   #print(n[1:-1:-1])


# 2.写一个程序，输入任意一个字符串，判断这个字符串是否是回文
#     （回文是指中心对称的文字）
#     如：上海自来水来自海上
#     ABCCBA 
#     12321
# n=input('字符串')
# if n[::-1]==n:
#     print("是")
# else:
#     print("否")

# 1.写一个程序，输入一个字符串，如果字符串不为空，则把第一个字符的编码值打印出来
# s=input("请输入一个字符串： ")
# if s!='':
#     print("第一个字符的编码是："，ord(s[0]))

# a=input("字符串")
# if a!=None:
#     print(ord(a[0]))

# s=input("请输入一个字符串： ")
# if len(s)!=0:
#     print("第一个字符的编码是：",ord(s[0]))

# 2.写一个程序。输入一个整数（0-65535），打印出这个值所对应的字符
# a=int(input("请输入整数(0~65535): "))
# print(chr(a))

# 1.输入一个字符串，把输入的字符串的空格全部去掉（包括字符串中间的空格）
# 1）打印原字符串及长度
# 2）打印处理后的字符串及长度
# s=input("输入字符串")
# a=s.replace(" ","")
# print(s,len(s))
# print(a,len(a))


#  2.写程序，输入三行文字，让这三行文字在一个方框内居中显示
#     请输入：    hello!
#     请输入：   I'm studing python!
#     请输入：    I like python
#     打印如下:
#      +---------------------+
#      |       hello!        |
#      | I'm studing python! |
#      |    I like python    |
#      +---------------------+
#      注：不要输入中文

# a='hello!'
# b="I'm studing python!"
# c='I like python'
# print("+"+"-"*32+"+")
# print("|",a.center(30),"|")
# print("|",b.center(30),"|")
# print("|",c.center(30),"|")
# print("+"+"-"*32+"+")

# a=input("输入文字")
# b=input("输入文字")
# c=input("输入文字")
# aa=len(a)
# bb=len(b)
# cc=len(c)
# d=max(aa,bb,cc)
# print(d)
# # print("+"+"-"*(d+2)+'+')
# # print('|',a.center(d),'|')
# # print('|',b.center(d),'|')
# # print('|',c.center(d),'|')
# # print("+"+"-"*(d+2)+'+')

# print("+"+"-"*(d+2)+'+')
# print('| '+a.center(d)+' |')
# print('| '+b.center(d)+' |')
# print('| '+c.center(d)+' |')
# print("+"+"-"*(d+2)+'+')
