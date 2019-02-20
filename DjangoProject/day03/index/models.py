from django.db import models

# Create your models here.

class Publisher(models.Model):
    #出版社名字
    name=models.CharField(max_length=30,verbose_name='名字')
    address=models.CharField(max_length=200,verbose_name='地址')
    #出版社地址
    city=models.CharField(max_length=30,verbose_name='城市')
    #出版社所在国家
    country=models.CharField(max_length=30,verbose_name='国家')
    #出版社网址
    website=models.URLField(null=True,verbose_name='网址')


    def __str__(self):
        return self.name
    class Meta:
        db_table='Publisher'
        verbose_name='出版社'
        verbose_name_plural=verbose_name




class Author(models.Model):
    name=models.CharField(max_length=30,verbose_name='姓名')
    age=models.IntegerField(verbose_name='年龄')
    email=models.EmailField(null=True,verbose_name='邮箱')
    isActive=models.BooleanField(default=True,verbose_name='邮箱用户')
    #增加对publisher的多对多的引用
    publisher_set=models.ManyToManyField(Publisher)

    def __str__(self):
        return self.name
    class Meta:
        #指定表名
        db_table='author'
        #指定显示名称
        verbose_name='作者'
        verbose_name_plural=verbose_name
        ordering=['-age']


class Book(models.Model):
    title=models.CharField(max_length=50,verbose_name='书名')
    publicate_date=models.DateField(verbose_name='出版时间')
    #增加对publicate(一)的一对多的引用
    publisher=models.ForeignKey(Publisher,null=True)
    #增加对Author的多对多的引用关系
    author_set=models.ManyToManyField(Author)

    def __str__(self):
        return self.title
    class Meta:
        #指定表名
        db_table='book'
        #指定显示名称
        verbose_name='书籍'
        verbose_name_plural=verbose_name
        ordering=['-publicate_date']



class Wife(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    #增加对Author的一对一关联关系
    author=models.OneToOneField(Author)

    def __str__(self):
        return self.name
    class Meta:
        db_table='wife'

