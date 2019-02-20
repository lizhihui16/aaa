from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$',login_),
    url(r'^log/$',register)

]