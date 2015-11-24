#coding=utf8
from django.conf.urls import url
from .views import *
urlpatterns = [
    url('^login', Login.as_view()),
    url('^register', Register.as_view()),

    #url('^logout', Logout.as_view()),
]
