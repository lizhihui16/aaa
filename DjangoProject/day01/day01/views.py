from django.http import HttpResponse



def show_views(request):
    return HttpResponse("我的第一个Django处理程序")

def sh_views(request):
    return HttpResponse('访问路径中包含sh的处理程序')


#匹配访问路径为/show/四位数字
#参数year:表示的是四位数字
def show1_views(request,year):
    return HttpResponse('传递进来的年份为：'+year)

def show2_views(request,a,b,c):
    return HttpResponse('生日为'+a+'年'+b+'月'+c+'日')

def show3_views(request,name,age):
    return HttpResponse("姓名：%s,年龄：%d"%(name,age))
