from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^$',cart_info,name='cart'),
    url(r'^addcart/$',add_cart,name='addcart'),
    url(r'^deletecart/$',delete_cart,name='deletecart'),

]