from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uname=models.CharField(max_length=50,verbose_name='用户名',null=False)
    upassword=models.CharField('密码',max_length=200,null=False)
    email=models.CharField('邮箱',max_length=40,null=False)
    isban=models.BooleanField('禁用',default=False)

    def __str__(self):
        return self.uname

    class Meta:
        db_table=''
        verbose_name='用户表'
        verbose_name_plural=verbose_name




class Address(models.Model):
    aname=models.CharField('姓名',max_length=40,null=False)
    address=models.CharField('收站点',max_length=150,null=False)
    cellphone=models.CharField('手机号',max_length=15,null=False)
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.aname













