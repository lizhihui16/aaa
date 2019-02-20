import re

# s='Hello World'
# pattern = r'hello'
# regex = re.compile(pattern,flags=re.I)

# s='''Hello World
# hello kitty
# 您好，北京
# '''
# pattern = r'.+'
# regex = re.compile(pattern,re.S)

# s='''Hello World
# hello kitty
# 您好，北京
# '''
# pattern = r'^hello'

s='''hello world
nihao beijing
'''
pattern = r'''hello  #匹配hello
\s+   #匹配空格
world  #匹配world
'''

regex = re.compile(pattern,re.X)
try:
    s = regex.search(s).group()
except Exception:
    print('没有匹配到内容')
else:
    print(s)