from django.conf.urls import url
from .views import *

urlpatterns=[
    #当我的访问路径为　index/则将请求交给index_views视图处理函数去处理
    #完整的请求路径为http://localhost:8000/music/index
    # url(r'^index/$',index_views),
    #当访问路径为空的时候，则将请求交给index_views去处理
    url(r'^$',index_views)
]