#   经理有:曹操,刘备,孙权
#   技术员有:曹操,孙权,张飞,关羽
#   用集合求:
#   1.即是经理也是技术员的人是谁
#   2.是经理,但不是技术员的人是谁
#   3.是技术员,但不是经理的人是谁
#   4.张飞是经理吗
#   5.身兼一职的人有谁
#   6.经理和技术员共有几人
# s1={'曹操','刘备','孙权'}
# s2={'曹操','孙权','张飞','关羽'}
# print(s1&s2)
# print(s1-s2)
# print(s2-s1)
# if "张飞" in s1:
#     print("是")
# else:
#     print("否")
# print(s1-s2|s2-s1)   #print(s2^s1)
# print(len(s1|s2))