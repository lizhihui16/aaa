from django.db import models
from django.contrib.auth.models import AbstractUser


SET_CHOICES = ((0,'buy'),(1,'sale'),(2,'admin'))
ROLE_CHOICES = ((0,'女'),(1,'男'))
BANK_CHOICES = ((0,'中国工商银行'),(1,'中国建设银行'),(2,'中国农业银行'),(3,'招商银行'),(4,'中国人民银行'),(5,'邮政银行'))
# Create your models here.
# 用户表Userinfo
#     用户名username(C)
#     密码password(C)
#     真实姓名realname(C)
#     身份证号iden(C)
#     住址ads(C)
#     手机号uphone(C)
#     性别sex(Ic)
#     角色role(Ic)
#     激活状态isActive(B)
#     是否禁用isBan(B)
# class UserInfo(models.Model):
#     username = models.CharField(max_length=50,verbose_name='用户名',null=False)
#     password = models.CharField(max_length=200,verbose_name='密码',null=False)
#     realname = models.CharField(max_length= 30,verbose_name='真实姓名',null=False)
#     iden = models.CharField('身份证号',max_length=18,null=False)
#     ads = models.CharField('地址',max_length=200,null=False)
#     uphone = models.CharField('手机号',max_length=20,null=False)
#     sex = models.IntegerField('性别',choices=ROLE_CHOICES,default=0)
#     role = models.IntegerField('角色',choices=SET_CHOICES,default=0)
#     isActive = models.BooleanField('是否激活',default=False)
#     isBan = models.BooleanField('是否禁用',default=False)

class UserInfo(AbstractUser):
    realname = models.CharField(max_length= 30,verbose_name='真实姓名',null=False)
    iden = models.CharField('身份证号',max_length=18,null=False)
    ads = models.CharField('地址',max_length=200,null=False)
    uphone = models.CharField('手机号',max_length=20,null=False)
    sex = models.IntegerField('性别',choices=ROLE_CHOICES,default=0)
    role = models.IntegerField('角色',choices=SET_CHOICES,default=0)
    isActive = models.BooleanField('是否激活',default=False)
    isBan = models.BooleanField('是否禁用',default=False)

    def __str__(self):
        return self.username

    # class Meta:
    #     # 指定表名
    #     db_table = 'userinfo'
    #     # 指定显示名称
    #     verbose_name = '用户表'
    #     verbose_name_plural = verbose_name

# 银行卡表Bankinfo
#     卡号cardNo(C)
#     用户user(F)
#     交易密码cpwd(C)
#     开户银行bank(Ic)
#     是否删除

class BankInfo(models.Model):
    cardno = models.CharField('卡号',max_length=30,null=False)
    user = models.ForeignKey(UserInfo)
    # user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    cpwd = models.CharField('交易密码',max_length=200,null=False)
    bank = models.IntegerField('开户银行',choices=BANK_CHOICES,default=0)
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.user.username