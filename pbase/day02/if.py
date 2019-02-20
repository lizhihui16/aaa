#输入一个数，判断这个数是奇数还是偶数
# x=int(input("请输入一个整数"))
# if x%2==0:
#     print("是偶数")
# else:
#     print("是奇数")

# 任意输入一个整数
# １）判断这个数是否大于１００
# ２）判断这个数是否小于０
# ３）判断这个数是否在５０～１５０之间
# x=int(input("请输入一个整数"))
# if 100<x:
#     print(x,"大于100")
# else:
#     print(x,"不大于100")

# if x<0:
#     print(x,"小于０")
# else:
#     print(x,"不小于０")

# if 50<x<150:
#     print(x,"在50~150之间")
# else:
#     print(x,"不在50~150之间")


# 输入一个整数，判断这个数是正数，负数，零
# num=int(input("请输入一个整数："))
# if num>0:
#     print(num,'正数')
# elif num<0:
#     print(num,"是负数")
# # elif num==0:
# else:
#     print(num,"是零")
# print("程序结束")



# 1.输入一个季度（１～４），输出这个季度有那几个月，如果输入不是１～４的数，则提示用户您输错了


# n=int(input("请输入季度"))
# if n==1:
#     print(1,"月",2,"月",3,"月")
# elif n==2:
#     print(4,"月",5,"月",6,"月")
# elif n==3:
#     print(7,"月",8,"月",9,"月")
# elif n==4:
#     print(10,"月",11,"月",12,"月")
# else:
#     print("输错了")

# n=int(input("请输入季度（１－４）"))
# if n==1:
#     print("春季有1,2,3月")
# elif n==2:
#     print("夏季有4,5,6月")
# elif n==3:
#     print("秋季有7,8,9月")
# elif n==4:
#     print("冬季有10,11,12月")
# else:
#     print("您输错了")


# 2.输入一年中的月份（１～１２），输出这个月在哪个季度，如果输入的是其他数，则提示您输错了
# m=int(input("输入月份"))
# if 0<m<=3:
#     print("春季")
# elif 3<m<=6:
#     print("夏季")
# elif 6<m<=9:
#     print("秋季")
# elif 9<m<=12:
#     print("冬季")
# else:
#     print("您输错了")


# n=int(input("请输入月份（１－１２）"))
# if 1<=n<=12:
#     print("用户输入的是合法的月份")
#     if n<=3:
#         print("春季")
#     elif n<=6:
#         print("夏季")
#     elif n<=9:
#         print("秋季")
#     else:
#         print("冬季")
# else:
#     print("您输错了")


# n=int(input("输入一个整数"))
# if n>=0:
#     print(n)
# else:
#     print(-1*n)


#此示例示意条件表达式的语法和用法
#商城促销满１００减２０
# money=int(input("总金额"))
# pay=money-20 if money>=100 else money
# print("您需要支付的：",pay,"元")

# 写程序，输入一个数，用条件表达式计算这个数的绝对值并打印出来
# n=int(input(''))
# n=-n if n<0 else n
# print(n)

#让用户输入一个学生成绩（０－100)之间，判断是否为有效成绩
# x=int(input(''))
# if 0<=x<=100:
#     pass
# else:
#     print("输入错误")


# １．北京出租车计价器
#     收费标准：３公里以内收费１３元
#     基本单价:２．３元／公里（超出３公里以内）
#     空驶费：超过１５公里后，每公里加收单价的５０％空驶费（即３．４５元／公里）
#     要求：
#     输入公里数，打印出费用金额（以元为单位四舍五入）
# km=float(input("请输入公里数: "))
# pay=0
# if 0<=km<=3:
#     pay=13
# elif 3<=km<=15:
#     pay=13+2.3*(km-3)
# elif km>15:
#     pay=13+2.3*(km-3)+2.3*0.5*(km-15)
# print(pay)
# print(round(pay))


# a=int(input("输入公里数"))
# if a>0:
#     if a<=3:
#         print("行驶公里数",a,13)
#     elif a<=15:
#         print("行驶公里数",a,round(13+2.3*(a-3)))
#     else:
#         print("行驶公里数",a,round(13+2.3*(15-3)+(2.3+2.3/2)*(a-15)))


# ２．输入一个学生的三科成绩
#         打印出最高分是多少？
#         打印出最低分是多少？
#         打印出平均分是多少？

# a=int(input("数学"))
# b=int(input("语文"))
# c=int(input("英语"))
# if a>=b:
#     if a<=c:
#         print("最高分",c,"最低分",b,"平均分",(a+b+c)/3)
#     elif a>c:
#         print("最高分",a,"最低分",b if b<c else c,"平均分",(a+b+c)/3)
# elif a<b:
#     if b<=c:
#         print("最高分",c,"最低分",a,"平均分",(a+b+c)/3)
#     elif b>c:
#         print("最高分",b,"最低分",a if a<c else c,"平均分",(a+b+c)/3)

# zuida=a
# if b>zuida：
#     zuida=b
# if zuida<c:
#     zuida=c




# ３．给出一个年份，判断是否为闰年并打印结果
# 规则：每四年一闰，每百年不闰，四百年又闰
# ２０１６　闰年
# ２１００　不是闰年
# ２４００　是闰年
# n=int(input("年份"))
# if n%4==0:
#     if n%100!=0 or n%400==0:
#         print("闰年")
#     else:
#         print("不是闰年")
# else:
#     print("不是闰年")


# n=int(input("年份"))
# if (n%4==0 and n%100!=0) or n%400==0:

#     print("闰年")

# else:
#     print("不是闰年")


# ４．ＢＭＩ（Body Mass Index)指数，又称身体质量指数
# ＢＭＩ公式：BMI=体重（公斤）／身高的平方（米）
# 标准表：
# ＢＭＩ<18.5　　　体重过轻
# 18.5<=BMI<24  　正常范围
# BMI>＝24　　　　　体重过重
# 输入身高和体重，打印ＢＭＩ值，并打印体重状况
# a=float(input("体重"))
# b=float(input("身高"))
# #BMI=round(a/b**2,1)
# BMI=a/b**2
# if BMI<=18.5:
#     print(a,"公斤",b,"米",BMI,"身体过轻")
# elif BMI<24:
#     print(a,"公斤",b,"米",BMI,"正常范围")
# else:
#     print(a,"公斤",b,"米",BMI,"身体过重")

