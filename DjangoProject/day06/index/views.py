from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse

from .forms import *
# Create your views here.


def request_views(request):
    # print(dir(request))
    # print(request.META)
    scheme=request.scheme
    body=request.body
    path=request.path
    host=request.get_host()
    method=request.method
    get=request.GET
    post=request.POST
    cookies=request.COOKIES

    return render(request,'01-request.html',locals())


def referer_views(request):
    #获取请求源地址，如果没有源地址，则获取一个'/'
    referer=request.META.get('HTTP_REFERER','/')
    return HttpResponse('请求源地址:'+referer)

def login_views(request):
    if request.method=="GET":
        return render(request,'02-login.html',locals())
    else:
        #接受前端传递过来的数据
        uname=request.POST['uname']
        upwd=request.POST['upwd']
        print(uname,upwd)
        return HttpResponse("POST接受成功")


def form_views(request):
    if request.method=='GET':
        form=RemarkForm()
        return render(request,'04-form.html',locals())
    else:
        #1.通过RemarkForm的构造函数，接受请求提交数据
        form=RemarkForm(request.POST)

        #2.通过验证
        if form.is_valid():
            #3.通过验证后取值
            cd=form.cleaned_data
            print(cd)
        return HttpResponse('取值成功')

def modelform_views(request):
    if request.method=='GET':
        #创建RegisterForm的对象,并发送到模板上
        form=RegisterForm()
        return render(request,'05-modelform.html',locals())
    else:
        #将request.post传递给RegisterForm的构造函数
        form = RegisterForm(request.POST)
        #让form通过验证
        if form.is_valid():
            # 取值
            user=User(**form.cleaned_data)
            print(user.uname,user.upwd,user.uemail)
            user.save()
        return redirect(reverse('a'))



def model_views(request):
    if request.method=='GET':
        #创建RegisterForm的对象,并发送到模板上
        form=RegisterForm()
        return render(request,'06-modelform.html',locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            if User.objects.filter(uname=user.uname,upwd=user.upwd):
                return HttpResponse('登录成功')
            else:
                return redirect(reverse('a'))












