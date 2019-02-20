from django.db.models import Avg, Count, Q, F
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def addbook_views(request):
    #方式１:Entry.objects.create()
    # book=Book.objects.create(title='Python编程基础',publicate_date='2015-10-12')
    # print('新增书籍的id为：%d'%book.id)

    # #方式２：通过Entry创建对象，对象.save()
    # book=Book(title='数据库基础')
    # book.publicate_date='2018-01-05'
    # book.save()
    # print('新增书籍的id为：%d'%book.id)

    # Book.objects.create(title='WEB开发基础',publicate_date='2018-01-15')
    # Book.objects.create(title='人工智能的发展',publicate_date='2015-11-15')
    # Book.objects.create(title='数据库的高级进价',publicate_date='2015-10-12')
    # Book.objects.create(title='python网络编程',publicate_date='2017-06-30')


    # Author.objects.create(name='王超',age=30,email='12212@163.com')
    # Author.objects.create(name='李白',age=25,email='321540230@163.com')
    # Author.objects.create(name="王福",age=22,email='156546545@163.com')
    # Author.objects.create(name='RapWang',age=31,email='Rapwang@163.com')
    # Author.objects.create(name='wangwc',age=33,email='wangwc@163.com')


    return HttpResponse('Add Book Success')


def query_views(request):
    #1.基本查询操作
    # books=Book.objects.all()
    # # print(type(books))
    # # print(books)
    # for book in books:
    #     print('ID:%d,书名:%s,出版日期：%s'%(book.id,book.title,book.publicate_date))
    # print(books.query)#打印输出SQL语句
    #

    #2.查询返回部分列
    # books=Book.objects.values('title','publicate_date')
    # for book in books:
    #     print('书名:%s,出版日期:%s'%(book["title"],book["publicate_date"]))


    #3.
    # books=Book.objects.values_list('id','title')
    # print(books)
    # for book in books:
    #     print('ID:%d,书名:%s'%(book[0],book[1]))


    #4.查询只返回一条数据
    # book=Book.objects.get(id=1)
    # print(book.title)


    #5查询id为１的book的信息
    #查询publicate_date为2015-10-12的book的信息
    # book=Book.objects.filter(id=1)
    # print(book)
    # list=Book.objects.filter(publicate_date='2015-10-12')
    # print(list)
    # for book in list:
    #     print('ID:%d,书名:%s,出版日期：%s'%(book.id,book.title,book.publicate_date))


    # list=Book.objects.filter(id=1,publicate_date='2015-10-12')
    # print(list)
    # for book in list:
    #     print('ID:%d,书名:%s,出版日期：%s'%(book.id,book.title,book.publicate_date))


    #7.查询publicate_date是2015年的所有数据
    # list=Book.objects.filter(publicate_date__year__gt=2015)
    # for book in list:
    #     print('ID:%d,书名:%s,出版日期：%s'%(book.id,book.title,book.publicate_date))




    # 1.查询出age小于等于30的Author的信息
    # list=Author.objects.filter(age__gte=30)
    # for auth in list:
    #     print('ID:%d,作者:%s,年龄：%s,邮箱：%s'%(auth.id,auth.name,auth.age,auth.email))

    # 2.查询出所有姓"王"的Author的信息
    # list=Author.objects.filter(name__startswith='王')
    # for auth in list:
    #     print('ID:%d,作者:%s,年龄：%s,邮箱：%s'%(auth.id,auth.name,auth.age,auth.email))

    # list=Author.objects.filter(email__contains='wang')
    # for auth in list:
    #     print('ID:%d,作者:%s,年龄：%d,邮箱：%s'%(auth.id,auth.name,auth.age,auth.email))

    #
    # #查询Author表中age大于"RapWang"的age的所有的信息
    # list=Author.objects.filter(age__gt=(Author.objects.get(id=4).age))
    #
    #
    # #查询Author中年龄不大于３５的人的信息
    # list=Author.objects.exclude(age__gt=30)
    #
    # list=Author.objects.order_by('-age')
    #
    #
    # for auth in list:
    #     print('ID:%d,作者:%s,年龄：%d,邮箱：%s'%(auth.id,auth.name,auth.age,auth.email))


    #查询author表中所有人的平均年龄－聚合函数aggregate
    # result=Author.objects.aggregate(avg=Avg('age'))
    # print('平均年龄为：%d'%result['avg'])


    #查询Book表中每个publicate_date所发行的书籍的数量
    list=Book.objects.values('publicate_date').annotate(count=Count('title')).values('publicate_date','count').all()
    list=Book.objects.filter(id__gt=1).values('publicate_date').annotate(count=Count('title')).values('publicate_date','count')
    print(list)

    return HttpResponse("<script>alert('查询成功!')</script>")



def all_views(request,id):
    list=Author.objects.filter(id=id)
    list.update(isActive=False)
    authors=Author.objects.filter(isActive=True).all()
    return render(request,'02-all.html',locals())

def authors_views(request):
    authors=Author.objects.filter(isActive=True)
    return render(request,'03-authors.html',locals())

def delete_views(request,id):
    list=Author.objects.filter(id=id)
    list.update(isActive=False)

    return redirect('/03-authors')


def update_views(request):
    # author=Author.objects.get(id=4)
    # author.name='wangwc'
    # author.age=30
    # author.email='wangwc@163.com '
    # author.save()


    # author=Author.objects.exclude(id=7)
    # author.update(name='jkhj',age=45)

    author=Author.objects.get(id=10)
    author.delete()
    return HttpResponse('Update Success')



def doQ_views(request):
    # Author.objects.all().update(age=F('age') + 100)
    #获取id=1或者isActive=True的Author们的信息
    authors=Author.objects.filter(Q(id=1)|Q(isActive=True))
    for a in authors:
        print('ID:%d,name:%s'%(a.id,a.name,))

    return HttpResponse('成功')


def oto_views(request):
    # #声明一个wife对象，并指明其author信息
    # wife=Wife()
    # wife.name='伟超夫人'
    # wife.age=30
    # wife.author_id=1
    # wife.save()


    # wife=Wife()
    # wife.name='Rapwang'
    # wife.age=29
    # author=Author.objects.get(id=3)
    # wife.author=author
    # wife.save()



    #查询－正向查询
    wife=Wife.objects.get(id=1)
    author=wife.author
    print('Wife:%s,Author:%s'%(wife.name,author.name))



    #反向查询
    author=Author.objects.get(id=1)
    wife=author.wife
    print('Wife:%s,Author:%s'%(wife.name,author.name))


    return HttpResponse("oto ok")


def otm_views(request):
    #正向查询：通过Book查询Publisher
    book=Book.objects.get(id=1)
    publisher=book.publisher
    print('书籍名称：'+book.title)
    print('所在出版社'+publisher.name)

    print('======================')

    #反向查询：通过Publisher查询Book
    pub=Publisher.objects.get(id=1)
    books=pub.book_set.all()
    print('所在出版社:'+pub.name)
    print('所出版的图书:')
    for book in books:
        print("Book Title:"+book.title)
    return HttpResponse('OK')



def mtm_views(request):
    #查询id=1的书籍的作者
    book=Book.objects.get(id=1)
    authors=book.author_set.all()
    print('书名：'+book.title)
    for au in authors:
        print('作者:'+au.name)

    print('=======================')
    #查询Rapwang所出版的书籍
    author=Author.objects.get(name='Rapwang')
    books=author.book_set.all()
    print(author.name+'所出版的书籍有：')
    for book in books:
        print('书名：'+book.title)
    return HttpResponse('3ok')


def mtmt(request):
    author=Author.objects.get(id=2)
    pub=author.publisher_set.all()
    print(author.name)
    for p in pub:
        print('出版社:'+p.name)

    print('============')
    publisher=Publisher.objects.get(id=1)
    au=publisher.author_set.all()
    print(publisher.name)
    for a in au:
        print('作者：'+a.name)

    return HttpResponse('ok')