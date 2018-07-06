# /usr/bin/python3
# *_*coding:utf-8 *_*
from django.conf.urls import url
from .views import *
urlpatterns = [
	url(r'^',loginviews,name='login'),
]