# import re 
import re
# pattern = r'abcdef'
pattern = r"(ab)cd(?P<dog>ef)"

regex = re.compile(pattern)

#获取match对象
obj = regex.search('abcdefgh',pos=0,endpos=6)
# print(dir(obj))

#obj属性变量
print(obj.pos)  #目标子串的开始位置
print(obj.endpos)   #目标子串的结束位置
print(obj.re)   #正则表达式
print(obj.string)  #目标字符串
print(obj.lastgroup)
print(obj.lastindex)
print(obj.start()) # 匹配到的起始位置
print(obj.end())  #匹配到的结束位置
print(obj.span()) #匹配到的起止位置


print(obj.group())
print(obj.group('dog'))
print(obj.groupdict())  #捕获组字典
print(obj.groups())#所有子组对应内容