from django.db import models
from userinfo.models import *
from sale.models import *




ORDER_CHOICES=((0,'待支付'),(1,'已支付'),(2,'订单取消'),(3,'订单失败'),(4,'订单完成'))
# Create your models here.



# 出价表Cartinfo （购物车？）
#     价格price(D)
#     买家buser(F)
#     汽车car(F)
class CartInfo(models.Model):
    price = models.DecimalField('价格',max_digits=8,decimal_places=2)
    buser = models.ForeignKey(UserInfo)
    car = models.ForeignKey(CarInfo)

    def __str__(self):
        return self.buser.username



# 订单表Orderinfo
#     用户买家buser(F userinfo)
#     用户卖家suser(F userinfo)
#     汽车car(TEXT)
#     价格price(D)
#     订单号orderNo(C)
#     订单状态status(Ic)
#     时间datetime(DT)
#     是否删除isDelete(B)

class OrderInfo(models.Model):
    buser = models.ForeignKey(UserInfo,related_name='buser')
    suser = models.ForeignKey(UserInfo,related_name='suser')
    car = models.TextField('汽车')
    price = models.DecimalField('价格',max_digits=8,decimal_places=2)
    orderNo = models.CharField('订单号',max_length=50,null=False)
    status = models.IntegerField('订单状态',choices=ORDER_CHOICES)
    datetime = models.DateTimeField('时间',auto_now=True)
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.orderNo
