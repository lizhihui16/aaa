from pandas import json

from django.shortcuts import render
from .models import *
from userinfo.models import *
from memberapp.models import *
import logging
from django.http import HttpResponse
# Create your views here.


def add_cart(request):
    #1.声明一个购物车
    new_cart=CartInfo()
    #2.获取用户id
    user_id=request.session.get('user_id')
    #3.获取添加商品的id
    good_id=request.GET.get('goodid')
    #4.获取添加数量
    good_count=request.GET.get('gcount')
    #5.查询商品
    good_=Goods.objects.filter(id=good_id)
    # print(good_)
    #6.查询用户
    user_=UserInfo.objects.get(id=user_id)
    #7.判断商品是否存在
    if len(good_)>0:
        new_cart.user=user_
        new_cart.good=good_[0]

    else:
        print(5)
        return render(request,'cart.html')
    #8.转化数量为整数
    new_cart.ccount=int(good_count)
    #9.查看是否添加过购物车
    #10.如果有＋１
    #11.如果没有保存


    try:
        oldgo=CartInfo.objects.filter(good_id=good_id,user_id=user_id)
        if len(oldgo)>0:
            oldgo[0].ccount=oldgo[0].ccount+int(good_count)
            oldgo[0].save()

        else:
            new_cart.save()
    except BaseException as e:
        logging.warning(e)
    return render(request,'cart.html')



def cart_info(request):
    user_id=request.session.get('user_id')
    find_goods=CartInfo.objects.filter(user=user_id)
    mycartc=0
    if user_id:
        for find_good in find_goods:
            mycartc += find_good.ccount
    return render(request,'cart.html',{'find_goods':find_goods,'mycartc':mycartc})



def delete_cart(request):
    user_id=request.session.get('user_id')
    cart_id=request.GET.get('cart_id')
    try:
        delcart = CartInfo.objects.filter(user_id=user_id,id=cart_id)
        delcart.delete()
    except BaseException as e:
        logging.warning(e)
    content={'status':'ok','text':'删除成功'}
    return HttpResponse(json.dumps(content))







