"""day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

dic={
    'name':'wangwc',
    'age':18
}

urlpatterns = [
    url(r'^login/', admin.site.urls),
    # #当我的访问路径为/sh
    # url(r'sh',sh_views),
    #当我的访问路径为　/show
    url(r'^show/$',show_views),
    #当访问路径为/show/四位数字的时候
    url(r'^show/(\d{4})/$',show1_views),
    #当访问路径为/show/四位数字/两位数字/两位数字的时候
    url(r'^show/(\d{4})/(\d{2})/(\d{2})/$',show2_views),
    #当访问路径为/show3/
    url(r'^show3/$',show3_views,dic)
]
