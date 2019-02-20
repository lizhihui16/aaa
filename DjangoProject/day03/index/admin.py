from django.contrib import admin
from .models import *

#声明Author的高级管理类AuthorAdmin
class AuthorAdmin(admin.ModelAdmin):
    #定义在列表页上显示的属性们
    list_display = ['name','age','email']
    #定义允许被点击的字段们
    list_display_links = ['name','email']
    #定义在列表页上就允许被修改的字段们
    list_editable = ['age']
    #添加允许被搜索的字段们
    search_fields = ['name','email']
    #右侧增加过滤器
    list_filter = ['name','email']
    # #指定在详情页中显示的z字段以及排列的顺序
    # fields = ['name','email','age']
    #指定在详情页中的字段分组们
    fieldsets = (
        (
            '基本选项',{
                'fields':('name','age'),
            }
        ),
        (
            '高级选项',{
                'fields':('email','isActive','publisher_set'),
                'classes':('collapse',)
            }
        )
    )


class BookAdmin(admin.ModelAdmin):
    list_display = ['title','publicate_date']
    date_hierarchy = 'publicate_date'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name','address','city']
    list_editable = ['address','city']
    search_fields = ['city','address','name','website']

    fieldsets = (
        (
            '基本选项',{
                'fields':('name','address','city'),
            }
        ),
        (
            '高级选项',{
                'fields':('country','website'),
                'classes':('collapse',)
            }
        )
    )







# Register your models here.

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife)


