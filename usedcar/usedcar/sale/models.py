from django.db import models
from userinfo.models import *

CAR_CHOISE=((0,'审核中'),(1,'已审核'),(2,'待审核'),(3,'未通过'))




# Create your models here.


# 品牌表Brand
#     名称title(C)
#     logo logo(IM)
#     新车价格newprice(DE)
#     是否删除isDelete(B)
class Brand(models.Model):
    title = models.CharField('名称',max_length=50)
    logo = models.ImageField('logo',upload_to='img/logo',default=False)
    newprice=models.DecimalField('新车价格',max_digits=8,decimal_places=2)
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.title



# 汽车表Carinfo
#     品牌brand（F）
#     上牌日期regist_data(DA)
#     发动机号engineNo(C)
#     公里数mileage(I)
#     维修记录record(C)
#     期望成交价格price(D)
#     图片picture(IM)
#     手续是否齐全formalities(B)
#     是否有债务debt(B)
#     卖家承诺promise(TEXT)
#     审核状态status(Ic)
#     用户user(F)
#     是否删除isDelete

class CarInfo(models.Model):
    brand = models.ForeignKey(Brand)
    regist_data = models.DateField('上牌日期')
    engineNo = models.CharField('发动机号',max_length=50,null=False)
    mileage = models.IntegerField('公里数')
    recoed = models.CharField('维修记录',max_length=200)
    price = models.DecimalField('期望成交价格',max_digits=8,decimal_places=2)
    picture = models.ImageField('图片',upload_to='img/car')
    formalities = models.BooleanField('手续是否齐全',default=False)
    debt = models.BooleanField('是否有债务',default=False)
    promise = models.TextField('卖家承诺',null=True)
    status = models.IntegerField('审核状态',choices=CAR_CHOISE,default=2)
    user = models.ForeignKey(UserInfo)
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.user.username