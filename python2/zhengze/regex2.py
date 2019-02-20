
    # 找一个文档，使用正则表达式
    # １、匹配其中大写字母开头的单词
    # ２、匹配其中所有数字
import re
f = open('/home/tarena/aid1808/python2/zhengze/LICENSE.txt','r')
data = f.read()

# pattern = r"[A-Z][a-zA-Z]*"
# pattern = r"\b[A-Z]\S*"


l = re.findall(pattern,data)
print(l)

# d = r'(\d+[./|\d]?[0-9]?%?)'
# d = r'(-?\d+[./%|\d]?\d?)'
# d = r'(-?\d*[./]?\d+%?)'
d = r'(-?\d+\.?/?\d+%?)'

l = re.findall(d,data)
print(l)
f.close()



# l = re.match(r'(\w{7,12}@(163|qq)\.com)','djhs fhdsdsh@163.com 10515281@qq.com')
# print(dir(l))
# print(l.group)

# print(re.findall('1\d{10}','13888888888 898786 1453514 51156556656'))