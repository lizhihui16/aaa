from django.conf.urls import url
from .views import *

# from cartinfo import views

urlpatterns= [
    url(r'^register/$',register_in,name='register'),
    url(r'^registerin/$',register_,name='register_in'),
    url(r'^login/$',signin,name='login'),
    url(r'^loginin/$',login_,name='login_in'),
    url(r'^loginout/$',login_out,name='login_out')
]